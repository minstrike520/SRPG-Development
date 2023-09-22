from enum import Enum
from typing import Dict

from utilities.src.tools import is_intstr

from .player import Player, PlayerManager
from .stage import Stage

InputSession = Enum("InputSession", [
    "init",
    "newc",
    "start"
])


class Console:
    def __init__(self):
        self.input_sessions = [InputSession.init]

    def init(self, cmd) -> Dict:
        self.input_sessions = [InputSession.newc, InputSession.start]
        for s in ["client_id", "board_size"]:
            if not is_intstr(cmd[s]):
                raise Exception
        self.admin: Player = Player(int(cmd["client_id"]))
        self.stage = Stage(int(cmd["board_size"]))
        self.players = PlayerManager()
        return {}