from typing import Optional
from player_node import PlayerNode
from player import Player


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
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next_node
            self.head.previous_node = None
        else:
            self.head = None
            self.tail = None

    def delete_tail(self):
        if self.tail is not None:
            self.tail = self.tail.previous_node
            self.tail.next_node = None
        else:
            self.head = None
            self.tail = None

    def display(self, forward = True):
        if forward:
            current_node = self.head
            while current_node:
                print(current_node.player, end=" <-> ")
                current_node = current_node.next_node
            print("None")
        else:
            current_node = self.tail
            while current_node:
                print(current_node.player, end=" <-> ")
                current_node = current_node.previous_node
            print("None")

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False


# player_list = PlayerList()
# players = [Player(int(i), str(i)) for i in range(6)]
# for player in players:
#     player_list.add(player)
# player_list.display()
# player_list.display(False)
# player_list.delete_tail()
# player_list.display()
# player_list.display(False)
# player_list.delete_head()
# player_list.display()
# player_list.display(False)
