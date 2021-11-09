class Game:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def start_game(self):
        print(f'Starting {self.title}!')


class MultiplayerGame(Game):
    def __init__(self, title, year, num_players, is_online):
        super().__init__(title, year)
        self.num_players = num_players
        self.is_online = is_online

    def create_team(self):
        print('Creating team!')
       

class SingleplayerGame(Game):
    def __init__(self, title, year, num_AI_enemies):
        super().__init__(title, year)
        self.num_AI_enemies = num_AI_enemies


class ShooterGame(MultiplayerGame):
    def __init__(self, title, year, num_players, is_online, is_first_person):
        super().__init__(title, year, num_players, is_online)
        self.is_first_person = is_first_person


class MOBA(MultiplayerGame):
    def __init__(self, title, year, num_players, is_online, map_size):
        super().__init__(title, year, num_players, is_online)
        self.map_size = map_size
        

cs = ShooterGame('Counter Strike', 2000, 10, True, True)

lol = MOBA('League of Legends', 2009, 15, True, 'big')
