import random
class Personality:

    @staticmethod
    def define_profession():
        file= open("personalidade/profession.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        profession = words[index].upper()
        return profession

    @staticmethod
    def define_dream():
        file= open("personalidade/dream.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        dream = words[index].upper()
        return dream

    @staticmethod
    def define_favorite_sport():
        file= open("personalidade/favorite_sport.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        favorite_sport = words[index].upper()
        return favorite_sport

    @staticmethod
    def define_favorite_movie():
        file= open("personalidade/favorite_movie.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        favorite_movie = words[index].upper()
        return favorite_movie

    @staticmethod
    def define_hobbies():
        file= open("personalidade/hobbies.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        favorite_movie = words[index].upper()
        return favorite_movie

    @staticmethod
    def define_life_style():
        file= open("personalidade/life_style.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        life_style = words[index].upper()
        return life_style

    @staticmethod
    def define_religion():
        file = open("personalidade/religion.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        religion = words[index].upper()
        return religion

    @staticmethod
    def define_favorite_animal():
        file = open("personalidade/favorite_animal.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        animal = words[index].upper()
        return animal

    @staticmethod
    def define_flaws():
        file = open("personalidade/flaws.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        flaws = words[index].upper()
        return flaws

    @staticmethod
    def define_state_of_mind():
        file = open("personalidade/state_of_mind.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        state = words[index].upper()
        return state