from Person import Person
from Match import Match
from Time import Time
from Relatorios import Relatorios

time = Time()
time.start_year = 1900
time.current_year = time.start_year
time.end_world = 2000
population = []
person = Person()
match = Match()
id = 1
##  Inicio ao Fim do mundo
while time.current_year <= time.end_world:
    population.append(person.born(time.current_year,id))
    population = match.looking_partner(population)
    population = person.makes_birthday(population)
    population = person.creates_personality(population)
    population = person.dies(population, time.current_year)

    id += 1
    time.current_year += 1
Relatorios.Relat_historia(population)
##Relatorios.make_paths(population)
##Relatorios.Quem_casou(population)