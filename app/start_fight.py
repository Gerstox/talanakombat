class StartFight:
  def select_player(self, player1, player2):
    current_fighter = player1
    # # jugador con combinación menor de botones (movimiento + golpes),
    if player1.calc_combinations() < player2.calc_combinations():
      print('For combinations: Player 1 start!')
      current_fighter = player1
    elif player1.calc_combinations() > player2.calc_combinations():
      print('For combinations: Player 2 start!')
      current_fighter = player2
    else:
      # jugador con menos movimientos,
      if player1.calc_movements() < player2.calc_movements():
        print('For movements: Player 1 start!')
        current_fighter = player1
      elif player1.calc_movements() > player2.calc_movements():
        print('For movements: Player 2 start!')
        current_fighter = player2
      else:
        # jugador con menos golpes,
        if player1.calc_hits() < player2.calc_hits():
          print('For hits: Player 1 start!')
          current_fighter = player1
        elif player1.calc_hits() > player2.calc_hits():
          print('For hits: Player 2 start!')
          current_fighter = player2
        else:
          print('For default: Player 1 start!')
