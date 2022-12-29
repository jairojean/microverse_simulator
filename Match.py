class Match:
    @staticmethod
    def looking_partner( population):
        level_match = 0
        for women in population:
            if women.marital_status == 'solteira' and women.age >= 18 and women.sex == 'FEMININO':
                for men in population:
                    if men.marital_status == 'solteira' and men.age >= 18 and men.sex == 'MASCULINO':
                        for men_person in men.personality:
                            if men_person in women.personality:
                                level_match += 1
                                if level_match >= 3:
                                    women.marital_status = 'Casada'
                                    women.partner = men.name
                                    women.id_partner = men.id
                                    men.marital_status = 'Casado'
                                    men.partner = women.name
                                    men.id_partner = women.id
                        level_match = 0
        return population


