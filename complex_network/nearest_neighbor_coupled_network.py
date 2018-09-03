# coding:utf-8

from numpy import *
import matplotlib.pyplot as plt
import networkx as nx
import link_prediction

def nearest_neighbor_coupled_network(N = 10, K = 6):
     G = nx.Graph()
     if (K > N-1) or (K % 2 == 1):
          print 'error: K must no larger than N-1 and be even'
          return
     for i in range(N):
         for j in range(i + 1, i + K / 2):
             jj = j
             if jj >= N:
                 jj %= N
             G.add_edge(i, jj)
     return G

def delete_link(G, k, p =0.6):
    # print '--------开始删除一定数量的链路--------'
    # 测试链路集
    test_set = []
    # 不存在链路集
    non_edges_set = []
    N = len(G.edges())
    non_edges_set = set(nx.non_edges(G))
    # print 'non_edges_set的链路数量:', len(non_edges_set)

    # 删除（k+1）条链路
    while True:
        # i = random.randint(0,N)
        # j = random.randint(0,N)
        # if i!=j and G.has_edge(i,j):
        #     test_set.append((i,j))
        #     G.remove_edge(i,j)

        for i, j in set(G.edges()):
            f = random.random()
            if f > p:
                test_set.append((i, j))
                G.remove_edge(i, j)
            if len(test_set) >= math.floor(k * N):
                break
        if len(set(test_set)) >= math.floor(k * N):
            break

    print 'test_set的链路数量:', len(test_set)
    print '删边后网络存在的链路数量:', len(G.edges())

    # # 判断删边是否正确
    # if len(test_set) + len(G.edges()) == N:
    #     pass
    # else:
    #     # print "删边出现错误！！！！！！！"
    #     exit(0)

    # print '------结束删除链路------'
    # print ''
    return set(test_set), set(non_edges_set)





if __name__ =='__main__':

    # # G = nearest_neighbor_coupled_network()
    # G = nx.random_graphs.random_regular_graph(4, 10)
    # # test, missing_edges = delete_link(G, k=0.1, p=0.5)
    # plt.figure(1)
    # pos = nx.circular_layout(G)
    # nx.draw_networkx(G, pos, with_labels=True)
    # plt.show()
#-------------------------------------------------------------
    # k = ['4', '8', '12', '16', '20', '24', '28', '32']

   link_prediction.Link_Precision(link_prediction.Jazz_network())
