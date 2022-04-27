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
        self.data = data
        # TODO 6: implementirati DBSCAN
        # kada algoritam zavrsi, u self.clusters treba da budu klasteri (tipa Cluster)
        raise NotImplementedError()
