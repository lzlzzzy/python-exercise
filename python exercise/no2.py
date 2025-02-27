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

sys.setrecursionlimit(3000)
pd.set_option('display.width', 280)

def MACD(df, n_fast, n_slow, ksgn='close'):
    xnam = 'macd'
    xnam2 = 'msign'
    xnam3 = 'mdiff'
    EMAfast = pd.Series(pd.ewm.mean(df[ksgn], span=n_fast, min_periods=n_slow - 1))
    EMAslow = pd.Series(pd.ewm.mean(df[ksgn], span=n_slow, min_periods=n_slow - 1))
    MACD = pd.Series(EMAfast - EMAslow, name=xnam)
    MACDsign = pd.Series(pd.ewm.mean(MACD, span=9, min_periods=8), name=xnam2)
    MACDdiff = pd.Series(MACD - MACDsign, name=xnam3)
    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff)
    return df

def gold_kill(df):
    df['msign_old'] = df['msign'].shift(1)
    df['macd_old'] = df['macd'].shift(1)
    killdate = df[(df['msign_old'] < df['macd_old']) & (df['msign'] > df['macd'])]
    golddate = df[(df['msign_old'] >= df['macd_old']) & (df['msign'] <= df['macd'])]
    return golddate, killdate

stardate = datetime.now()
stockdf = pd.DataFrame()

# 重试机制
for attempt in range(3):
    try:
        stockdf = ts.get_stock_basics()
        if stockdf is not None:  # 确保获取的数据不为空
            break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        time.sleep(5)  # 等待5秒后重试
else:
    print("Failed to retrieve stock basics after 3 attempts.")
    sys.exit(1)

stock_gold_kill_info = pd.DataFrame(columns=['code', 'name', 'date', 'close', 'lastgolddate', 'lastgoldclose', 'lastkilldate', 'lastkillclose'])
n = 1
startime = datetime.strftime(stardate - timedelta(days=180), '%Y-%m-%d')

for code in stockdf.index:
    i = int(n / len(stockdf) * 100)
    s1 = "\r[%s%s]%d/%d" % ("*" * i, " " * (100 - i), n, len(stockdf))
    sys.stdout.write(s1)
    sys.stdout.flush()
    n += 1

    for attempt in range(3):
        try:
            df = ts.get_hist_data(code, startime)
            if df is None:  # 如果没有数据，跳过
                break

            df.sort_index(inplace=True)
            macddf = MACD(df, 12, 26)
            gold, kill = gold_kill(macddf)

            last_gold_info = {
                'lastgolddate': gold.tail(1).index.values[0] if not gold.empty else None,
                'lastgoldclose': gold.tail(1).close.values[0] if not gold.empty else None,
            }
            last_kill_info = {
                'lastkilldate': kill.tail(1).index.values[0] if not kill.empty else None,
                'lastkillclose': kill.tail(1).close.values[0] if not kill.empty else None,
            }

            gold_kill_info = {
                'date': df.tail(1).index.values[0],
                'code': code,
                'close': df.tail(1).close.values[0],
                'name': stockdf[stockdf.index == code].name.values[0],
                **last_gold_info,
                **last_kill_info,
            }
            break  # 成功获取数据后跳出重试循环
        except Exception as e:
            print(f"\nError fetching data for {code} on attempt {attempt + 1}: {e}")
            time.sleep(5)  # 等待5秒后重试
    else:
        continue  # 如果重试失败，跳过该股票

    stock_gold_kill_info = stock_gold_kill_info.append(pd.DataFrame.from_dict(gold_kill_info, orient='index').T, ignore_index=True)

stock_gold_kill_info.to_csv('./stock_gold_kill_info.csv', index=False, encoding='gbk')

enddate = datetime.now()
print('\n运行时间：', enddate - stardate)
