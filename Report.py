import json
import pandas as pd

from Person import Person

class Report:
    @staticmethod
    def Relat_individual(population):
        for person in population:
            print('_________ Relatório individual dos cidadões _________')
            print('Nome: ', person.name)
            print('Sexo: ', person.gender)
            print('Personalidade', person.personality)
            print('Data Nascimento: ', person.birth_date)
            print('Idade: ', person.age)
            print('Estado civil: ', person.marital_status)
            print('Parceiro: ', person.partner)
            if person.status_life == 'Morte':
                print('Morreu no ano de ', person.death_date)
                print('Morreu com idade de ', person.age_death)
                print('Morreu causa da morte foi ' + person.cause_death)

    @staticmethod
    def Relat_history(population):
        for person in population:
            print('_________ Relatório individual dos cidadões _________')
            print(f'De CPF: {person.id}, nascido em {person.birth_date}, {person.name}  é uma pessoa do sexo {person.gender} Teve como caracteristicas da personalidade  {person.personality}')
            print(f' que durante sua vida se relacionou com {person.partner} de cpf {person.id_partner} , sendo então uma pessoa {person.marital_status}')
            if person.status_life == 'Morte':
                print(f'{person.name} morreu no ano de {person.death_date} aos {person.age_death} anos de idade de {person.cause_death}')
            else:
                print(f' Hoje {person.name} esta com {person.age} anos de idade.')
            print('_                _')
    @staticmethod
    def who_married(population):
        for person in population:
            if person.marital_status == 'Casado' or person.marital_status == 'Casada':
                print(f" Cpf: {person.id}  {person.name} com a personalidade  {person.personality} \n casou com {person.partner} de CPF {person.id_partner}" )
    @staticmethod
    def deadly_disease(population):
        illness = []
        larger = 0
        for person in population:
            if person.status_life == 'Morte':
                if person.cause_death not in illness:
                    illness.append( person.cause_death)
        for cause_death in illness:
            dead_people = 0
            cont = 0
            for person in population:
                if person.status_life == 'Morte':
                    dead_people += 1
                    if person.cause_death == cause_death:
                        cont += 1
            if cont > larger:
                deadly = cause_death
                larger = cont
            print(f'A Doença {cause_death} Matou {cont} vezes.')
        print(f'A doença que mais matou foi a {deadly} matou {larger} Vezes.')
        print(f'Total de mortes nessa simulação {dead_people}.')

    @staticmethod
    def Construindo_de_objeto_pra_json(population):
        lista_json = json.dumps(population, default=lambda x: x.__dict__)
        with open('simulation_report/simulation_population.json', 'a') as f:
            f.write(lista_json)
    def Construindo_de_json_para_objeto():
        population = []
        person = Person()
        i = 0
        with open("simulation_report/simulation_population.json", "r") as arquivo:
            lista = json.load(arquivo)
            for item in lista:
                person.name = item["name"]
                population.append(person)

        for person in population:
            print(person.name)















