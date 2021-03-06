import unittest
import ccs
import time
import datetime

####################################################################################################################
# BTCCPRO                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCPRO
        self.base = ccs.constants.XBT
        self.quote = ccs.constants.CNY
        symbol = ccs.btccpro.Symbol(self.base, self.quote)

        self.tz = datetime.timezone.utc

        self.json = '{"asks":[[6929,22],[6930,25]],"bids":[[6910.3,11],[6903,4]],"date":1486145574689}'
        self.orderbook = ccs.btccpro.public.response.OrderBook(self.json, symbol)

        self.ordersA = self.orderbook.asks()
        self.orderA = self.ordersA[0]
        self.ordersB = self.orderbook.bids()
        self.orderB = self.ordersB[0]
        self.m = ccs.btccpro.public.response
        # time.sleep(3)

    def testPrice(self):
        self.assertEqual(self.orderA.price(), 6929)
        self.assertEqual(self.orderB.price(), 6910.3)

    def testAmount(self):
        self.assertEqual(self.orderA.amount(), 22)
        self.assertEqual(self.orderB.amount(), 11)

    def testStock(self):
        self.assertEqual(self.orderA.stock(), self.stock)
        self.assertEqual(self.orderB.stock(), self.stock)

    def testMethod(self):
        self.assertEqual(self.orderA.method(), ccs.constants.ORDER)
        self.assertEqual(self.orderB.method(), ccs.constants.ORDER)

    def testUsymbol(self):
        self.assertEqual(self.orderA.usymbol(), self.base + ":" + self.quote)
        self.assertEqual(self.orderB.usymbol(), self.base + ":" + self.quote)

    def testOsymbol(self):
        pass

    def testData(self):
        pass

    def testRaw(self):
        pass

    def testStr(self):
        pass


if __name__ == '__main__':
    unittest.main()








