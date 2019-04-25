#!/usr/bin/python3
#coding:utf-8

from prehost import find_html_ele
from config import *
import unittest

class hzz_data_fh(find_html_ele):
    u'''复核通过'''
    # @unittest.skip('跳过')
    def test_01(self):
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务复核')
        for a in range(99):
            time.sleep(1)
            super().fuhe()
            super().fuhe_tg()
            time.sleep(1)
            super().fuhe_sure()


    @unittest.skip('跳过')
    def test_02(self):
        u'''复核不通过'''
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务复核')
        for a in range(50):
            super().fuhe()
            super().tuihui('退回了')
            super().tuihui_tg()
            time.sleep(1)
            super().fuhe_sure()









if __name__ == "__main__":
    pass