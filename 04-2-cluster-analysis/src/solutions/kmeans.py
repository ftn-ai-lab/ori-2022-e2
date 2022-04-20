"""
    @author:    SW 15/2013   Dragutin Marjanovic
    @email:     dmarjanovic94@gmail.com
"""

from __future__ import print_function
import numpy, random, copy


class Cluster(object):

    def __init__(self, center):
        self.center = center
        self.data = []  # podaci koji pripadaju ovom klasteru

    def recalculate_center(self):
        # TODO 1: implementirano racunanje centra klastera
        # centar klastera se racuna kao prosecna vrednost svih podataka u klasteru
        new_center = [0 for i in range(len(self.center))]
        for datum in self.data:
            for i in range(len(datum)):
                new_center[i] += datum[i]
                
        n = len(self.data) 
        if n != 0:       
            self.center = [x/n for x in new_center]
                


class KMeans(object):

    def __init__(self, n_clusters, max_iter):
        """
        :param n_clusters: broj grupa (klastera)
        :param max_iter: maksimalan broj iteracija algoritma
        :return: None
        """
        self.data = None
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.clusters = []

    def fit(self, data, normalize = False):
        self.data = data  # lista N-dimenzionalnih podataka
        # TODO 4: normalizovati podatke pre primene k-means
        if normalize:
            self.data = self.normalize_data(self.data)

        # TODO 1: implementiran K-means algoritam za klasterizaciju podataka
        # kada algoritam zavrsi, u self.clusters treba da bude "n_clusters" klastera (tipa Cluster)
        
        # dimenzije prostora
        dimensions = len(self.data[0])
        # Napravimo n random tacaka i postavimo ih kao center klastera
        for i in range(self.n_clusters):
            point = [random.random() for x in range(dimensions)]
            self.clusters.append(Cluster(point))
        
        iter_no = 0
        not_moves = False
        while iter_no <= self.max_iter and (not not_moves):
            # Ispraznimo podatke koji pripadaju klasteru
            for cluster in self.clusters:
                cluster.data = []
                
            for datum in self.data:
                # Nadjemo indeks klastera kom pripada tacka
                cluster_index = self.predict(datum)
                # Dodamo tu tacku u taj klaster da bismo mogli izracunati centar
                self.clusters[cluster_index].data.append(datum)
                
            # Preracunamo centar
            not_moves = True
            for cluster in self.clusters:
                old_center = copy.deepcopy(cluster.center)
                cluster.recalculate_center()
            
                not_moves = not_moves and (cluster.center == old_center)
            
            print("Iter no: " + str(iter_no))    
            iter_no += 1

        # TODO (domaci): prosiriti K-means da stane ako se u iteraciji centri klastera nisu pomerili

    def predict(self, datum):
        # TODO 1: implementirano odredjivanje kom klasteru odredjeni podatak pripada
        # podatak pripada onom klasteru cijem je centru najblizi (po euklidskoj udaljenosti)
        # kao rezultat vratiti indeks klastera kojem pripada
        min_distance = None
        cluster_index = None
        for index in range(len(self.clusters)):
            distance = self.euclidean_distance(datum, self.clusters[index].center)
            if min_distance is None or distance < min_distance:
                cluster_index = index
                min_distance = distance
        
        return cluster_index
    
    # Euklidsko rastojanje izmedju dvije tacke    
    def euclidean_distance(self, x, y):
        sq_sum = 0
        for xi, yi in zip(x, y):
            sq_sum += (yi - xi)**2
        
        # vracamo sqrt(sq_sum)
        return sq_sum**0.5
        
    # Normalizovanje podataka
    def normalize_data(self, data):
        # Broj kolona
        cols = len(data[0])
        
        for col in range(cols):
            column_data = []
            for row in data:
                column_data.append(row[col])
            
            # Izracunamo srednju vrijednost za kolonu
            mean = numpy.mean(column_data)
            # Izracunamo standardnu devijaciju za kolonu
            std  = numpy.std(column_data)
            
            # Normalizujemo kolonu
            for row in data:
                row[col] = (row[col] - mean)/std
        
        # Vratimo normalizovane podatke        
        return data

    def sum_squared_error(self):
        # TODO 3: implementirano izracunavanje sume kvadratne greske
        # SSE (sum of squared error)
        # unutar svakog klastera sumirati kvadrate rastojanja izmedju podataka i centra klastera
        sse = 0
        for cluster in self.clusters:
            for datum in cluster.data:
                sse += self.euclidean_distance(cluster.center, datum)
        
        return sse**2
