"""
This program will simulate a population of gophers over a ten-year
 period and display each year's births, deaths and population size.
Initial population 1000. Every year, a random number of gophers is born,
between 10% of the current population, and 20%.
 Each year, a random number of gophers die, between 5% and 25%
"""
import random

BIRTH_RATE_MIN = .10
BIRTH_RATE_MAX = .20
DEATH_RATE_MIX = .05
DEATH_RATE_MAX = .25
NUMBER_YEARS = 10
INITIAL_POPULATION = 1000


def main():
    print('Welcome to the Gopher Population Simulator!')
    print('Starting population:', INITIAL_POPULATION)

    population = INITIAL_POPULATION
    for year in range(NUMBER_YEARS):
        birth_rate = random.uniform(BIRTH_RATE_MIN, BIRTH_RATE_MAX)
        death_rate = random.uniform(DEATH_RATE_MIX, DEATH_RATE_MAX)
        births = int(population * birth_rate)
        deaths = int(population * death_rate)
        population = population + births - deaths

        print('{} gophers were born.  {} died.'.format(births, deaths))
        print('Population: {}'.format(population))
        print('Year {}\n'.format(year + 1))


main()
