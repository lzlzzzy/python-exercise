# -*- coding: utf-8 -*-
'''
    实现功能：
    1. macd指标计算
    2. 记录金叉死叉数据并输出CSV文件
'''

import pandas as pd
from datetime import datetime, timedelta
import tushare as ts
import sys
import time

# 初始化 Tushare Pro
ts.set_token('cf1cf3c9288b9d536461ac61c4a1006db76763b665e47b44c19660e7')  # 替换为您的 API Token
pro = ts.pro_api()

sys.setrecursionlimit(3000)
pd.set_option('display.width', 280)

def MACD(df, n_fast, n_slow, ksgn='close'):
    EMAfast = df[ksgn].ewm(span=n_fast, adjust=False).mean()
    EMAslow = df[ksgn].ewm(span=n_slow, adjust=False).mean()
    MACD = EMAfast - EMAslow
    MACDsign = MACD.ewm(span=9, adjust=False).mean()
    MACDdiff = MACD - MACDsign
    df['macd'] = MACD
    df['msign'] = MACDsign
    df['mdiff'] = MACDdiff
    return df

def gold_kill(df):
    df['msign_old'] = df['msign'].shift(1)
    df['macd_old'] = df['macd'].shift(1)
    killdate = df[(df['msign_old'] < df['macd_old']) & (df['msign'] > df['macd'])]
    golddate = df[(df['msign_old'] >= df['macd_old']) & (df['msign'] <= df['macd'])]
    return golddate, killdate

stardate = datetime.now()
stockdf = pd.DataFrame()

# 获取所有股票的基本信息
try:
    stockdf = pro.stock_basic()
except Exception as e:
    print(f"Error retrieving stock basics: {e}")
    sys.exit(1)

stock_gold_kill_info = pd.DataFrame(columns=['code', 'name', 'date', 'close', 'lastgolddate', 'lastgoldclose', 'lastkilldate', 'lastkillclose'])
n = 1
startime = datetime.strftime(stardate - timedelta(days=180), '%Y-%m-%d')

for code in stockdf['ts_code'][0:10]:
    i = int(n / len(stockdf) * 100)
    s1 = "\r[%s%s]%d/%d" % ("*" * i, " " * (100 - i), n, len(stockdf))
    sys.stdout.write(s1)
    sys.stdout.flush()
    n += 1

    try:
        df = pro.daily(ts_code=code, start_date=startime.replace('-', ''), end_date=datetime.strftime(stardate, '%Y%m%d'))
        if df.empty:
            continue

        df.sort_values(by='trade_date', inplace=True)
        macddf = MACD(df, 12, 26)
        gold, kill = gold_kill(macddf)

        last_gold_info = {
            'lastgolddate': gold.tail(1)['trade_date'].values[0] if not gold.empty else None,
            'lastgoldclose': gold.tail(1)['close'].values[0] if not gold.empty else None,
        }
        last_kill_info = {
            'lastkilldate': kill.tail(1)['trade_date'].values[0] if not kill.empty else None,
            'lastkillclose': kill.tail(1)['close'].values[0] if not kill.empty else None,
        }

        gold_kill_info = {
            'date': df.tail(1)['trade_date'].values[0],
            'code': code,
            'close': df.tail(1)['close'].values[0],
            'name': stockdf[stockdf['ts_code'] == code]['name'].values[0],
            **last_gold_info,
            **last_kill_info,
        }

        stock_gold_kill_info = stock_gold_kill_info._append(gold_kill_info, ignore_index=True)

    except Exception as e:
        print(f"\nError fetching data for {code}: {e}")
        continue

stock_gold_kill_info.to_csv('./stock_gold_kill_info.csv', index=False, encoding='gbk')

enddate = datetime.now()
print('\n运行时间：', enddate - stardate)
