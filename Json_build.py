import json
from Person import Person
class json_config:
    @staticmethod
    def build_object_to_json(population):
        lista_json = json.dumps(population, default=lambda x: x.__dict__)
        with open('File_population/simulation_population.json', 'a') as f:
            f.write(lista_json)
            print("Chegou aqui")
    def build_json_to_object():
        population = []
        with open("File_population/simulation_population.json", "r") as arquivo:
            lista = json.load(arquivo)
            for item in lista:
                person = Person()
                person.id = item["id"]
                person.status_life = item["status_life"]
                person.name = item["name"]
                person.gender = item["gender"]
                person.birth_date = item["birth_date"]
                person.age = item["age"]
                person.age_death = item["age_death"]
                person.marital_status = item["marital_status"]
                person.death_date = item["death_date"]
                person.cause_death = item["cause_death"]
                person.id_partner = item["id_partner"]
                person.partner = item["partner"]
                person.personality = item["personality"]
                population.append(person)
        return population