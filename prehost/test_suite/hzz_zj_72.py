#!/usr/bin/python3
#coding:utf-8

from prehost.hzz_zj_ele import find_html_ele
from config import *


class hzz_data_add_72(find_html_ele):
    u'''账户核准制增加72类型'''
    # @unittest.skip('跳过')
    def test_72_2(self):
        u'''72_2 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('72')
        super().first_accountattr('2')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_72_3(self):
        u'''72_3 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('72')
        super().first_accountattr('3')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_72_4(self):
        u'''72_4 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('72')
        super().first_accountattr('4')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_72_6(self):
        u'''72_6 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('72')
        super().first_accountattr('6')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_72_7(self):
        u'''72_7 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('72')
        super().first_accountattr('7')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()

    # @unittest.skip('跳过')
    def test_72_8(self):
        u'''72_8 类型测试'''
        time.sleep(2)
        super().show_tree()
        super().dwzh_hzz()
        super().change_iframe('核准制业务申报')
        super().data_add()
        super().first_businesstype('72')
        super().first_accountattr('8')
        super().sure_yes()
        #录入信息
        super().add_ele_50_71_72_73_74('accountno', test_number)
        super().add_ele_50_71_72_73_74('accountname', test_text)
        # 上传
        super().click_sc()
        super().input_file()
        super().sure_upload()
        super().sure_comm()
        time.sleep(2)
        super().sure_final_upload()
        #返回主iframe
        super().switch_default_iframe()









if __name__ == "__main__":
    pass