
from app.utils import Utils

PLAYERS = Utils.players
MESSAGES = Utils.messages

def custom_combat():
  print(MESSAGES['valid_letters'])

  custom_fight = {}

  for player in range(PLAYERS):
    current_player = player + 1
    player_movements = input(MESSAGES['enter_movement'].format(player=current_player)).split(',')
    player_hits = input(MESSAGES['enter_hit'].format(player=current_player)).split(',')
    while(len(player_movements) != len(player_hits)):
      print(MESSAGES['len_warning'])
      player_hits = input(MESSAGES['enter_hit'].format(player=current_player)).split(',')

    custom_fight[f'player{current_player}'] = {
      'movements': [move.strip().upper() for move in player_movements],
      'hits': [hit.strip().upper() for hit in player_hits],
    }

  return custom_fight
