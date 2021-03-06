"""
Authors: Justin Pusztay, Matt Lubas, Griffin Noe
Filename: cayleygraphics.py
Project: Research for Irina Mazilu, Ph.D.

Contains the class CayleyGraphics, which generates a graphic image of the
Cayley Tree. 

Code Adapted from: https://www.udacity.com/wiki/creating-network-graphs-with-python
"""

__author__ = "\n".join(['Justin Pusztay (pusztayj20@mail.wlu.edu)',
                        'Matt Lubas (lubasm18@mail.wlu.edu',
                        'Griffin Noe (noeg21@mail.wlu.edu'])

__all__ = ['CayleyGraphics']


import networkx as nx
import matplotlib.pyplot as plt
import Cayley as cy
from tkinter import *

class CayleyGraphics(object):

    def __init__(self,generations,links):
        """Creates a CayleyTree object in order to create an image
           of the graph."""
        self.tree = cy.CayleyTree(generations, links)
##        self.top = Tk()
##        self.top.mainloop()

    def drawCayley(self,labels=None, graph_layout='spring',
                   node_size=1000, node_color='blue', node_alpha=0.3,
                   node_text_size=12,
                   edge_color='blue', edge_alpha=0.3, edge_thickness=2,
                   edge_text_pos=0.3,
                   text_font='sans-serif'):
        """Method that physically draws the Cayley Tree graph based on generations
           and connections"""
        # create networkx graph
        graph=nx.Graph()

        #creates a Cayley-like tree with links and connections
        #graph =nx.balanced_tree(connections,generations)

        # add edges
        for edge in self.tree.linksAsTuples():
            graph.add_edge(edge[0], edge[1])

        # these are different layouts for the network you may try
        # shell seems to work best
        if graph_layout == 'spring':
            graph_pos=nx.spring_layout(graph)
        elif graph_layout == 'spectral':
            graph_pos=nx.spectral_layout(graph)
        elif graph_layout == 'random':
            graph_pos=nx.random_layout(graph)
        else:
            graph_pos=nx.shell_layout(graph)
            
        #Stop motion picture of state progression
        color_map = []
        for node in graph:
##            if node == 0:
##                color_map.append('red')
##            else:
            color_map.append('blue')
                
        # draw graph
        nx.draw_networkx_nodes(graph,graph_pos,node_size=node_size, 
                               alpha=node_alpha, node_color=color_map)
        nx.draw_networkx_edges(graph,graph_pos,width=edge_thickness,
                               alpha=edge_alpha,edge_color=edge_color)
        nx.draw_networkx_labels(graph, graph_pos,font_size=node_text_size,
                                font_family=text_font)

        if labels is None:
            labels = range(len(self.tree.linksAsTuples()))

        edge_labels = dict(zip(self.tree.linksAsTuples(), labels))
        """
        #Below on how to label edges.
        nx.draw_networkx_edge_labels(graph, graph_pos, edge_labels=edge_labels, 
                                     label_pos=edge_text_pos)
        """
        # show graph
        plt.show()
        #print(type(plt.gcf()))
        



    
