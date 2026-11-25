
import random
import math
import matplotlib.pyplot as plt

# Antenna target design
target = [5, 3, 2]

def fitness(x):
    return sum((x[i] - target[i])**2 for i in range(3))

# Generate random nests
def initialize(n):
    return [[random.uniform(0, 10) for j in range(3)] for i in range(n)]

# Generate Levy flight
def levy():
    beta = 1.5
    sigma = (
        math.gamma(1+beta) * math.sin(math.pi*beta/2) /
        (math.gamma((1+beta)/2) * beta * 2**((beta-1)/2))
    ) ** (1/beta)

    u = random.gauss(0, sigma)
    v = random.gauss(0, 1)

    return u / (abs(v)**(1/beta))

# Cuckoo Search Algorithm
def cuckoo_search():
    n = int(input("Enter number of nests: "))
    iterations = int(input("Enter number of iterations: "))

    pa = 0.25
    alpha = 0.01

    nests = initialize(n)

    best = min(nests, key=fitness)[:]
    history = []

    for it in range(iterations):

        # Generate new solutions using Levy flight
        for i in range(n):
            new = []

            for j in range(3):
                step = levy()
                value = nests[i][j] + alpha * step * (nests[i][j] - best[j])
                value = max(0, min(10, value))
                new.append(value)

            # Replace nest if new solution is better
            k = random.randint(0, n-1)

            if fitness(new) < fitness(nests[k]):
                nests[k] = new

        # Abandon worst nests
        nests.sort(key=fitness)

        abandon = max(1, int(pa*n))

        for i in range(n-abandon, n):
            nests[i] = [random.uniform(0, 10) for j in range(3)]

        # Update best solution
        current = min(nests, key=fitness)

        if fitness(current) < fitness(best):
            best = current[:]

        history.append(fitness(best))

        print("\nIteration:", it+1)
        print("Best Antenna Parameters:", [round(x, 4) for x in best])
        print("Fitness:", round(fitness(best), 6))

    print("\nOPTIMAL ANTENNA DESIGN")
    print("Length:", round(best[0], 4))
    print("Width:", round(best[1], 4))
    print("Feed Position:", round(best[2], 4))
    print("Minimum Fitness:", round(fitness(best), 6))

    # Convergence graph
    plt.plot(range(1, iterations+1), history, marker='o')
    plt.xlabel("Iterations")
    plt.ylabel("Best Fitness")
    plt.title("Cuckoo Search - Antenna Optimization")
    plt.grid()
    plt.show()

cuckoo_search()
