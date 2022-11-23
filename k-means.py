import random
import numpy as np
import matplotlib.pyplot as plt

k = 3
rnd = 0
ROUND_LIMIT = 10
THRESHOLD = 1e-10
melons = []
clusters = []

f = open(r'C:\Users\86152\Desktop\wine\melons.txt')
for line in f:
    melons.append(np.array(line.split(' '), dtype = np.string_).astype(np.float64))

mean_vectors = random.sample(melons, k)

while True:
    rnd += 1
    change = 0
    clusters = []
    for i in range(k):
        clusters.append([])
    for melon in melons:
        c = np.argmin(
            list(map( lambda vec: np.linalg.norm(melon - vec, ord = 2), mean_vectors))
        )

        clusters[c].append(melon)

    for i in range(k):

        new_vector = np.zeros((1,2))
        for melon in clusters[i]:
            new_vector += melon
        new_vector /= len(clusters[i])

        change += np.linalg.norm(mean_vectors[i] - new_vector, ord = 2)
        mean_vectors[i] = new_vector

    if rnd > ROUND_LIMIT or change < THRESHOLD:
        break

print('最终迭代%d轮'%rnd)

colors = ['red', 'green', 'blue']

for i, col in zip(range(k), colors):
    for melon in clusters[i]:
        plt.scatter(melon[0], melon[1], color = col)

plt.show()
