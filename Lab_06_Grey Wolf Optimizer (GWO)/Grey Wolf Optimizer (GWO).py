
import random
import matplotlib.pyplot as plt

# Objective function
def fitness(x):
    return (x[0]-40)**2 + (x[1]-35)**2 + (x[2]-25)**2

# Initialize wolves
def initialize(n):
    wolves = []
    for i in range(n):
        wolves.append([random.uniform(0, 100) for j in range(3)])
    return wolves

# Grey Wolf Optimizer
def gwo():
    n = int(input("Enter number of wolves: "))
    iterations = int(input("Enter number of iterations: "))

    wolves = initialize(n)

    alpha = [0, 0, 0]
    beta = [0, 0, 0]
    delta = [0, 0, 0]

    history = []

    for t in range(iterations):

        # Sort wolves based on fitness
        wolves.sort(key=fitness)

        alpha = wolves[0][:]
        beta = wolves[1][:]
        delta = wolves[2][:]

        a = 2 - 2 * t / iterations

        # Update wolf positions
        for i in range(n):
            for j in range(3):

                r1 = random.random()
                r2 = random.random()
                A1 = 2*a*r1 - a
                C1 = 2*r2
                D1 = abs(C1*alpha[j] - wolves[i][j])
                X1 = alpha[j] - A1*D1

                r1 = random.random()
                r2 = random.random()
                A2 = 2*a*r1 - a
                C2 = 2*r2
                D2 = abs(C2*beta[j] - wolves[i][j])
                X2 = beta[j] - A2*D2

                r1 = random.random()
                r2 = random.random()
                A3 = 2*a*r1 - a
                C3 = 2*r2
                D3 = abs(C3*delta[j] - wolves[i][j])
                X3 = delta[j] - A3*D3

                wolves[i][j] = (X1+X2+X3)/3

                wolves[i][j] = max(0, min(100, wolves[i][j]))

        # Find best solution
        best = min(wolves, key=fitness)

        history.append(fitness(best))

        print("\nIteration:", t+1)
        print("Alpha:", [round(x, 2) for x in alpha])
        print("Best Solution:", [round(x, 2) for x in best])
        print("Fitness:", round(fitness(best), 4))

    # Final result
    wolves.sort(key=fitness)
    best = wolves[0]

    print("\nOPTIMAL RENEWABLE ENERGY ALLOCATION")
    print("Solar Energy:", round(best[0], 2))
    print("Wind Energy:", round(best[1], 2))
    print("Hydropower:", round(best[2], 2))
    print("Minimum Fitness:", round(fitness(best), 6))

    # Convergence graph
    plt.plot(range(1, iterations+1), history, marker='o')
    plt.xlabel("Iterations")
    plt.ylabel("Best Fitness")
    plt.title("GWO - Renewable Energy Optimization")
    plt.grid()
    plt.show()

gwo()
