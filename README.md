# Nature-Inspired Optimization Algorithms Using Python

A collection of five nature-inspired optimization algorithms implemented using Python. This project demonstrates how biological behaviors and natural phenomena can be applied to solve real-world optimization problems across healthcare, networking, machine learning and engineering.

## 📌 Project Overview

This project implements the following five optimization algorithms:

| No. | Algorithm | Application |
|---|---|---|
| 1 | Genetic Algorithm (GA) | General Function Optimization |
| 2 | Particle Swarm Optimization (PSO) | Healthcare Resource Optimization |
| 3 | Ant Colony Optimization (ACO) | Dynamic Routing |
| 4 | Gene Expression Algorithm (GEA) | Cancer Classification Simulation |
| 5 | Cuckoo Search (CS) | Antenna Parameter Optimization |

## 🧬 1. Genetic Algorithm (GA)

**Application: Function Optimization**

Genetic Algorithm is inspired by natural selection and genetics. It evolves a population of potential solutions using selection, crossover and mutation.

**Implementation:**
- Binary chromosome representation.
- Initial population generation.
- Fitness evaluation.
- Tournament selection.
- One-point crossover.
- Mutation.
- Best solution identification.

**Objective:** Find the maximum value of a mathematical function.

Example objective function:

`f(x) = x²`

## 🏥 2. Particle Swarm Optimization (PSO)

**Application: Healthcare Resource Optimization**

PSO is inspired by the collective behavior of birds flocking and fish schooling. It optimizes hospital resource allocation by finding suitable values for doctors, nurses and beds.

**Implementation:**
- Initialize particles with random positions and velocities.
- Calculate particle fitness.
- Update personal best (pbest).
- Update global best (gbest).
- Update velocity and position.
- Repeat until the maximum iterations are reached.

**Objective:** Minimize the difference between allocated resources and target requirements.

Example target:
- Doctors: 10
- Nurses: 20
- Beds: 30

## 🐜 3. Ant Colony Optimization (ACO)

**Application: Dynamic Routing**

ACO is inspired by the foraging behavior of ants. It uses pheromone trails and heuristic information to find shorter routes between locations.

**Implementation:**
- Define cities and their coordinates.
- Initialize pheromone trails.
- Construct routes using probabilistic selection.
- Calculate route distances.
- Apply pheromone evaporation.
- Update pheromone trails.
- Identify the shortest route.

**Objective:** Find the shortest possible route visiting all cities and returning to the starting city.

## 🧪 4. Gene Expression Algorithm (GEA)

**Application: Cancer Classification Simulation**

Gene Expression Algorithm uses genetic sequences to represent candidate solutions. These sequences are expressed into functional parameters and optimized through evolutionary operations.

**Implementation:**
- Generate simulated gene-expression data.
- Encode classification parameters as binary chromosomes.
- Evaluate classification accuracy.
- Perform selection, crossover and mutation.
- Express chromosomes into numerical weights and thresholds.
- Evaluate the best classification model.

**Objective:** Optimize a classification rule to distinguish simulated benign-like and malignant-like samples.

*Note: This is an educational simulation using synthetic data, not a clinically validated cancer detection system.*

## 📡 5. Cuckoo Search (CS)

**Application: Antenna Parameter Optimization**

Cuckoo Search is inspired by the brood parasitism behavior of cuckoo birds. It uses Lévy flights to explore the search space and identify better solutions.

**Implementation:**
- Initialize random nests.
- Evaluate fitness.
- Generate new solutions using Lévy flights.
- Replace existing nests when better solutions are found.
- Abandon poor nests.
- Update the best solution.
- Visualize convergence.

**Objective:** Find optimal antenna parameters by minimizing an assumed mathematical objective function.

Example parameters:
- Antenna length.
- Antenna width.
- Feed position.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Visualization:** Matplotlib
- **Randomization:** Python Random Module
- **Mathematical Computation:** Math Module
- **Environment:** Google Colab / Jupyter Notebook / VS Code

## 📂 Project Structure

```text
Nature-Inspired-Optimization/
│
├── Genetic_Algorithm.py
├── Particle_Swarm_Optimization.py
├── Ant_Colony_Optimization.py
├── Gene_Expression_Algorithm.py
├── Cuckoo_Search.py
│
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Nature-Inspired-Optimization.git
```

### 2. Navigate to the project directory

```bash
cd Nature-Inspired-Optimization
```

### 3. Install dependencies

```bash
pip install matplotlib
```

### 4. Run an algorithm

For example:

```bash
python Genetic_Algorithm.py
```

Similarly, execute the other Python files to run their respective optimization algorithms.

**Google Colab:** Upload the Python files or paste the code into separate notebook cells and execute them.

## 📊 Key Features

- Five nature-inspired optimization algorithms.
- Practical application-based problem modelling.
- Interactive user input for algorithm parameters.
- Fitness evaluation and optimization.
- Visualization of convergence using graphs.
- Best solution tracking across iterations.
- Python implementations compatible with Jupyter Notebook and Google Colab.

## 🎯 Learning Outcomes

- Understand nature-inspired optimization techniques.
- Implement evolutionary and swarm intelligence algorithms.
- Understand selection, crossover and mutation.
- Learn particle movement and pheromone updating.
- Understand Lévy flight-based exploration.
- Apply optimization techniques to different problem domains.
- Analyze optimization performance using graphical visualization.

## ⚠️ Disclaimer

The healthcare, cancer classification, routing and antenna applications in this project are simplified educational models. They demonstrate optimization concepts and are not intended to replace real-world clinical, transportation or electromagnetic simulation systems.

## 👨‍💻 Contributors

Developed as an academic project to demonstrate the implementation and applications of nature-inspired optimization algorithms using Python.

---

⭐ If you find this project useful, consider giving the repository a star!
