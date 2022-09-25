import random
class Personality:
    def __init__(self):
        self.profession = self.define_profession()
        self.dream = ''
        self.favorite_sport = ''
## Define Profissão
    def define_profession(self):
        file= open("personalidade/profession.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        self.profession = words[index].upper()
        return self.profession
    ## Define Sonho
    def define_dream(self):
        file= open("personalidade/dream.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        self.dream = words[index].upper()
        return self.dream
    ## Define Sonho
    def define_favorite_sport(self):
        file= open("personalidade/favorite_song.txt", "r")
        words = []
        for line in file:
            line = line.strip()
            words.append(line)
        file.close()
        index = random.randrange(0, len(words))
        self.favorite_sport = words[index].upper()
        return self.favorite_sport