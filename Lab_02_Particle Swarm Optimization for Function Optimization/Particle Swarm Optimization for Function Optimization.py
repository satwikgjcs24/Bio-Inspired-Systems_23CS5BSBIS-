
import random
import matplotlib.pyplot as plt

def fitness(p):
    return (p[0]-10)**2 + (p[1]-20)**2 + (p[2]-30)**2

def initialize(n):
    particles = []
    for i in range(n):
        pos = [random.uniform(0,50) for j in range(3)]
        vel = [random.uniform(-5,5) for j in range(3)]
        particles.append([pos,vel])
    return particles

def pso():
    n = int(input("Enter number of particles: "))
    mx = int(input("Enter number of iterations: "))

    w = 0.5
    c1 = 1.5
    c2 = 1.5

    particles = initialize(n)

    pbest = [p[0][:] for p in particles]
    gbest = min(pbest, key=fitness)[:]

    history = []

    for it in range(mx):
        for i in range(n):
            pos, vel = particles[i]

            if fitness(pos) < fitness(pbest[i]):
                pbest[i] = pos[:]

            if fitness(pbest[i]) < fitness(gbest):
                gbest = pbest[i][:]

            for j in range(3):
                r1 = random.random()
                r2 = random.random()

                vel[j] = (w * vel[j] +
                          c1 * r1 * (pbest[i][j] - pos[j]) +
                          c2 * r2 * (gbest[j] - pos[j]))

                pos[j] = pos[j] + vel[j]
                pos[j] = max(0, min(50, pos[j]))

        history.append(fitness(gbest))

        print("\nIteration:", it + 1)
        print("Global Best:", [round(x, 2) for x in gbest])
        print("Fitness:", round(fitness(gbest), 4))

    print("\nOPTIMAL HEALTHCARE RESOURCE ALLOCATION")
    print("Doctors:", round(gbest[0]))
    print("Nurses:", round(gbest[1]))
    print("Beds:", round(gbest[2]))
    print("Minimum Fitness:", round(fitness(gbest), 4))

    plt.plot(range(1, mx+1), history, marker='o')
    plt.xlabel("Iterations")
    plt.ylabel("Fitness")
    plt.title("PSO - Healthcare Resource Optimization")
    plt.grid()
    plt.show()

pso()
