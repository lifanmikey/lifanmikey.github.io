# coding:utf-8

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import re

# 读取txt文件数据,有多个空格间隔

G = nx.Graph()
filename = r'E:\dataset\jazz.txt'
node_list = []
lnum = 0
with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()  # 整行读取数据
        if not lines:
            break
            pass
        lnum += 1
        # 从第四行开始处理数据
        if lnum >= 4:
            # 对多的空格进行处理
            temp = ' '.join(re.split(' +|\n+', lines)).strip()
            line = re.split(' ', temp.strip())
            # 获得第一个节点
            first_node = line[0]
            # 获得第二个节点
            second_node = line[1]
            node_list.append(np.append(first_node, second_node))
        pass
for i in range(len(node_list)):
    G.add_edge(node_list[i][0], node_list[i][1])
print 'number of network nodes:', len(G.nodes())
print 'number of network edges:', len(G.edges())
nx.draw(G)
plt.show()  # 显示图形
