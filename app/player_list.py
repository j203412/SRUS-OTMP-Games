from typing import Optional
from player_node import PlayerNode
from player import Player
from typing import Union


class PlayerList:

    def __init__(self):
        """Initialises an empty double linked list"""
        self.head: Optional[PlayerNode] = None
        self.tail: Optional[PlayerNode] = None

    def add(self, player: Player):
        new_node = PlayerNode(player)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # As there is only one node, 'new_node' is effectively both the head AND the tail
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.player, end=" <-> ")
            current_node = current_node.next_node
        print("None")

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False


player_list = PlayerList()
players = [Player(int(i), str(i)) for i in range(3)]
for player in players:
    player_list.add(player)
player_list.display()
