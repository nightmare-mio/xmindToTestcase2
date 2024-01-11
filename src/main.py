'''
Author: nightmare-mio wanglongwei2009@qq.com
Date: 2023-11-02 00:03:10
LastEditTime: 2024-01-11 22:07:59
Description: 
'''
#coding:utf8
# import subprocess

# 安装依赖包
# import os
# file_path = os.path.dirname(os.path.dirname(__file__))
# print(file_path)
# setup_path = os.path.join(file_path, 'lib', 'setup.py')
# subprocess.Popen('python3 ' + setup_path + ' install', shell=True)

from lib.readXmind import *
from  lib.writeExcel import *
from  lib.headExcel import *
import logging
def get_xmind_content(xmind_file,output_file):
    #生成测试用例
    read_xmind = ReadXmindList(xmind_file)
    # excel_title=read_xmind.excel_title #获取模块标题
    head_excel=headExcel()
    write_excel = WriteExcel(output_file,head_excel)
    testcase_list = []
    read_xmind.get_list_content(read_xmind.content, testcase_list, write_excel,template="template0" )#写入excel
    write_excel.write_analysis_wooksheek()#写入测试分析excel
    write_excel.save_excel() #保存excel
    logging.info("Generate Xmind file successfully: {}".format(output_file))
    
    # 固定模板1
def get_xmind_content_template(xmind_file,output_file):
    #生成测试用例
    read_xmind = ReadXmindList(xmind_file)
    # excel_title=read_xmind.excel_title #获取模块标题
    head_excel=headExcel()
    head_excel.head_testcase=["storyid", '所属模块','子模块','用例标题', '前置条件', '步骤', '预期', '用例类型', '实际结果',"备注"]
    write_excel = WriteExcel(output_file,head_excel)
    testcase_list = []
    read_xmind.get_list_content(read_xmind.content, testcase_list, write_excel,template="template1")#写入excel
    write_excel.write_analysis_wooksheek()
    write_excel.save_excel() #保存excel
    logging.info("Generate Xmind file successfully: {}".format(output_file))
    
    # yatop
def get_xmind_content_template_yatop(xmind_file,output_file):
    #生成测试用例
    read_xmind = ReadXmindList(xmind_file)
    # excel_title=read_xmind.excel_title #获取模块标题
    head_excel=headExcel()
    head_excel.head_testcase=head_excel.head_testcase_yatop
    write_excel = WriteExcel(output_file,head_excel)
    testcase_list = []
    read_xmind.get_list_content(read_xmind.content, testcase_list, write_excel,template="template_yatop")#写入excel
    write_excel.write_analysis_wooksheek()
    write_excel.save_excel() #保存excel
    logging.info("Generate Xmind file successfully: {}".format(output_file))
    
# 由用户输入模板
def get_xmind_content_auto_template(xmind_file,output_file,head):
    read_xmind = ReadXmindList(xmind_file)
    head_excel=headExcel()
    head_excel.head_testcase=head
    write_excel = WriteExcel(output_file,head_excel)
    testcase_list = []
    read_xmind.get_list_content(read_xmind.content, testcase_list, write_excel,template="auto_template")#写入excel
    write_excel.write_analysis_wooksheek()
    write_excel.save_excel() #保存excel
    logging.info("Generate Xmind file successfully: {}".format(output_file))