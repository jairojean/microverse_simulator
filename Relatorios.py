class Relatorios:
    def Relat_individual(populacao):
        for person in populacao:
            print('_________ Relatório individual dos cidadões _________')
            print('Nome: ', person.name)
            print('Sexo: ', person.sex)
            print('Personalidade', person.personality)
            print('Data Nascimento: ', person.birth_date)
            print('Idade: ', person.age)
            print('Estado civil: ', person.marital_status)
            print('Parceiro: ', person.partner)
            if person.status_life == 'Morte':
                print('Morreu no ano de ', person.death_date)
                print('Morreu com idade de ', person.age_death)
                print('Morreu causa da morte foi ' + person.cause_death)
    def Relat_historia(populacao):
        for person in populacao:
            print('_________ Relatório individual dos cidadões _________')
            print(f' Nascido em {person.birth_date}, {person.name}  é uma pessoa do sexo {person.sex} Teve como caracteristicas da personalidade  {person.personality}')
            print(f' que durante sua vida se relacionou com {person.partner}, sendo então uma pessoa {person.marital_status}')
            if person.status_life == 'Morte':
                print(f'{person.name} morreu no ano de {person.death_date} aos {person.age_death} anos de idade de {person.cause_death}')
            else:
                print(f' Hoje {person.name} esta com {person.age} anos de idade.')
            print('_                _')