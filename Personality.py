import random
class Personality:
    @staticmethod
    def define_profession():
        file= open("Build_personality/profession.txt", "r")
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
        file= open("Build_personality/dream.txt", "r")
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
        file= open("Build_personality/favorite_sport.txt", "r")
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
        file= open("Build_personality/favorite_movie.txt", "r")
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
        file= open("Build_personality/hobbies.txt", "r")
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
        file= open("Build_personality/life_style.txt", "r")
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
        file = open("Build_personality/religion.txt", "r")
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
        file = open("Build_personality/favorite_animal.txt", "r")
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
        file = open("Build_personality/flaws.txt", "r")
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
        file = open("Build_personality/state_of_mind.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        state = words[index].upper()
        return state