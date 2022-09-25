import random
from Personality import Personality
from Time import Time
class Person:
    def __init__(self):
        self.status_life = ''
        self.dad = ''
        self.mother  = ''
        self.name  = ''
        self.birth_date = ''
        self.age = 0
        self.age_death = ''
        self.death_date = ''
        self.cause_death = ''
        self.marital_status = 'solteira'
        self.partner = 'ninguém'
        self.child_number = ''
        self.sex = ['MASCULINO' , 'FEMININO']
        self.personality = []
        self.son = []
    time = Time()
    def looking_partner(self, population):
        for women in population:
            if women.marital_status == 'solteira' and women.age >= 18 and women.sex == 'FEMININO':
                for men in population:
                    if men.marital_status == 'solteira' and men.age >= 18 and men.sex == 'MASCULINO':
                        women.marital_status = 'Casada'
                        men.marital_status = 'Casado'
                        women.partner = men.name
                        men.partner = women.name
        return population
    def makes_birthday(self, population):
        for person in population:
            if person.status_life == 'ativo':
                person.age += 1
        return population
    def dies(self, population, current_date):
        for person in population:
            if person.age_death == person.age and person.status_life == 'ativo':
                person.death_date = current_date
                person.status_life = 'Morte'
                arquivo = open("arquivos/cause_death.txt", "r")
                words = []
                for line in arquivo:
                    line = line.strip()
                    words.append(line)
                arquivo.close()
                index = random.randrange(0, len(words))
                die = words[index].upper()
                person.cause_death = die
        return population
    def choose_name(self, sex):
        if sex == 'MASCULINO':
            arquivo = open("arquivos/male_names.txt", "r")
            words = []
            for line in arquivo:
                line = line.strip()
                words.append(line)
            arquivo.close()
            index = random.randrange(0, len(words))
            name = words[index].upper()
            return name
        else:
            arquivo = open("arquivos/female_names.txt", "r")
            words = []
            for line in arquivo:
                line = line.strip()
                words.append(line)
            arquivo.close()
            index = random.randrange(0, len(words))
            name = words[index].upper()
            return name
    def creates_personality(self, age):
        personality = Personality()
        profession = personality.define_profession()
        dream =   personality.define_dream()
        sport = personality.define_favorite_sport()

        if age >= 18:
            personality = [' Profissão: '+ profession,' Sonho: '+ dream, ' Gosta de : ' + sport]
        else:
            personality = [' Sonho: '+ dream+ ' Gosta de : ' + sport]

        return personality
    def born(self,current_date, year_end):
        person = Person()
        person.sex = random.choice(self.sex)
        person.name = self.choose_name(person.sex)
        person.birth_date = current_date
        person.age = 0
        person.personality = self.creates_personality(person.age)
        person.status_life = 'ativo'
        person.age_death = random.randrange(18,110)
        return person