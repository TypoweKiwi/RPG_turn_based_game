from Game.Game import Game, Game_state

game = Game()
while game.state == Game_state.idle:
    game.create_new_game()
    while game.state == Game_state.running:
        game.begin_current_encounter()
        game.move_a_step()
        game.check_state()
    game.check_if_win()
    game.check_end()