import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1337)

n = 150

s1 = np.ndarray(shape=(n, 2))
s2 = np.ndarray(shape=(n, 4))

data = []  # ovde se nalaze podaci, u vidu liste tacaka sa (x,y) koordinatama

plt.figure()

for i in range(n):
    x1, y1 = np.random.normal(), np.random.normal()
    s1[i] = (x1, y1)

    r2, theta2 = np.random.normal(5, 0.25), np.random.uniform(0, 2*np.pi)
    x2, y2 = r2 * np.cos(theta2), r2 * np.sin(theta2)
    s2[i] = (x2, y2, r2, theta2)

    plt.scatter(x1, y1)
    plt.scatter(x2, y2)

    data.append((x1, y1))
    data.append((x2, y2))

plt.show()

# TODO 5: K-means nad ovim podacima

# TODO 7: DBSCAN nad ovim podacima
