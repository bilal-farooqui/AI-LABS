import random

# Problem parameters
weights = [2, 3, 6, 7, 5, 9]  # Weights of items
values = [6, 5, 8, 9, 6, 7]  # Values of items
capacity = 15  # Max weight capacity of the knapsack
population_size = 10  # Number of chromosomes
generations = 50  # Number of iterations
mutation_rate = 0.1  # Probability of mutation

# Function to calculate fitness
def fitness(chromosome):
    total_weight = sum([weights[i] * chromosome[i] for i in range(len(chromosome))])
    total_value = sum([values[i] * chromosome[i] for i in range(len(chromosome))])
    if total_weight > capacity:
        return 0  # Invalid solution
    return total_value

# Generate initial population
def generate_population(size, length):
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(size)]

# Selection function (Tournament Selection)
def select(population):
    selected = random.sample(population, 2)
    return max(selected, key=fitness)

# Crossover function (Single-Point Crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation function
def mutate(chromosome):
    if random.random() < mutation_rate:
        index = random.randint(0, len(chromosome) - 1)
        chromosome[index] = 1 - chromosome[index]  # Flip the bit
    return chromosome

# Main Genetic Algorithm
def genetic_algorithm():
    population = generate_population(population_size, len(weights))
    for _ in range(generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select(population)
            parent2 = select(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        population = new_population
    # Return the best solution
    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)

# Run the Genetic Algorithm
solution, solution_fitness = genetic_algorithm()
print("Best solution:", solution)
print("Total value of selected items:", solution_fitness)
