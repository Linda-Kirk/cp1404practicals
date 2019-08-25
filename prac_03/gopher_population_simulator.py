"""
This program will simulate a population of gophers over a ten-year
 period and display each year's population size.
Initial population 1000. Every year, a random number of gophers is born,
between 10% of the current population, and 20%.
 Each year, a random number of gophers die, between 5% and 25%
"""
import random

BIRTH_RATE_MIN = .10
BIRTH_RATE_MAX = .20
DEATH_RATE_MIX = .05
DEATH_RATE_MAX = .25


def main():
    initial_population = 1000
    birth_rate = round(random.uniform(BIRTH_RATE_MIN, BIRTH_RATE_MAX), 2)
    death_rate = round(random.uniform(DEATH_RATE_MIX, DEATH_RATE_MAX), 2)
    print(death_rate)
    print(birth_rate)

    # births = initial_population



main()
