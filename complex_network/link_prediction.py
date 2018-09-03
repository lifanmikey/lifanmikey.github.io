# coding:utf-8

import networkx as nx
from networkx.utils import not_implemented_for
import matplotlib.pyplot as plt
from math import log
from operator import itemgetter, attrgetter
import random
import xlwt
import numpy as np
import re
import math
import csv

# 构造最近邻耦合网络---规则网络
def NNC_network(N = 10, K = 8):
    '''规则网络总的节点数N,邻居数K---最近邻耦合网络'''
    G = nx.Graph()
    if (K > N - 1) or (K % 2 == 1):
        print 'error: K must no larger than N-1 and be even'
        return
    for i in range(N):
        for j in range(i + 1, i + K / 2):
            jj = j
            if jj >= N:
                jj %= N
            G.add_edge(i, jj)
    return G

# 构造Jazz网络
# 198个节点 2742条边
def Jazz_network():
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
    # print len(G.nodes()), len(G.edges)
    return G

# 删除部分连边
def delete_link(G, k=0.1, p=0.5):
    # 测试链路集合---删除部分已存在的连边
    test_set = []
    # 缺失链路集合
    missing_edges_set = []
    N = len(G.edges())
    missing_edges_set = set(nx.non_edges(G))

    while True:
        for i, j in set(G.edges()):
            f = random.random()
            if f > p:
                test_set.append((i, j))
                G.remove_edge(i, j)
            if len(test_set) >= math.floor(k * N):
                break
        if len(set(test_set)) >= math.floor(k * N):
            break
    return set(test_set), set(missing_edges_set)

# AUC指标
def AUC_Indx(pred, test_set, non_edges_set):
    test_pre = []  # 测试集预测分集
    missing_edges_pre = []  # 缺失链路预测分集

    n = 0  # AUC公式中的n'
    m = 0  # AUC公式中的n"

    for u, v, p in pred:
        if (u, v) in test_set or (v, u) in test_set:
            test_pre.append(p)
        else:
            missing_edges_pre.append(p)

    if len(test_set) == len(test_pre) and len(non_edges_set) == len(missing_edges_pre) and len(test_set) != 0:
        pass
    else:
        print "计算失败！！！！！！"
        exit(0)

    for i in range(len(test_pre)):
        for j in range(len(missing_edges_pre)):
            #  大于+1
            if test_pre[i] > missing_edges_pre[j]:
                n += 1.0

            # 等于+0.5
            if test_pre[i] == missing_edges_pre[j]:
                m += 0.5

    return (n + m)/(len(test_set)*len(non_edges_set))

# 准确度指标
def Precision_Index(pred, test_set):
    L = 0
    # 从预测分列表中选出分数最高的M条链路，其中有L条链路属于测试集，则precision = L/M
    for u, v, p in pred[0:len(test_set)]:
        if (u, v) in test_set or (v, u) in test_set:
            L += 1.0
    return L/len(test_set)

# 保存结果
def save_data(filename, result):
    f = open(filename, 'w')
    writer = csv.writer(f)
    for record in result:
        writer.writerow(record)
    f.close()

def Link_Precision(Graph):
    """Step1------构造网络"""
    G = Graph

    # plt.figure(1)
    # plt.subplot(211)
    # pos = nx.circular_layout(G)
    # nx.draw_networkx(G, pos, with_labels=True)

    # 对构造的网络删除部分连边
    test_set, non_edges_set = delete_link(G)

    # plt.subplot(212)
    # pos = nx.circular_layout(G)
    # nx.draw_networkx(G, pos, with_labels=True)
    # plt.show()

    """Step2------对网络缺失边预测得分值"""
    # preds = nx.adamic_adar_index(G)
    # preds = nx.common_neighbors(G)
    # preds = nx.jaccard_coefficient(G)
    preds = nx.resource_allocation_index(G)
    preds = sorted(preds, key=itemgetter(2), reverse=True)  # 根据连边的预测得分值降序排序

    """Step3------AUC，Precision指标的计算"""
    auc_result = AUC_Indx(preds, test_set, non_edges_set)
    precision_result = Precision_Index(preds, test_set)

    """输出结果"""
    print "AUC:", auc_result, "Precision:", precision_result
    return auc_result, precision_result

def resultPlot(result):
    # 可视化
    k = [example[2] for example in result]
    x = range(len(k))
    y1 = [example[0] for example in result]
    y2 = [example[1] for example in result]

    plt.figure()
    plt.clf()
    plt.plot(x, y1, marker='o', label='AUC', color='red', linewidth=2)
    plt.plot(x, y2, marker='*', label="precision", color="blue", linewidth=2)
    plt.xlabel("K")
    plt.title("NNC_result")
    plt.xticks(x, k, rotation=45)
    plt.legend()
    plt.savefig(r'E:\Users\Michael\PycharmProjects\complex_network\result/result_NNC.jpg')
    plt.show()

if __name__ =='__main__':
    # k1 = np.arange(0.1, 0.9, 0.1)
    # # 折线图显示最后的结果
    # plt.figure(1)
    # plt.axis([0, 1, 0, 1])
    # # plt.xlabel('k')
    # # plt.text()
    # plt.plot(k1, AUC_average_list, 'ko',k1, AUC_average_list, 'k', k1, Precision_average_list, 'r--',k1, Precision_average_list, 'ro')
    # plt.savefig('Result_1000.jpg')
    # plt.show()

    # --------------------------------------------------------------------------------------------------------------
    result = list()
    for k in range(6, 804, 4):
        AUC_sum = 0;Precision_sum = 0
        for i in range(10):
            auc_result, precision_result = Link_Precision(NNC_network(1000, k))
            AUC_sum += auc_result; Precision_sum += precision_result
        auc = AUC_sum / 10; precision = Precision_sum / 10
        result.append(np.array([auc, precision, k-2]))
    filename = 'result_NNC'
    save_data(r'E:\Users\Michael\PycharmProjects\complex_network\result/%s.csv' % filename, result)
    resultPlot(result)