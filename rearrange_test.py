#!/usr/bin/env python3

import unittest

from rearrange_name import rearrange_name

class Test_Rearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        assert rearrange_name(testcase) == expected

    def test_empty(self):
        testcase = ""
        expected = ""
        assert rearrange_name(testcase) == expected

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        assert rearrange_name(testcase) == expected

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        assert rearrange_name(testcase) == expected

unittest.main()