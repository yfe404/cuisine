# Encode solution space
## Chromosome: contains the quantity of each ingredient
## Allele: one ingredient quantity per allele


# Set algorithm parameters


# Create initial population
def generate_initial_population(population_size, individual_size):
    pass

# Measure fitness of individuals
def fitness(individual, *args, **kwargs):
    pass

# Select parents
def set_probabilities_of_population(population):
    probability_of_selection = [0 for _ in range(len(population))]
    all_fitnesses = [fitness(x) for x in population]
    total_fitness = sum(all_fitnesses)

    for idx, individual in enumerate(population):
        probability_of_selection[idx] = all_fitnesses[idx] / total_fitness
    

def roulette_wheel_selection(population, number_of_selections):
    possible_probabilities = set_probabilities_of_population(population)
    slices = []
    total = 0
    for i in range(number_of_selections):
        slices.append(i)


# Reproduce offspring


# Population next generation


# Measure fitness of individuals

