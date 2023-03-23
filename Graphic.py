
from matplotlib import pyplot as plt
class Graphic:
    def Graphic_Gender_pie(population):
        gender = "Masculino", "Feminino"
        Men = 0
        Women = 0
        for person in population:
            if person.gender == 'MASCULINO':
                Men += 1
            else:
                Women += 1
        data = [Men,Women]
        print(f"Homens: {Men}  Mulheres: {Women}")
        plt.pie(data, labels= gender)
        plt.show()
    def Graphic_deadly_disease_bar(population):
        illness = []
        list_cause_death = []
        list_quanti = []
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
            if cont != 1:
                list_cause_death.append(cause_death)
                list_quanti.append(cont)
                print(f'A Doença {cause_death} Matou {cont} vezes.')
        plt.bar(list_cause_death,list_quanti)
        plt.title('Doença que mais matou')
        plt.xlabel('Doença')
        plt.ylabel('Quantidade')
        plt.show()
    def Graphic_morte_ao_longo_anos(population, anoinicio, anofim):
        data = []
        total = []
        anoAtual = 0
        totalanos = anofim - anoinicio
        while anoAtual <= totalanos:
            cont = 0
            for person in population:
                if person.death_date == (anoinicio + anoAtual):
                    print(person.name, person.death_date)
                    cont +=1
                    total.append(cont)
                    data.append((anoinicio + anoAtual))
            anoAtual += 1
        plt.bar(data, total)
        plt.title('Morte por ano')
        plt.xlabel('Ano')
        plt.ylabel('Quantidade de Mortes')
        plt.show()