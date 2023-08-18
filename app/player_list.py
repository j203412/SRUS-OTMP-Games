from typing import Optional
from player_node import PlayerNode
from player import Player


class PlayerList:

    def __init__(self):
        """Initialises an empty double linked list"""
        self.head: Optional[PlayerNode] = None
        self.tail: Optional[PlayerNode] = None

    def append_head(self, player: Player):
        new_node = PlayerNode(player)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # As there is only one node, 'new_node' is effectively both the head AND the tail
        else:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node

    def append_tail(self, player: Player):
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

    def delete_by_uid(self, uid):
        current_node = self.head
        while current_node:
            if current_node.player.uid == uid:
                if current_node.previous_node is not None:  # Checks if there is a node before the current one
                    current_node.previous_node.next_node = current_node.next_node  # Bypasses the node to be deleted
                else:
                    self.head = current_node.next_node  # If there's no previous node, move the head along
                if current_node.next_node is not None:  # Checks if there is a node after the current one
                    current_node.next_node.previous_node = current_node.previous_node  # Bypasses the node to be deleted
                else:
                    self.tail = current_node.previous_node  # If there's no next node, bring the tail back
                return
            else:
                current_node = current_node.next_node  # Continue to iterate until a uid match has been found

    def display(self, forward=True):
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


if __name__ == '__main__':
    player_list = PlayerList()
    players = [Player(int(i), str(i)) for i in range(6)]
    player_head = Player(0, "0")

    for player in players:
        player_list.append_tail(player)
    player_list.display()
    player_list.display(False)
    player_list.delete_tail()
    player_list.display()
    player_list.display(False)
    player_list.delete_head()
    player_list.display()
    player_list.display(False)
    player_list.append_head(player_head)
    player_list.display()
    player_list.delete_by_uid(3)
    player_list.display()
    player_list.delete_by_uid(2)
    player_list.display()
