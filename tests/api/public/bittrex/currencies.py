# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Bittrex. This endpoint offer informations about currencies.
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"


import unittest
import ccs
import jsonschema
import json
import time


def schema():
    return ccs.bittrex.configuration.SCHEMA["getCurrencies"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        sleep()

    def testSchema(self):
        r = ccs.bittrex.public.getCurrencies()
        jsonschema.validate(json.loads(r), schema())


class Invalid(unittest.TestCase):
    def setUp(self):
        pass

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = '{"success":false,"message":"INVALID","result":null}'
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
