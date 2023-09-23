from enum import Enum
from typing import Dict

from ..utilities.tools import is_intstr

from .player import Player, PlayerManager
from .stage import Stage

InputSession = Enum("InputSession", ["init", "newc", "start"])


class IllegalOperation(Exception):

    def __init__(self, reason: str, di={}):
        detail = {"reason": reason}
        detail.update(di)
        super().__init__(str(detail))
        self.detail = detail


class Console:

    def __init__(self):
        self.input_sessions = [InputSession.init]

    def init(self, cmd) -> Dict:
        self.input_sessions = [InputSession.newc, InputSession.start]
        for s in ["client_id", "board_size"]:
            if not is_intstr(cmd[s]):
                raise IllegalOperation(
                    "argument with inaprropriate input", {
                        "argument": s,
                        "input value": cmd[s],
                        "input should be": "a number"
                    })
        self.admin: Player = Player(int(cmd["client_id"]))
        self.stage = Stage(int(cmd["board_size"]))
        self.players = PlayerManager()
        return {}
