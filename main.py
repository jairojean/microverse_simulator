from Person import Person
from Match import Match
from Time import Time
import Population_report
from Json_build import Json_build
from Graphic import Graphic

if __name__ == "__main__":
    start = False
    time = Time()
    time.start_year = 2000
    time.current_year = time.start_year
    time.end_world = 2100
    population = []
    person = Person()
    match = Match()
    id = 1
    #  Inicio ao Fim do mundo
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
    #population = Json_build.build_object_to_json()
    population = Json_build.build_json_to_object()

# Relatórios
    #Population_report.Relat_history(population)
    #Population_report.deadly_disease(population)
    #Population_report.who_married(population)
    #Population_report.Relat_individual(population)

# Gráficos
    #Graphic.Graphic_deadly_disease_bar(population)
    #Graphic.Graphic_Gender_pie(population)
    Graphic.Graphic_death_over_years(population,time.start_year,time.end_world)


