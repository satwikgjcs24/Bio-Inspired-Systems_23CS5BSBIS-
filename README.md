# Nature-Inspired Optimization Algorithms Using Python

A collection of **seven nature-inspired optimization algorithms** implemented using Python. This project demonstrates how biological behaviors and natural phenomena can be applied to solve optimization problems across healthcare, networking, machine learning, engineering, and renewable energy.

## 📌 Project Overview

This project implements the following seven optimization algorithms:

| No. | Algorithm | Application |
|---|---|---|
| 1 | Genetic Algorithm (GA) | General Function Optimization |
| 2 | Particle Swarm Optimization (PSO) | Healthcare Resource Optimization |
| 3 | Ant Colony Optimization (ACO) | Dynamic Routing |
| 4 | Gene Expression Algorithm (GEA) | Cancer Classification Simulation |
| 5 | Cuckoo Search (CS) | Antenna Parameter Optimization |
| 6 | Grey Wolf Optimizer (GWO) | Renewable Energy Resource Allocation |
| 7 | Parallel Cellular Algorithm (PCA) | Solar Panel Tracking Optimization |

---

## 🧬 1. Genetic Algorithm (GA)

**Application: Function Optimization**

Genetic Algorithm is inspired by natural selection and genetics. It evolves a population of potential solutions using selection, crossover, and mutation.

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

PSO is inspired by the collective behavior of birds flocking and fish schooling. It optimizes hospital resource allocation by finding suitable values for doctors, nurses, and beds.

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
- Perform selection, crossover, and mutation.
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

## 🐺 6. Grey Wolf Optimizer (GWO)

**Application: Renewable Energy Resource Allocation**

Grey Wolf Optimizer is inspired by the leadership hierarchy and hunting behavior of grey wolves. It uses three leading solutions called alpha, beta, and delta to guide the remaining search agents.

**Implementation:**
- Initialize a population of grey wolves.
- Evaluate the fitness of each wolf.
- Identify alpha, beta, and delta wolves.
- Calculate the coefficient `a` to control exploration and exploitation.
- Update wolf positions based on the three leading wolves.
- Repeat the process for the specified number of iterations.
- Identify the best solution.

**Objective:** Optimize the allocation of renewable energy resources by minimizing the difference between the obtained allocation and target requirements.

Example target allocation:
- Solar Energy: 40
- Wind Energy: 35
- Hydropower: 25

The objective function is based on the squared difference between the obtained and target allocations.

## ☀️ 7. Parallel Cellular Algorithm (PCA)

**Application: Solar Panel Tracking Optimization**

Parallel Cellular Algorithms are inspired by biological cells and cellular automata. Each cell represents a possible solution and interacts with its neighboring cells to improve the search process.

**Implementation:**
- Define a mathematical objective function.
- Initialize a two-dimensional grid of cells.
- Generate random solution positions for each cell.
- Evaluate the fitness of every cell.
- Identify neighboring cells.
- Select the best neighboring solution.
- Update cell states using neighborhood information and random variation.
- Repeat the process for a specified number of iterations.
- Track and display the best solution.

**Objective:** Minimize the solar panel tracking error by optimizing two tracking parameters.

Example objective function:

`f(x, y) = x² + y²`

Where:
- `x` represents horizontal tracking error.
- `y` represents vertical tracking error.

The goal is to find values closer to `(0, 0)` to minimize the tracking error.

*Note: This is an educational simulation of cellular neighborhood-based optimization. It demonstrates cellular optimization principles and does not represent a complete real-world solar tracking controller or a fully parallel hardware implementation.*

---

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
├── Grey_Wolf_Optimizer.py
├── Parallel_Cellular_Algorithm.py
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
pip install -r requirements.txt
```

Alternatively:

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

- Seven nature-inspired optimization algorithms.
- Application-based problem modelling.
- Interactive user input for algorithm parameters.
- Fitness evaluation and optimization.
- Population-based search techniques.
- Neighborhood-based cellular optimization.
- Visualization of convergence using graphs.
- Best solution tracking across iterations.
- Python implementations compatible with Jupyter Notebook and Google Colab.

## 🎯 Learning Outcomes

- Understand nature-inspired optimization techniques.
- Implement evolutionary and swarm intelligence algorithms.
- Understand selection, crossover, and mutation.
- Learn particle movement and pheromone updating.
- Understand Lévy flight-based exploration.
- Understand the leadership hierarchy of Grey Wolf Optimization.
- Learn neighborhood interactions in cellular optimization.
- Apply optimization techniques to different problem domains.
- Analyze optimization performance using graphical visualization.

## 📚 Research and References

The project is supported by research literature related to nature-inspired optimization techniques.

**Parallel Cellular Algorithm:**

Evsutin, O., Shelupanov, A., Meshcheryakov, R., Bondarenko, D., and Rashchupkina, A., "The Algorithm of Continuous Optimization Based on the Modified Cellular Automaton," *Symmetry*, vol. 8, no. 9, Art. no. 84, 2016.

- [Research Paper](https://doi.org/10.3390/sym8090084)
- [Download PDF](https://www.mdpi.com/2073-8994/8/9/84/pdf)

*Additional research papers for the other algorithms can be added as the literature survey is completed.*

## ⚠️ Disclaimer

The healthcare, cancer classification, routing, antenna, renewable energy, and solar tracking applications in this project are simplified educational models.

They demonstrate optimization concepts and are not intended to replace real-world clinical, transportation, electromagnetic simulation, energy management, or solar tracking systems.

## 👨‍💻 Contributors

Developed as an academic project to demonstrate the implementation and applications of nature-inspired optimization algorithms using Python.

---

⭐ If you find this project useful, consider giving the repository a star!
