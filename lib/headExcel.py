'''
Author: nightmare-mio wanglongwei2009@qq.com
Date: 2023-10-31 23:12:44
LastEditTime: 2024-01-11 21:28:29
Description: 
'''
from typing import Any


class headExcel(object):
    def __init__(self):
        # 默认使用的head_testcase
        self.head_testcase=['用例目录', '用例名称', '前置条件', '用例步骤', '预期结果', '用例类型', '用例状态', '用例等级', '需求ID',
                '创建人', '测试结果', '是否开发自测']
        self.head_testscope=['序号', '功能模块', '功能名称', '角色', '责任人', '更新日期', '备注']
        self.head_outline= ['需求编号', '功能模块', '功能名称', '功能点', '用例类型', '检查点', '用例设计', '预期结果', '类别',
                '责任人', '状态', '更新日期', '用例编号']
        self.head_testcase_1=["storyid", '所属模块','子模块','用例标题', '前置条件', '步骤', '预期', '用例类型', '实际结果',"备注"]
        self.head_testcase_yatop=["storyid", '所属模块', '用例标题', '前置条件', '步骤', '预期', '用例类型', '实际结果',"备注"]