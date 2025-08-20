from Game.Game import Game, Game_state

game = Game()
while game.state == Game_state.idle:
    game.start_menu()
    while game.state == Game_state.running:
        game.take_step()
        game.check_state()
    game.check_if_win()
    game.check_end()