#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

def random_name(sex=-1):
    if sex == -1:
        sex = random.randint(0, 1)

    first_name = "赵钱孙李周吴郑王冯陈褚"
    girl = "秀娟英华慧巧美娜静淑惠珠翠雅芝"
    boy = "伟刚勇毅俊峰强军平保东文辉力"

    first = random.choice(first_name)
    if sex == 0:
        names = boy
    else:
        names = girl
    # names = boy if sex == 0 else girl
    second = random.choice(names)
    has_third = random.randint(0, 1)
    if has_third == 1:
        third = random.choice(names)
    else:
        third = ''
    # third = random.choice(names) if has_third == 1 else ''

    full_name = first + second + third
    return full_name

name1=random_name()
name2=random_name(0)
name3=random_name(1)
print(name1,name2,name3,sep=' | ')