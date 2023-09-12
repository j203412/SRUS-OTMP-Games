
class PlayerBNode:

    def __init__(self, player):
        self._player = player
        self._left_node = None
        self._right_node = None

    @property
    def player(self):
        return self.player

    @property
    def left_node(self):
        return self.left_node

    @left_node.setter
    def left_node(self, value):
        self.left_node = value

    @property
    def right_node(self):
        return self.right_node

    @right_node.setter
    def right_node(self, value):
        self.right_node = value

