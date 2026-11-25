
import random
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

BITS = 5
POPULATION_SIZE = 10
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1

def fitness(ch):
    return int(ch, 2) ** 2

def create_population():
    return [format(random.randint(0, 31), "05b") for i in range(POPULATION_SIZE)]

def select_parent(pop):
    a, b = random.sample(pop, 2)
    return max(a, b, key=fitness)

def crossover(p1, p2):
    point = random.randint(1, BITS - 1)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return point, c1, c2

def mutate(ch):
    bits = list(ch)
    for i in range(BITS):
        if random.random() < MUTATION_RATE:
            bits[i] = "1" if bits[i] == "0" else "0"
    return "".join(bits)

def run_ga():
    generations = int(input("Enter generations: "))
    pop = create_population()
    best = max(pop, key=fitness)

    for gen in range(generations):
        new_pop = []
        last = None

        while len(new_pop) < POPULATION_SIZE:
            p1 = select_parent(pop)
            p2 = select_parent(pop)

            if random.random() < CROSSOVER_RATE:
                point, c1, c2 = crossover(p1, p2)
                last = (p1, p2, point, c1, c2)
            else:
                c1, c2 = p1, p2

            c1 = mutate(c1)
            c2 = mutate(c2)

            new_pop.append(c1)
            if len(new_pop) < POPULATION_SIZE:
                new_pop.append(c2)

        pop = new_pop

        current = max(pop, key=fitness)
        if fitness(current) > fitness(best):
            best = current

        clear_output(wait=True)

        print("GENERATION:", gen + 1)
        print("Best Chromosome:", best)
        print("Best Value:", int(best, 2))
        print("Best Fitness:", fitness(best))

        if last:
            p1, p2, point, c1, c2 = last

            print("\nONE POINT CROSSOVER")
            print("Parent 1:", p1[:point] + "|" + p1[point:])
            print("Parent 2:", p2[:point] + "|" + p2[point:])
            print("Child 1: ", c1[:point] + "|" + c1[point:])
            print("Child 2: ", c2[:point] + "|" + c2[point:])

        print("\nCURRENT POPULATION")

        for ch in sorted(pop, key=fitness, reverse=True):
            print(ch, " Value:", int(ch, 2), " Fitness:", fitness(ch))

        plt.figure(figsize=(8, 3))
        plt.bar(range(1, len(pop) + 1), [fitness(ch) for ch in pop])
        plt.xlabel("Individual")
        plt.ylabel("Fitness")
        plt.title("Population Fitness")
        plt.show()

    print("\nFINAL BEST SOLUTION")
    print("Chromosome:", best)
    print("Value:", int(best, 2))
    print("Maximum Fitness:", fitness(best))

run_ga()
