from pypokerengine.api.game import setup_config, start_poker
from Agents.strategycallplayer import StrategyCallPlayer
from Agents.consoleplayer import ConsolePlayer
from Agents.randomplayer import RandomPlayer
from Agents.honestplayer import HonestPlayer
from Agents.montecarloplayer import MonteCarloPlayer

config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=20)
config.register_player(name="f1", algorithm=ConsolePlayer())
config.register_player(name="f1", algorithm=StrategyCallPlayer())
config.register_player(name="m1", algorithm=MonteCarloPlayer())
config.register_player(name="r1", algorithm=RandomPlayer())
config.register_player(name="h1", algorithm=HonestPlayer())
game_result = start_poker(config, verbose=1)
