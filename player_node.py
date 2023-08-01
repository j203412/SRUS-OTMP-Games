class PlayerNode:

    def __init__(self, player):
        self._player = player
        self.next_node = None
        self.previous_node = None

    def get_player(self):
        return self._player

    def get_next_node(self):
        return self.next_node

    def get_previous_node(self):
        return self.previous_node

    def key(self):
        return self.player._uid

    def __str__(self):
        return f"{self._player}"
