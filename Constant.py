#-*- coding=utf-8 -*-
#one inst -> one strategy/thread, and customized indicators
'''
inst_strategy = {'rb1801': {'strategy':'StrategyRBreaker', 'volume':3},
                 'rb1805': {'strategy':'StrategyFairyFour'},
                 'hc1805' : {'strategy':'StrategyDoubleMA', 'fast':7,'slow':30, 'volume':2},
                 }
'''
inst_strategy = {'rb1801': {'strategy':'StrategyRBreaker', 'volume':3},
                 'hc1805': {'strategy':'StrategyAvpGrid'}
                 }



#{'p1701', strategy_thread}
inst_thread = {}

# {'inst', [DayBar, SendOrder, RtnOrder]}
#             |_____[ bar1, bar2, bar3, ...]
#                      |_____(open, high, low, close, ...)
database_map = {}
suffix_list = ['_DayBar', '_SendOrder', '_RtnOrder']


BROKER_ID = "9999"
INVESTOR_ID = "105686"
PASSWORD = "ftp123"

#std ctp
#ADDR_MD = "tcp://180.168.146.187:10010"
#ADDR_TRADE = "tcp://180.168.146.187:10000"


#7*24 ctp for testing

ADDR_MD = "tcp://180.168.146.187:10031"
ADDR_TRADE = "tcp://180.168.146.187:10030"


TICK_DIR = './ticks/'
LOGS_DIR = './logs/'

OPEN,HIGH,LOW,CLOSE = range(4)




