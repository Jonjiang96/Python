# Author: Jon
# -*- coding: UTF-8 -*-
import  json
nums = {}
cr_bought = []
bought_item = 'bought_item.json'                                             #已购买商品列表
balance = 'balance.json'
p_list = 'productions.json'
try:
    with open(balance) as fb_obj:
        r_balance = str(json.load(fb_obj))
except json.decoder.JSONDecodeError:
    salary = input("Input your salary:")
    r_balance = salary
print('your balance is %s'.capitalize() % r_balance)

with open(p_list) as fp_obj:
    production_list = json.load(fp_obj)
if r_balance.isdigit():                                    # 将字符数字转换为数字
    r_balance = int(r_balance)
    print('编号 商品名 单价\n'.rstrip())
    for index, item in enumerate(production_list):       # 打印商品列表
        print(index, '\t', item, '\t', production_list[item])
    while True:
        for num, item in enumerate(production_list):
            nums[num] = item
        custmer_chioce = input("Choice your item number...")    # 选择商品编号
        if custmer_chioce.isdigit():
            custmer_chioce = int(custmer_chioce)
            if custmer_chioce in nums:
                p = nums[custmer_chioce]
                if r_balance > production_list[p]:                 # 取出商品加入购买清单打印商品及余额
                        r_balance -= production_list[p]
                        cr_bought.append(nums[custmer_chioce])
                        print("Added %s your cart..your balance is %d RMB" % (nums[custmer_chioce], r_balance))
                else:
                    print("Your balance is not enough...fuck off")
            else:
                print("Input invalid")
        else:                                                       # 退出
            if custmer_chioce == "q":
                with open(bought_item, 'a+') as fbo_obj:
                    json.dump(cr_bought, fbo_obj)
                with open(balance, 'w+') as fb_obj:
                    json.dump(r_balance, fb_obj)
                print('Your bought item '+ str(cr_bought)  + '\tYour balance is '+ str(r_balance) + 'RMB')
                break
''' 
----------重点------------
1、方法isdigit
    salary.isdigit() >> 判断salary 是否是数字，包含字符数字和数值型数字
2、方法len
    len(production_list) >> 取列表长度，并返回列表长度值
3、方法enumerate
    for index,item in enumerate(production_list):     >> 打印出列表下标
        print(index,item)
4、列表，数组使用
    production_list = 
    [                                    >> 列表(list)值可改变，多种操作 
    ("Bike",5000),                       >> 数组(tuple)值不可改变，只有index和count操作
    ("Book",31),
    ("Wacth",1000),
    ("Iphon",6000),
    ("Mac_pro",9000)
    ]
5、异常处理
    try:
        sentence..(可能出错的语句，例：打开未存在的文件)
    except  typeEEOR  ：
        sentence..（出现异常错误后，如何处理）
    else:
        sentence...（未出现异常错误，执行语句）
        

'''
