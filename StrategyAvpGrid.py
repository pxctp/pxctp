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
s_limit = 0

class StrategyAvpGrid(threading.Thread, Strategy):
    def __init__(self, inst, volume = 1):
        Strategy.__init__(self, inst)
        threading.Thread.__init__(self)
        self.volume = volume
        self.InitIndicator()
        self.b_limit = 0
        self.s_limit = 0

        self.lastprice = []
        self.avprice = []


    def InitIndicator(self):
        pass # no need to calculate indicator in this strategy

    # def Every(self,a,b): #判断是否a>b, every item in a is larger than every item in b correspondingly.
    #     print a, type(a)
    #
    #
    #     for i in range(len(a)):
    #         if a[i] < b[i]:
    #             return False
    #         return  True


    def run(self):


        self.lastprice.append(int(self.tick.LastPrice ))

        self.avprice.append(int(self.tick.AveragePrice/10))


        if len(self.lastprice)>10 and len(self.avprice)>10:
            self.lastprice.pop(0)        
            self.avprice.pop(0)

            if self.lastprice[-5]>self.avprice[-5]:
                Clastprice = self.lastprice[-4:]
                AVlastprice = self.avprice[-4:]

                print Clastprice

                print AVlastprice

        print self.tick.LastPrice

        #print self.lastprice
        #print self.avprice


        Strategy.strategy_state[self.tick.InstrumentID] = True



        '''
        if len(self.lastprice)>33:
            self.newprice = self.lastprice[-6:]
            self.avpnprice = self.avprice[-6:]


            #print self.newprice
            #print self.avpnprice
            aa = self.newprice.pop(0)
            bb = self.avpnprice.pop(0)

            print aa
            print bb


        if self.newprice[0] < self.avpnprice[0] and self.Every(aa, bb) and self.b_limit<3:
            self.PrepareOrder(self.tick.InstrumentID, B, K, 1, self.tick.LastPrice)  # LastPrice
            self.b_limit += 1

        if self.newprice[0] > self.avpnprice[0] and self.Every(bb,aa) and self.s_limit < 3:
            self.PrepareOrder(self.tick.InstrumentID, S, K, 1, self.tick.LastPrice)  # LastPrice
            self.s_limit += 1

            #b_sendorder, s_sendorder = self.getSendOrderCount()

            print self.tick.InstrumentID, self.tick.LastPrice, self.tick.AveragePrice/10

        
        '''

        # in case restart/reuse thread since python not support

        threading.Thread.__init__(self)
        Strategy.strategy_state[self.tick.InstrumentID] = False

    def PrepareOrder(self, inst, direc, open_close, volume, price):
        order = self.formatOrder(inst, direc, open_close, volume, price)
        self.sendOrder(order)















