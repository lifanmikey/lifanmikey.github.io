# -*- coding:utf-8 -*-

# import numpy as np
# import matplotlib.pyplot as plt
#
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure("2subplot")
# plt.subplot(211)
# plt.ylabel('some')
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.xlabel('k')
# plt.ylabel('some2')
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

# import warnings
# import matplotlib.pyplot as plt
#
# warnings.filterwarnings('ignore')
# plt.figure(1)
# plt.subplot(211)             # figure1中的第一个子图
# plt.plot([1, 2, 3])
# plt.subplot(212)             # figure1中的第二个子图
# plt.plot([4, 5, 6])
#
#
# plt.figure(2)                # figure2
# plt.plot([4, 5, 6])          # 默认使用subplot(111),此时figure2为当
#                              # 前figure
#
# plt.figure(1)                # 设置figure1为当前figure;
#                              # 但是subplot(212)为当前子图
# plt.subplot(211)             # 使subplot(211)为当前子图
# plt.title('Easy as 1, 2, 3') # 对subplot(211)命名
# plt.show()

# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
#
# print dict['one']  # 输出键为'one' 的值
# print dict[2]  # 输出键为 2 的值
# print dict
# print tinydict  # 输出完整的字典
# print tinydict.keys()  # 输出所有键
# print tinydict.values()  # 输出所有值

# i = 1
# while 1:            # 循环条件为1必定成立
#     print i         # 输出1~10
#     i += 1
#     if i > 10:     # 当i大于10时跳出循环
#         break

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# var = 1
# while var == 1:  # 该条件永远为true，循环将无限执行下去
#     num = raw_input("Enter a number  :")
#     print "You entered: ", num
#
# print "Good bye!"
