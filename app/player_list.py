from typing import Optional
from player_node import PlayerNode
from player import Player


class PlayerList:

    def __init__(self):
        self.head: Optional[PlayerNode] = None
        self.current_node: Optional[PlayerNode] = None

    def add(self, player: Player):
        if self.head is None:
            self.head = PlayerNode(player)
            return
