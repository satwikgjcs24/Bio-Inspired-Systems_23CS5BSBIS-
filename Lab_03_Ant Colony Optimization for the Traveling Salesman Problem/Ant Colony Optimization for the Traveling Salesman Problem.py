
import random
import math
import matplotlib.pyplot as plt

cities = {
    0: (2, 3),
    1: (5, 4),
    2: (8, 2),
    3: (7, 7),
    4: (3, 8),
    5: (1, 6)
}

n = len(cities)

def distance(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

dist = [[distance(i,j) for j in range(n)] for i in range(n)]

def select_city(current, unvisited, pheromone, alpha, beta):
    probabilities = []

    for city in unvisited:
        p = (pheromone[current][city] ** alpha)
        h = (1 / dist[current][city]) ** beta
        probabilities.append(p * h)

    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]

    return random.choices(unvisited, weights=probabilities)[0]

def calculate_route(route):
    total = 0

    for i in range(len(route)-1):
        total += dist[route[i]][route[i+1]]

    total += dist[route[-1]][route[0]]
    return total

def aco():
    ants = 10
    iterations = 50
    alpha = 1
    beta = 2
    rho = 0.5
    Q = 100

    pheromone = [[1 for j in range(n)] for i in range(n)]

    best_route = None
    best_distance = float('inf')
    history = []

    for it in range(iterations):
        routes = []

        for ant in range(ants):
            start = random.randint(0, n-1)
            route = [start]
            unvisited = list(range(n))
            unvisited.remove(start)

            while unvisited:
                current = route[-1]

                next_city = select_city(
                    current, unvisited, pheromone, alpha, beta
                )

                route.append(next_city)
                unvisited.remove(next_city)

            routes.append(route)

            d = calculate_route(route)

            if d < best_distance:
                best_distance = d
                best_route = route[:]

        # Pheromone evaporation
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1-rho)

        # Pheromone update
        for route in routes:
            d = calculate_route(route)
            deposit = Q / d

            for i in range(n):
                a = route[i]
                b = route[(i+1) % n]

                pheromone[a][b] += deposit
                pheromone[b][a] += deposit

        history.append(best_distance)

        print("\nIteration:", it+1)
        print("Best Route:", best_route + [best_route[0]])
        print("Distance:", round(best_distance, 2))

    print("\nFINAL BEST ROUTE")
    print("Route:", best_route + [best_route[0]])
    print("Shortest Distance:", round(best_distance, 2))

    # Route visualization
    x = [cities[i][0] for i in best_route + [best_route[0]]]
    y = [cities[i][1] for i in best_route + [best_route[0]]]

    plt.figure(figsize=(7,5))
    plt.plot(x, y, marker='o')

    for i in cities:
        plt.text(cities[i][0], cities[i][1], str(i))

    plt.title("ACO - Dynamic Routing")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid()
    plt.show()

    # Convergence graph
    plt.figure(figsize=(7,4))
    plt.plot(history, marker='o')
    plt.title("ACO Convergence")
    plt.xlabel("Iterations")
    plt.ylabel("Best Distance")
    plt.grid()
    plt.show()

aco()
