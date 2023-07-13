from app.utils import Utils

class Fighter:

  error = False

  def __init__(self, player, movements, hits, health=6):

    exists_player = Utils.fighters.get(player)

    if exists_player:
      self.player = player
      self.movements = movements
      self.hits = hits
      self.name = exists_player['name']
      self.lastname = exists_player['lastname']
      self.round = 0
      self.max_round = len(movements)
      self.current_attack_name = False
      self.current_attack_damage = False
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
      raise Exception(self.error[1])

  def calc_combinations(self):
    return len(self.movements) + len(self.hits)

  def calc_movements(self):
    return len("".join(self.movements))

  def calc_hits(self):
    return len("".join(self.hits))

  def attack(self):
    if self.max_round > self.round:
      movement = self.movements[self.round]
      hit = self.hits[self.round]
      merge_buttons = "".join([movement, hit])
      if self.is_special_attack(merge_buttons):
        print(f'{self.name} {self.current_attack_name}')
      else:

        attack_name=""
        if (len(movement) > 1):
          attack_name = "se mueve"
        if (movement in Utils.basic_actions):
          attack_name = Utils.basic_actions[movement]
        if(hit in Utils.basic_actions):
          if attack_name != "":
            attack_name += " y "
          attack_name += Utils.basic_actions[hit]
        print(f"{self.name} {attack_name}")
        self.current_attack_name = f"{self.name} {attack_name}"
        self.current_attack_damage = 1
    else:
      self.error = Utils.messages["no_attacks"].format(player=self.player)
      raise Exception(self.error)
    self.round += 1

  def is_special_attack(self, attack):
    fighter_properties = Utils.fighters[self.player]
    is_special = False
    for fighter_property in fighter_properties["special_attacks"]:
      special_combination = "".join(fighter_property["combination"])
      if special_combination == attack:
        self.current_attack_name = fighter_property["name"]
        self.current_attack_damage = fighter_property["damage"]
        is_special = True
    return is_special
