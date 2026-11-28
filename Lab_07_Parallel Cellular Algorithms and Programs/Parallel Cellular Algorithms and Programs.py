
import random
import math
import matplotlib.pyplot as plt

def fitness(x):
    return x[0]**2 + x[1]**2

def initialize(n):
    cells = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append([random.uniform(-10, 10), random.uniform(-10, 10)])
        cells.append(row)
    return cells

def pca():
    n = int(input("Enter grid size: "))
    iterations = int(input("Enter number of iterations: "))

    cells = initialize(n)
    best = [0, 0]
    best_fit = float('inf')
    history = []

    for t in range(iterations):
        old = [[cell[:] for cell in row] for row in cells]
        new = [[cell[:] for cell in row] for row in cells]

        for i in range(n):
            for j in range(n):
                neighbors = []

                for a in range(max(0, i-1), min(n, i+2)):
                    for b in range(max(0, j-1), min(n, j+2)):
                        neighbors.append(old[a][b])

                local_best = min(neighbors, key=fitness)

                x = old[i][j]
                r = random.random()
                mutation = random.uniform(-1, 1) * (1 - t / iterations)

                new[i][j] = [
                    x[0] + r * (local_best[0] - x[0]) + mutation,
                    x[1] + r * (local_best[1] - x[1]) + mutation
                ]

                new[i][j][0] = max(-10, min(10, new[i][j][0]))
                new[i][j][1] = max(-10, min(10, new[i][j][1]))

        cells = new

        for row in cells:
            for cell in row:
                f = fitness(cell)

                if f < best_fit:
                    best_fit = f
                    best = cell[:]

        history.append(best_fit)

        print("Iteration:", t+1, "Best:", best, "Fitness:", best_fit)

    print("\nBest Tracking Parameters:", best)
    print("Minimum Tracking Error:", best_fit)

    plt.plot(history)
    plt.xlabel("Iterations")
    plt.ylabel("Best Fitness")
    plt.title("Parallel Cellular Algorithm")
    plt.grid()
    plt.show()

pca()
