from app.manage_json import ManageJson
from app.utils import Utils
from app.start_fight import StartFight
from app.fighter import Fighter
import time

def main():
  manageJson = ManageJson()

  default_fights = manageJson.read_json(Utils.fights_file)
  fighters = Utils.fighters

  MESSAGES = Utils.messages
  select_options = Utils.options

  kombat_selection = int(input(MESSAGES['select_combat']))

  print(MESSAGES['selected_fight'].format(selected=kombat_selection))

  if kombat_selection not in select_options:
    print(MESSAGES['invalid_option'])
  elif kombat_selection == 4:
    from app.custom_combat import custom_combat
    combat = custom_combat()
  else:
    combat = default_fights[f'fight{kombat_selection}']

  player1 = Fighter('player1', combat['player1']['movements'], combat['player1']['hits'])
  player2 = Fighter('player2', combat['player2']['movements'], combat['player2']['hits'])

  # We decided which player attack first
  current_fighter = StartFight.select_player(player1, player2)

  finish_battle = False

  while not finish_battle:
    time.sleep(2)
    print(f"""
      Player1 health: {player1.health}
      Player2 health: {player2.health}
    """)
    if player1.health > 0 and player2.health > 0:
      current_fighter.attack()

      # We change player
      if current_fighter.player == "player1":
        player2.health -= player1.current_attack_damage
        current_fighter = player2
      else:
        player1.health -= player2.current_attack_damage
        current_fighter = player1
      steps += 1
    else:
      finish_battle = True
      if player1.health <= 0:
        finish_game(player1, player2)
      if player2.health <= 0:
        finish_game(player2, player1)


def finish_game(looser, winner):
  print(f"""{looser.player}, {looser.name} {looser.lastname} has died in combat
      at the hands of {winner.name} {winner.lastname}.""")

if __name__ == "__main__":
    main()
