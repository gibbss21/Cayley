"""
"""

from Cayley.abstractnetwork import *
import csv

class Senate(AbstractNetwork):
    """Creates senate object. Requires a list of senators and their ideology
       scores."""

    def __init__(self, model, BP_constant, radius = 0.07, csv_file = 'senatedata.csv'):
        self.file = csv_file
        self.constant = BP_constant
        self.keys = list()
        if model.lower() in ['linear','limited','complete']:
            self.model = model.lower()
        else:
            raise ValueError("Model type unrecognized")
        if self.model == 'limited':
            self.radius = radius
        AbstractNetwork.__init__(self)
        self.autoCreate()

    def getType(self):
        """Just for quick fix in MonteCarlo."""
        return "Senate"

    def nodeNumber(self):
        return 100

    def autoCreate(self):
        rank_list = [0]*100
        med_list = list()
        with open(self.file) as file:
            readCSV = csv.reader(file, delimiter=',')
            for row in readCSV:
                if row[8] != 'name':
                    self.add(row[8], ideology = float(row[3]), rank = int(row[0]))
                    rank_list[int(row[0])-1] = row[8]
                    if int(row[0]) in [50,51]:
                        med_list.append(float(row[3]))
            self.center = 0.5*sum(med_list)

        ideals = self.getNodeFeature('ideology')
        if self.model == 'linear':
            for i in range(len(rank_list)-1):
                if i not in [0,len(rank_list)]:
                    self.multipleLinkCreator(rank_list[i],\
                                             [rank_list[i-1], rank_list[i+1]])
                elif i == 0:
                    self.linkCreator(rank_list[i],rank_list[i+1])
                elif i == len(rank_list)-1:
                    self.linkCreator(rank_list[i],rank_list[i-1])
        if self.model == 'limited':
            for item in self.getNodes():
                margin = (ideals[item]-self.radius, ideals[item]+self.radius)
##                if item == 'Franken' or item == 'Sanders':
##                    print(item)
##                    print(margin)
                neighbors = list()
                for i in self.getNodes():
                    if margin[0] <= ideals[i] <= margin[1] and i != item:
                        neighbors.append(i)
                self.multipleLinkCreator(item, neighbors)
##                if item == 'Franken' or item == 'Sanders':
##                    print(item)
##                    print(neighbors)
            neigh_d = self.getNodeFeature('neighbors')
            for item in self.getNodes():
                if len(neigh_d[item]) == 0:
                    raise ValueError("Radius too small for connected graph.")
        if self.model == 'complete':
            self.completeGraph()

        for senator in self:
<<<<<<< HEAD
<<<<<<< HEAD
            eta = ideals[senator]-self.center
            self.add(senator,beta=(1/(self.constant*(abs(eta)))+1),\
                        phi = (1/(self.constant*abs(eta))+1))
##            print(senator)
##            print("phi/Beta")
##            print(1/(self.constant*(abs(partisan)))+1)
=======
            partisan = ideals[senator]-self.center
            self.add(senator,beta=(1/(self.constant*(abs(partisan)+0.0001))+1),\
                        phi = (1/(self.constant*(abs(partisan)+0.0001))+1))
            print(senator)
            print("phi/Beta")
            print(1/(self.constant*(abs(partisan)+0.0001))+1)
>>>>>>> a200eb192d145f5a3baddd829288aea0508b99de
=======
            eta = ideals[senator]-self.center
            self.add(senator,beta=(1/(self.constant*(abs(eta)+0.01))+1),\
                        phi = (1/(self.constant*(abs(eta)+0.01))+1))
##            print(senator)
##            print("phi/Beta")
##            print(1/(self.constant*(abs(eta)))+1)
>>>>>>> 3d09111f9b0c42dc2bee612fb0760b3772f753ce
