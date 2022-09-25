from Person import Person
from Time import Time
from Relatorios import Relatorios

time = Time()
time.start_year = 1900
time.current_year = time.start_year
time.end_world = 2000
population = []
person = Person()

##  Inicio ao Fim do mundo
while time.current_year <= time.end_world:
    population.append(person.born(time.current_year,time.end_world))
    population = person.looking_partner(population)
    population = person.dies(population, time.end_world)
    population = person.makes_birthday(population)
    time.current_year += 1

Relatorios.Relat_historia(population)
