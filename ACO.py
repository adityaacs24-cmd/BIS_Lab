import random
import math

cities = [(0, 0), (2, 6), (5, 3), (8, 8), (6, 1)]
n = len(cities)

ants = 10
iterations = 100
alpha = 1
beta = 2
rho = 0.5
Q = 100

def dist(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

pheromone = [[1.0] * n for _ in range(n)]
best_route = []
best_length = float("inf")

for _ in range(iterations):
    routes = []

    for _ in range(ants):
        start = random.randrange(n)
        route = [start]
        unvisited = list(range(n))
        unvisited.remove(start)

        while unvisited:
            current = route[-1]
            weights = [
                pheromone[current][j] ** alpha
                * (1 / dist(current, j)) ** beta
                for j in unvisited
            ]

            next_city = random.choices(
                unvisited, weights=weights, k=1
            )[0]

            route.append(next_city)
            unvisited.remove(next_city)

        route.append(start)

        length = sum(
            dist(route[i], route[i + 1])
            for i in range(n)
        )

        routes.append((route, length))

        if length < best_length:
            best_length = length
            best_route = route.copy()

    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - rho)

    for route, length in routes:
        for i in range(n):
            a, b = route[i], route[i + 1]
            pheromone[a][b] += Q / length
            pheromone[b][a] += Q / length

print("Best route:", best_route)
print("Shortest distance:", round(best_length, 2))
