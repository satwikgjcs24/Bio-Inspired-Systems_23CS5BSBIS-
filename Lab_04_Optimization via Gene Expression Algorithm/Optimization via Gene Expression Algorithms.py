
import random
import matplotlib.pyplot as plt

GENES = 4
BITS = 8
POP_SIZE = 20
MUTATION_RATE = 0.02
CROSSOVER_RATE = 0.8

# Generate simulated gene expression dataset
def create_data():
    data = []

    for i in range(100):
        x = [max(0, min(1, random.gauss(0.3, 0.15))) for j in range(3)]
        data.append((x, 0))

    for i in range(100):
        x = [max(0, min(1, random.gauss(0.7, 0.15))) for j in range(3)]
        data.append((x, 1))

    random.shuffle(data)
    return data

# Decode chromosome into weights and threshold
def express(ch):
    genes = [int(ch[i:i+BITS], 2) for i in range(0, GENES*BITS, BITS)]

    weights = [g / 255 * 2 for g in genes[:3]]
    threshold = genes[3] / 255 * 6

    return weights, threshold

# Calculate classification accuracy
def fitness(ch, data):
    weights, threshold = express(ch)
    correct = 0

    for x, label in data:
        score = sum(weights[i] * x[i] for i in range(3))
        prediction = 1 if score >= threshold else 0

        if prediction == label:
            correct += 1

    return correct / len(data)

# Initialize population
def initialize():
    return [
        ''.join(random.choice('01') for j in range(GENES*BITS))
        for i in range(POP_SIZE)
    ]

# Tournament selection
def select(pop, data):
    a, b = random.sample(pop, 2)
    return max([a, b], key=lambda x: fitness(x, data))

# One-point crossover
def crossover(p1, p2):
    point = random.randint(1, len(p1)-1)

    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]

    return c1, c2

# Mutation
def mutate(ch):
    bits = list(ch)

    for i in range(len(bits)):
        if random.random() < MUTATION_RATE:
            bits[i] = '1' if bits[i] == '0' else '0'

    return ''.join(bits)

# Gene Expression Algorithm
def gea():
    generations = int(input("Enter number of generations: "))

    data = create_data()
    train = data[:160]
    test = data[160:]

    pop = initialize()
    best = max(pop, key=lambda x: fitness(x, train))

    history = []

    for gen in range(generations):
        new_pop = [best]

        while len(new_pop) < POP_SIZE:
            p1 = select(pop, train)
            p2 = select(pop, train)

            if random.random() < CROSSOVER_RATE:
                c1, c2 = crossover(p1, p2)
            else:
                c1, c2 = p1, p2

            c1 = mutate(c1)
            c2 = mutate(c2)

            new_pop.append(c1)

            if len(new_pop) < POP_SIZE:
                new_pop.append(c2)

        pop = new_pop

        current = max(pop, key=lambda x: fitness(x, train))

        if fitness(current, train) > fitness(best, train):
            best = current

        acc = fitness(best, train)
        history.append(acc)

        print("\nGeneration:", gen+1)
        print("Best Chromosome:", best)
        print("Training Accuracy:", round(acc*100, 2), "%")

    weights, threshold = express(best)

    print("\nFINAL CLASSIFICATION MODEL")
    print("Best Chromosome:", best)
    print("Gene Weights:", [round(w, 3) for w in weights])
    print("Threshold:", round(threshold, 3))
    print("Training Accuracy:", round(fitness(best, train)*100, 2), "%")
    print("Testing Accuracy:", round(fitness(best, test)*100, 2), "%")

    # Test a new simulated sample
    sample = [0.65, 0.72, 0.68]

    score = sum(weights[i] * sample[i] for i in range(3))

    result = "Malignant-like" if score >= threshold else "Benign-like"

    print("\nSAMPLE CLASSIFICATION")
    print("Expression Values:", sample)
    print("Predicted Class:", result)

    plt.plot(range(1, generations+1), history, marker='o')
    plt.xlabel("Generations")
    plt.ylabel("Training Accuracy")
    plt.title("GEA - Classification Optimization")
    plt.grid()
    plt.show()

gea()
