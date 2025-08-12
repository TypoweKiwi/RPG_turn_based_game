from Game.Saves.Load_game_func import load_game
from Game.Saves.Saves_game_func import save_game
from PlayerClasses.Team import Team
from Game.Map import Map

players = Team(name="Test")
map = Map(players=players)
save_name = "Test"
save_game(save_name=save_name, players=players, map=map)

map_after_load = load_game(save_name=save_name)

if map == map_after_load:
    print("Save_load_test - passed")
else:
    print("Save_load_test - failed")