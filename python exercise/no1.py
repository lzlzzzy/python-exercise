# -*- coding: utf-8 -*-
'''
	实现功能：
	1.macd指标计算
	2.记录金叉死叉数据并输出CSV文件
'''
import pandas as pd
from datetime import datetime,timedelta
import tushare as ts
import sys

sys.setrecursionlimit(3000) #设置最大遍历次数
pd.set_option('display.width', 280) # 打印最大列数设置


def MACD(df, n_fast, n_slow, ksgn='close'):
    '''
    def MACD(df, n_fast, n_slow):
      #MACD指标信号和MACD的区别, MACD Signal and MACD difference
	MACD是查拉尔·阿佩尔(Geral Appel)于1979年提出的，由一快及一慢指数移动平均（EMA）之间的差计算出来。
	“快”指短时期的EMA，而“慢”则指长时期的EMA，最常用的是12及26日EMA：

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】
        df, pd.dataframe格式数据源,
        增加了3栏：macd,sign,mdiff
    '''
    xnam = 'macd'.format(n=n_fast, n2=n_slow)
    xnam2 = 'msign'.format(n=n_fast, n2=n_slow)
    xnam3 = 'mdiff'.format(n=n_fast, n2=n_slow)
    EMAfast = pd.Series(pd.ewma(df[ksgn], span=n_fast, min_periods=n_slow - 1))
    EMAslow = pd.Series(pd.ewma(df[ksgn], span=n_slow, min_periods=n_slow - 1))
    MACD = pd.Series(EMAfast - EMAslow, name=xnam)
    MACDsign = pd.Series(pd.ewma(MACD, span=9, min_periods=8), name=xnam2)
    MACDdiff = pd.Series(MACD - MACDsign, name=xnam3)
    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff)
    return df


def gold_kill(df):
    '''
    金叉死叉信息筛选
    :param df:
    :return:
    '''
    df['msign_old'] = df['msign'].shift(1)
    df['macd_old'] = df['macd'].shift(1)
    killdate = df[(df['msign_old']<df['macd_old']) & (df['msign'] > df['macd'])]
    golddate = df[(df['msign_old']>=df['macd_old']) & (df['msign'] <= df['macd'])]
    return golddate,killdate

#记录运行开始时间
stardate = datetime.now()
#获取最新A股数据
stockdf = ts.get_stock_basics()
#金叉死叉数据集
stock_gold_kill_info = pd.DataFrame(columns=['code','name','date','close','lastgolddate','lastgoldclose','lastkilldate','lastkillclose'])
# 计数变量
n = 1
#从180的数据开始计算，可更改
startime = datetime.strftime(stardate-timedelta(days=180),'%Y-%m-%d')
#遍历A股数据
for code in stockdf.index:
    # 运行进度条
    i = int(n/len(stockdf)*100)
    s1 = "\r[%s%s]%d/%d"%("*"*i," "*(100-i),n,len(stockdf))
    sys.stdout.write(s1)
    sys.stdout.flush()
    n += 1
    # 获取截止当前日期的日K数据
    df = ts.get_hist_data(code,startime)
    #新股、停牌股等特殊情况没有金叉死叉数据，报错忽略
    try:
        df.sort_index(inplace=True)
        macddf = MACD(df,12,26)
        gold,kill=gold_kill(macddf)
        gold_kill_info = {
                          'lastgolddate': gold.tail(1).index.values[0], #最近一次金叉时间
                          'lastgoldclose': gold.tail(1).close.values[0], #最近一次金叉收盘价
                          'lastkilldate': kill.tail(1).index.values[0], #最近一次死叉时间
                          'lastkillclose': kill.tail(1).close.values[0], #最近一次死叉收盘价
                          'date':df.tail(1).index.values[0], #最新收盘价日期
                          'code':code, #股票代码
                          'close':df.tail(1).close.values[0], #最新收盘价
                          'name':stockdf[stockdf.index == code].name.values[0] #股票名字
                          }
    except (IndexError,AttributeError) as e:
        continue
    # 追加到金叉死叉数据集
    stock_gold_kill_info = stock_gold_kill_info.append(pd.DataFrame.from_dict(gold_kill_info,orient='index').T,ignore_index=True)
#保存金叉死叉数据集，目录与运行文件一样，可更改
stock_gold_kill_info.to_csv('stock_gold_kill_info.csv',index = False,encoding='gbk')

enddate = datetime.now()
print('\n运行时间：',enddate-stardate)