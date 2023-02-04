import random


def create_chromosome(n):

    return [random.randint(0, n-1) for _ in range(n)]

def fitness(chromosome):

    n = len(chromosome)
    # Check for queens attacking in the same row
    row_attacks = len(chromosome) - len(set(chromosome))
    # Check for queens attacking in the same diagonal
    diagonal_attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) == abs(chromosome[i]-chromosome[j]):
                diagonal_attacks += 1
    return n - (row_attacks + diagonal_attacks)

def crossover(chromosome1, chromosome2):

    n = len(chromosome1)
    # Choose a random crossover point
    crossover_point = random.randint(0, n-1)
    # Create two new chromosomes by swapping the tails of the input chromosomes
    chromosome1_new = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    chromosome2_new = chromosome2[:crossover_point] + chromosome1[crossover_point:]
    return chromosome1_new, chromosome2_new

def mutate(chromosome):

    n = len(chromosome)
    # Choose a random mutation point
    mutation_point = random.randint(0, n-1)
    # Create a new chromosome by changing the value at the mutation point
    chromosome_new = chromosome[:]
    chromosome_new[mutation_point] = random.randint(0, n-1)
    return chromosome_new

def generate_population(n, size):

    return [create_chromosome(n) for _ in range(size)]

def select_chromosome(population, fitness_scores):

    total_fitness = sum(fitness_scores)
    cumulative_fitness = [fitness_scores[0]]
    for i in range(1, len(fitness_scores)):
        cumulative_fitness.append(cumulative_fitness[-1] + fitness_scores[i])
    random_value = random.uniform(0, total_fitness)
    for i, cumulative_score in enumerate(cumulative_fitness):
        if random_value <= cumulative_score:
            return population[i]

def genetic_algorithm(n, size, generations):

    population = generate_population(n, size)
    for generation in range(generations):
     fitness_scores = [fitness(chromosome) for chromosome in population]
     if max(fitness_scores) == n:
      return population[fitness_scores.index(max(fitness_scores))]
new_population = []
for i in range(size):
 chromosome1 = select_chromosome(population, fitness_scores)
chromosome2 = select_chromosome(population, fitness_scores)
chromosome1, chromosome2 = crossover(chromosome1, chromosome2)
chromosome1 = mutate(chromosome1)
chromosome2 = mutate(chromosome2)
new_population.append(chromosome1)
if len(new_population) < size:
 new_population.append(chromosome2)
population = new_population
