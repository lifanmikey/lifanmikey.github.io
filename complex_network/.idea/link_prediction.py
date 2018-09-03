# coding:utf-8

from math import log

import networkx as nx
from networkx.utils import not_implemented_for

import matplotlib.pyplot as plt

__all__ = ['resource_allocation_index']

def _apply_prediction(G, func, ebunch = None):
    """Applies the given function to each edge in the specified iterable
        of edges.
        `G` is an instance of :class:`networkx.Graph`.
        `func` is a function on two inputs, each of which is a node in the
        graph. The function can return anything, but it should return a
        value representing a prediction of the likelihood of a "link"
        joining the two nodes.
        `ebunch` is an iterable of pairs of nodes. If not specified, all
        non-edges in the graph `G` will be used.
    """
    if ebunch is None:
        ebunch = nx.non_edges(G)
    return ((u,v,func(u,v)) for u,v in ebunch)

@not_implemented_for('directed')
@not_implemented_for('multigraph')
def resource_alloction_index(G,ebunch =None):
    r"""Compute the resource allocation index of all node pairs in ebunch.
       Resource allocation index of `u` and `v` is defined as
       .. math::
           \sum_{w \in \Gamma(u) \cap \Gamma(v)} \frac{1}{|\Gamma(w)|}
       where $\Gamma(u)$ denotes the set of neighbors of $u$.
       Parameters
       ----------
       G : graph
           A NetworkX undirected graph.
       ebunch : iterable of node pairs, optional (default = None)
           Resource allocation index will be computed for each pair of
           nodes given in the iterable. The pairs must be given as
           2-tuples (u, v) where u and v are nodes in the graph. If ebunch
           is None then all non-existent edges in the graph will be used.
           Default value: None.
       Returns
       -------
       piter : iterator
           An iterator of 3-tuples in the form (u, v, p) where (u, v) is a
           pair of nodes and p is their resource allocation index.
       Examples
       --------
       >>> import networkx as nx
       >>> G = nx.complete_graph(5)
       >>> preds = nx.resource_allocation_index(G, [(0, 1), (2, 3)])
       >>> for u, v, p in preds:
       ...     '(%d, %d) -> %.8f' % (u, v, p)
       ...
       '(0, 1) -> 0.75000000'
       '(2, 3) -> 0.75000000'
       References
       ----------
       .. [1] T. Zhou, L. Lu, Y.-C. Zhang.
          Predicting missing links via local information.
          Eur. Phys. J. B 71 (2009) 623.
          https://arxiv.org/pdf/0901.0553.pdf
    """
    def predict(u,v):
        return sum(1 / G.degree(w) for w in nx.common_neighbors(G,u,v))
    return _apply_prediction(G, func, ebunch)

def regular_graph():
    pass

def caculate_AUC():
    test_set = []
    non_edges_set = []
    pass

if __name__ =='__main__':
    G = nx.complete_graph(5)
    G.remove_edge(0,1)
    nx.draw(G)
    plt.show()
    preds = nx.resource_allocation_index(G, [(0, 1), (2, 3)])
    for u, v, p in preds:
        print '(%d, %d) -> %.8f' % (u, v, p)