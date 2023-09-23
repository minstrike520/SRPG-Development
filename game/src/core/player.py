class Player:
    def __init__(self, client_id: int) -> None:
        self.client_id = client_id
        self.controlling_char_ids = set()


class PlayerManager(set):
    def __init__(self):
        super().__init__(set())

    def find_by_client_id(self, id: str):
        for p in self:
            if p.client_id == id:
                return p
        raise IndexError