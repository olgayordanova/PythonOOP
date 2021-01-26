class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills ={}
        self.guild ="Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name]=mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        res = f'Name: {self.name}'+'\n'
        res+= f'Guild: {self.guild}'+'\n'
        res+= f'HP: {self.hp}'+'\n'
        res+= f'MP: {self.mp}'+'\n'
        for key,value in self.skills.items():
            res +=f'==={key} - {value}'+'\n'
        return res


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != self.name and player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        player_names = [p.name for p in self.players]
        if player_name not in player_names:
            return f"Player {player_name} is not in the guild."
        else:
            del self.players[player_name.index(player_name)]
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_lst = "".join ( [player.player_info () for player in self.players] )
        res = f'Guild: {self.name}' + '\n'
        res += f'{players_lst}'
        return res



