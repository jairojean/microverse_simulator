from Person import Person
from Match import Match
from Time import Time
from Json_build import json_config
from Graphic import Graphic
from view.build_population_story import building_interface

if __name__ == "__main__":
    start = True
    time = Time()
    time.start_year = 2000
    time.current_year = time.start_year
    time.end_world = 2100
    population = []
    person = Person()
    match = Match()
    id = 1

# Inicio ao Fim do mundo
    if start == True:
        while time.current_year <= time.end_world:
            population = person.makes_birthday(population)
            population.append(person.born(time.current_year,id))
            population = person.creates_personality(population)
            population = match.looking_partner(population)
            population = person.dies(population, time.current_year)
            id += 1
            time.current_year += 1

# Manipulando Jsons
    if start == True:
        json_config.build_object_to_json(population)
    else:
        population = json_config.build_json_to_object()

# Gráficos
    Graphic.Graphic_deadly_disease_bar(population)
    Graphic.Graphic_Gender_pie(population)
    Graphic.Graphic_death_over_years(population,time.start_year,time.end_world)
    Graphic.Graphic_marital_status(population)
    Graphic.Graphic_status_life(population)

# Monta páginas HTML
    building_interface.build_table_interface(population)
    building_interface.building_story_interface(population)

