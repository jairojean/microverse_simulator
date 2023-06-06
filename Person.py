import random
from Personality import Personality
from Time import Time
class Person:
    def __init__(self):
        self.id = 0
        self.status_life = ''
        self.name = ''
        self.birth_date = ''
        self.age = 0
        self.age_death = ''
        self.death_date = ''
        self.cause_death = ''
        self.marital_status = 'solteira'
        self.partner = 'ninguém'
        self.id_partner = 0
        self.gender = ['MASCULINO' , 'FEMININO']
        self.personality = []
    time = Time()

    @staticmethod
    def choose_name(sex):
        if sex == 'MASCULINO':
            arquivo = open("file/male_names.txt", "r")
            words = []
            for line in arquivo:
                line = line.strip()
                words.append(line)
            arquivo.close()
            index = random.randrange(0, len(words))
            name = words[index].upper()
            return name
        else:
            arquivo = open("file/female_names.txt", "r")
            words = []
            for line in arquivo:
                line = line.strip()
                words.append(line)
            arquivo.close()
            index = random.randrange(0, len(words))
            name = words[index].upper()
            return name

    @staticmethod
    def creates_personality(population):
        for person in population:
            if person.age >= 18:
                personality = Personality()
                profession = personality.define_profession()
                dream = personality.define_dream()
                movie = personality.define_favorite_movie()
                sport = personality.define_favorite_sport()
                hobbies = personality.define_hobbies()
                life_style = personality.define_life_style()
                religion = personality.define_religion()
                animal = personality.define_favorite_animal()
                state_of_mind = personality.define_state_of_mind()
                flaws = personality.define_flaws()
                person.personality = [profession,state_of_mind , religion , flaws, dream, hobbies, animal, sport, movie, life_style]
            else:
                person.personality = [f'Com essa idade de {person.age} anos, ainda esta desenvolvendo sua personalidade']
        return population

    @staticmethod
    def makes_birthday(population):
        for person in population:
            if person.status_life == 'ativo':
                person.age += 1
        return population

    @staticmethod
    def dies(population, current_date):
        for person in population:
            if person.age_death == person.age and person.status_life == 'ativo':
                person.death_date = current_date
                person.status_life = 'Morte'
                arquivo = open("file/cause_death.txt", "r")
                words = []
                for line in arquivo:
                    line = line.strip()
                    words.append(line)
                arquivo.close()
                index = random.randrange(0, len(words))
                die = words[index].upper()
                person.cause_death = die
        return population
    def born(self,current_date,id):
        person = Person()
        person.gender = random.choice(person.gender)
        person.name = self.choose_name(person.gender)
        person.birth_date = current_date
        person.id = id
        person.age = 0
        person.personality = []
        person.status_life = 'ativo'
        person.age_death = random.randrange(18,100)
        return person


