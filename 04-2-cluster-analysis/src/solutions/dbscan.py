"""
    @author:    SW 15/2013   Dragutin Marjanovic
    @email:     dmarjanovic94@gmail.com
"""

from __future__ import print_function
import numpy as np


class Cluster(object):

    def __init__(self):
        self.data = []  # podaci koji pripadaju ovom klasteru


class DBScan(object):

    def __init__(self, epsilon, min_points):
        """
        :param epsilon: za epsilon okolinu
        :param min_points: minimalan broj tacaka unutar epsilon okoline
        :return: None
        """
        self.epsilon = epsilon
        self.min_points = min_points
        self.data = None
        self.clusters = []

    def fit(self, data):
        # Prebacujem iz NumPy niza u listu
        arr = np.array(data)
        self.data = arr.tolist()
        
        # Oznacim sve tacke kao 'not_visited'
        for point in self.data:
            point.append('not_visited')
            
        # TODO 6: implementiran DBSCAN
        # kada algoritam zavrsi, u self.clusters treba da budu klasteri (tipa Cluster)

        cluster_index = -1
        for point in self.data:
            # Ako je tacka posjecenja
            if 'visited' == point[-1]:
                continue
            
            # Oznacimo je kao 'visited'
            point[-1] = 'visited'
            
            # Dobavimo 'komsije' te tacke
            neighbors = self.get_neighbors(point)
            
            if len(neighbors) < self.min_points:
                point[-1] = 'noise'
            else:
                self.clusters.append(Cluster())
                cluster_index += 1
                self.expand_cluster(point, neighbors, cluster_index)
        
    def expand_cluster(self, point, neighbors, cluster_no):
        # Dodamo tacku 'point' u klaster sa rednim brojem 'claster_no'
        self.clusters[cluster_no].data.append(point[:-1])
        
        # Za svaku tacku u skupu susjeda
        for pt in neighbors:
            # Ako nije oznacena - oznacimo je
            if 'visited' != pt[-1]:
                pt[-1] = 'visited'
                
                # Dobavimo njene komsije
                neighbors_pts = self.get_neighbors(pt)
                
                # Ako ima minimalan broj komsija
                if len(neighbors_pts) >= self.min_points:
                    # Spojimo liste
                    neighbors.extend(neighbors_pts)
            
            # Provjeravamo da li se tacka nalazi u nekom klasteru
            point_in_cluster = False        
            for c in self.clusters:
                for cluster_point in c.data:
                    if pt[:-1] == cluster_point:
                        point_in_cluster = True
                        break
                        
                if point_in_cluster:
                    break
            
            # Ako tacka nije ni u jednom klasteru dodamo je
            if not point_in_cluster:
                self.clusters[cluster_no].data.append(pt[:-1])

        
    # Metoda koja vraca tacke koje su u epsilon okolini tacke 'point'        
    def get_neighbors(self, point):
        points = []
        points.append(point)
        
        for pt in self.data:
            if self.euclidean_distance(pt[:-1], point[:-1]) < self.epsilon:
                points.append(pt)
                
        return points
            
    # Euklidsko rastojanje izmedju dvije tacke    
    def euclidean_distance(self, x, y):
        sq_sum = 0
        for xi, yi in zip(x, y):
            sq_sum += (yi - xi)**2
        
        # Vracamo sqrt(sq_sum)
        return sq_sum**0.5