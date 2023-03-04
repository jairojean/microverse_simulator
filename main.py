from Person import Person
from Match import Match
from Time import Time
from Report import Report
from Graphic import Graphic

if __name__ == "__main__":
    time = Time()
    time.start_year = 2000
    time.current_year = time.start_year
    time.end_world = 2100
    population = []
    person = Person()
    match = Match()
    id = 1

##  Inicio ao Fim do mundo
    while time.current_year <= time.end_world:
        population = person.makes_birthday(population)
        population.append(person.born(time.current_year,id))
        population = person.creates_personality(population)
        population = match.looking_partner(population)
        population = person.dies(population, time.current_year)
        id += 1
        time.current_year += 1


## Manipulando Jsons
    #Report.Construindo_de_objeto_pra_json(population)
    Report.Construindo_de_json_para_objeto()


## Relatórios
    #Report.Relat_history(population)
    ##Report.deadly_disease(population)
    ##Report.who_married(population)
    ##Report.Relat_individual(population)

## Gráficos
    ##Graphic.Graphic_Gender_pie(population)
    ##Graphic.Graphic_morte_ao_longo_anos(population,time.start_year,time.end_world)

