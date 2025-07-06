from Game.Game import Game, Game_state

game = Game()
while game.state == Game_state.idle:
    game.create_new_game()
    while game.state == Game_state.running:
        pass