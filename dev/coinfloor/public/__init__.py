import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response

def ticker(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + '/' + cur2

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def transactions(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + '/' + cur2

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + '/' + cur2

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))