from app.utils import Utils

class Fighter:

  error = False

  def __init__(self, player, health=6):

    exists_player = Utils.fighters.get(player)

    if exists_player:
      self.player = player
      self.name = exists_player['name']
      self.lastname = exists_player['lastname']
      self.health = health
    else:
      self.error = [True, f'Player not found {player}']

  def get_player_info(self):
    if not self.error:
      print(f'''
      Player: {self.player}
      Name: {self.name}
      Lastname: {self.lastname}
      Health: {self.health}
      ''')
    else:
      print(self.error[1])

  # def fatality(self, movements="", hit=""):
  #   if self.name == 'Tonyn'

#   player1: {
#     name: "Tonyn",
#     lastname: "Stallone"
#   },
#   player2: {
#     name: "Arnaldor",
#     lastname: "Shuatseneguer"
#   },

# [
#   "Tonyn Stallone": [
#     {
#       "name": "Taladoken!",
#       "combination": ["DSD", "P"],
#       "damage" 3,
#     },
#     {
#       "name": "Remuyuken!",
#       "combination": ["SD", "K"],
#       "damage" 2,
#     },
#     {
#       "name": "Hit!",
#       "combination": ["P"],
#       "damage" 1,
#     },
#     {
#       "combination": ["K"],
#       "damage" 1,
#       "name": "Kick!",
#     },
#   ],
#   "Arnaldor Shuatseneguer": [
#     {
#       "name": "Remuyuken!",
#       "combination": ["SA", "K"],
#       "damage" 3,
#     },
#     {
#       "name": "Taladoken!",
#       "combination": ["ASA", "P"],
#       "damage" 2,
#     },
#     {
#       "name": "Hit!",
#       "combination": ["P"],
#       "damage" 1,
#     },
#     {
#       "name": "Kick!",
#       "combination": ["K"],
#       "damage" 1,
#     },
#   ],
# ]
