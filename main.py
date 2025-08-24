from Game.Game import Game, Game_state

game = Game()
while game.state == Game_state.idle:
    game.start_menu()
    while game.state == Game_state.running:
        game.enter_adventure_hub()