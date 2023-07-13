class Utils:
  options = [0,1,2,3,4]

  players = 2

  fights_file = 'app/fights.json'

  fighters = {
    "player1": {
      "name": "Tonyn",
      "lastname": "Stallone",
      "special_attacks": [
        {
          "name": "usa un Taladoken!",
          "combination": ["DSD", "P"],
          "damage": 3,
        },
        {
          "name": "conecta un Remuyuken!",
          "combination": ["SD", "K"],
          "damage": 2,
        }
      ]
    },
    "player2": {
      "name": "Arnaldor",
      "lastname": "Shuatseneguer",
      "special_attacks": [
        {
          "name": "conecta un Remuyuken!",
          "combination": ["SA", "K"],
          "damage": 3,
        },
        {
          "name": "usa un Taladoken!",
          "combination": ["ASA", "P"],
          "damage": 2,
        }
      ]
    }
  }

  basic_actions = {
    "A": "retrocede",
    "S": "se agacha",
    "D": "avanza",
    "W": "salta",
    "P": "le da un puñetazo",
    "K": "da una patada",
  }

  messages = {
    "select_combat": '''
    Select your kombat:
    0. Exit
    1. Fight 1
    2. Figth 2
    3. Fight 3
    4. Custom combat
    ''',
    "len_warning": '''
     _______________________________________________________
    |                                                       |
    | !!! WARNING!!!                                        |
    |                                                       |
    |  Enter the same number of moves for hits.             |
    |  Note: if there is no hit, use an additional comma    |
    |  Example; P,,K,P or ,P,P,                             |
    |_______________________________________________________|
    ''',
    'valid_letters': '''
    Rules:
    Valid letters for movements: A,S,D,W
    Valid letters for hits: P, K

    ''',
  'enter_movement': 'Enter movements for player {player} separated by comma ej: SA,SA,W,D:\n',
  'enter_hit': 'Enter hits for player {player} separated by comma ej: K,P,P,P:\n',
  'selected_fight': 'You have selected fight: {selected}\n',
  'invalid_option': f'You have selected an incorrect option, please select between {options}',
  'start_game': "Do you want to play again? Y/N",
  'invalid_option_2': 'Invalid option use Y or N\n',
  'byebye': 'Thanks for playing, good bye!\n',
  'no_attacks': "There are no more attacks for {player}\n"
  }
