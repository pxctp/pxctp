#-*- coding:utf-8 -*-

import threading
from FinalLogger import logger
from Strategy import Strategy
from Indicators import Indicators

import sys
if sys.platform == 'win32':
    from ctp_win32 import ApiStruct
elif sys.platform == 'linux2' :
    from ctp_linux64 import ApiStruct

s = S = ApiStruct.D_Sell
b = B = ApiStruct.D_Buy
k = K = ApiStruct.OF_Open
p = P = ApiStruct.OF_Close

b_limit = 0


class StrategyFairyFour(threading.Thread, Strategy):
    def __init__(self, inst, volume = 1):
        Strategy.__init__(self, inst)
        threading.Thread.__init__(self)
        self.volume = volume
        self.InitIndicator()

        self.b_limit = 0
        self.s_limit = 0

    def InitIndicator(self):
        pass # no need to calculate indicator in this strategy

    def run(self):
        Strategy.strategy_state[self.tick.InstrumentID] = True
        daybar_list = Indicators.getDayBarList(self.tick.InstrumentID)
        if not daybar_list:
            print 'Need one bar at least in database'
            threading.Thread.__init__(self)
            Strategy.strategy_state[self.tick.InstrumentID] = False
            return

        last_daybar = daybar_list[-1]
        #open, high, low, close, volume
        last_high = last_daybar[1]
        last_low = last_daybar[2]

        b_sendorder, s_sendorder = self.getSendOrderCount()

        #print self.tick
        print self.tick.AveragePrice/10

        #b_limit = 0
        if self.tick.LastPrice > (self.tick.AveragePrice/10 + 2) and self.b_limit <3:
            self.PrepareOrder(self.tick.InstrumentID, B, P, s_sendorder, self.tick.LastPrice)  # LastPrice
            print u"buy one."
            self.b_limit += 1



        if self.tick.LastPrice > last_high : # close short and open long

            '''
            if s_sendorder > 0 :
                self.PrepareOrder(self.tick.InstrumentID, ApiStruct.D_Buy, ApiStruct.OF_Close, s_sendorder, self.tick.UpperLimitPrice) # LastPrice
            elif b_sendorder < self.volume :
                self.PrepareOrder(self.tick.InstrumentID, ApiStruct.D_Buy, ApiStruct.OF_Open, self.volume-b_sendorder, self.tick.UpperLimitPrice)
            '''
            if s_sendorder > 0 :
                self.PrepareOrder(self.tick.InstrumentID, B, P, s_sendorder, self.tick.LastPrice) # LastPrice
            elif b_sendorder < self.volume :
                self.PrepareOrder(self.tick.InstrumentID, B, K, self.volume-b_sendorder, self.tick.LastPrice)

        if self.tick.LastPrice < last_low : # close long and open short
            if b_sendorder > 0:
                self.PrepareOrder(self.tick.InstrumentID, S, P, s_sendorder, self.tick.LastPrice)  # LastPrice
            elif s_sendorder < self.volume :
                self.PrepareOrder(self.tick.InstrumentID, S, K, self.volume-s_sendorder, self.tick.LastPrice)

        # in case restart/reuse thread since python not support
        threading.Thread.__init__(self)
        Strategy.strategy_state[self.tick.InstrumentID] = False


    def PrepareOrder(self, inst, direc, open_close, volume, price):
        order = self.formatOrder(inst, direc, open_close, volume, price)
        self.sendOrder(order)















