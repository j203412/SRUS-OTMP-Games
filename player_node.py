from player import Player


class PlayerNode:

    def __init__(self, player: Player):
        self._player = player
        self.next_node = None
        self.previous_node = None


    @property
    def player(self):
        return self._player

    @property
    def next_node(self):
        return self.next_node

    @property
    def previous_node(self):
        return self.previous_node

    @player.setter
    def player(self, value):
        self._player = value

    @next_node.setter
    def next_node(self, value):
        self.next_node = value

    @previous_node.setter
    def previous_node(self, value):
        self.previous_node = value

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"{self._player}"
