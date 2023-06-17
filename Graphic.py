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
        plt.title('Homens e Mulheres na simulação')
        plt.pie(data, labels= gender, autopct='%1.1f%%')
        plt.savefig('view/Image/Graphic_Gender_pie.png')
        #plt.show()
        plt.figure()
    def Graphic_marital_status(population):
        marital_status = "Casado", "Solteiros"
        single = 0
        married = 0
        for person in population:
            if person.marital_status == 'Casado' or person.marital_status == 'Casada':
                married += 1
            else:
                single += 1
        data = [married, single]
        plt.title('Estado Civil da população')
        plt.pie(data, labels=marital_status,autopct='%1.1f%%')
        plt.savefig('view/Image/Graphic_marital_status.png')
        #plt.show()
        plt.figure()

    def Graphic_status_life(population):
        status_life = "Vivos", "Mortos"
        alive = 0
        dead = 0
        for person in population:
            if person.status_life == 'ativo':
                alive += 1
            else:
                dead += 1
        data = [alive, dead]
        plt.title('Vivos e mortos da população')
        plt.bar(status_life, data)
        plt.xlabel('Status')
        plt.ylabel('Quantidade')
        plt.savefig('view/Image/Graphic_status_life.png')
        #plt.show()
        plt.figure()

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
            if cont != 1 and cont != 2:
                list_cause_death.append(cause_death)
                list_quanti.append(cont)
        plt.bar(list_cause_death,list_quanti)
        plt.title('Doença que mais matou')
        plt.xlabel('Doença')
        plt.ylabel('Quantidade')
        plt.savefig('view/Image/Graphic_deadly_disease_bar.png')
        #plt.show()
        plt.figure()
    def Graphic_death_over_years(population, anoinicio, anofim):
        data = []
        total = []
        anoAtual = 0
        totalanos = anofim - anoinicio
        while anoAtual <= totalanos:
            cont = 0
            for person in population:
                if person.death_date == (anoinicio + anoAtual):
                    cont +=1
                    total.append(cont)
                    data.append((anoinicio + anoAtual))
            anoAtual += 1
        plt.bar(data, total)
        plt.title('Morte por ano')
        plt.xlabel('Ano')
        plt.ylabel('Quantidade de Mortes')
        plt.savefig('view/Image/Graphic_death_over_years.png')
        #plt.show()
        plt.figure()