#!/usr/bin/env python
# -*- coding:utf-8 -*-
# # class ClassA1():
# #     a1 = 10
# #
# #     def print_a(self):
# #         print(self.a1)
# #
# # d = ClassA1()
# # d.print_a()
# class phone():
#     name="xiaomi"
#     def __init__(self,color):
#         self.color=color
#         print(self.color)
#
#     def chicun(self):
#         print("6cun")
#
#     def duanxin(self):
#         print("短信")
# # o = phone("黑")
# # o.chicun()
# #o.duanxin()

# import json
# d = '''{"name":"小明","sex":"未知"}'''
# c = json.loads(d)
# c["sex"]="男"
# print(c)
#
# k = json.dumps(c,ensure_ascii=False)
# print(k)
#
# import random
# d = random.randint (1,32)
# print(d)
#
# e = random.choice(["asd","123","ert"])
# print(e)

# import os
#
# f = os.path.abspath("957.txt")
# print(f)
#
# g = os.path.basename(f)
# print(g)
#
# h = os.path.dirname(f)
# print(h)
#
# os.system(cmd)
# l = ["小明","小张"]
# l.insert(1,"小红")
# print(l)
#
# # pop默认删除列表最后一个元素
# l = ["小明","小张","小红"]
# l.pop()
# print(l)
# # pop 可以根据下标删除元素
# l.pop(0)
# print(l)
import os
try :
    os.mkdir("xin")
except FileExistsError:
    print("已经创建")
else:
    print()
