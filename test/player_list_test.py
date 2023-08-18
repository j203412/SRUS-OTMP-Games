import unittest
from player import Player
from player_list import PlayerList


class PlayerListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.player_list = PlayerList()
        self.players = [Player(int(i), str(i)) for i in range(6)]

    def test_head_is_initially_none(self):
        self.assertIsNone(self.player_list.head)

    def test_tail_is_initially_none(self):
        self.assertIsNone(self.player_list.tail)

    def test_head_has_player_instance(self):
        for player in self.players:
            self.player_list.append_tail(player)
        self.assertIsNotNone(self.player_list.head)
        self.assertIs(self.player_list.head.player, self.players[0])

    def test_tail_has_player_instance(self):
        for player in self.players:
            self.player_list.append_tail(player)
        self.assertIsNotNone(self.player_list.tail)
        self.assertIs(self.player_list.tail.player, self.players[-1])

    def test_delete_head(self):
        for player in self.players:
            self.player_list.append_tail(player)
        self.assertIs(self.player_list.head.player, self.players[0])
        self.player_list.delete_head()
        self.assertIs(self.player_list.head.player, self.players[1])

    def test_delete_tail(self):
        for player in self.players:
            self.player_list.append_tail(player)
        self.assertIs(self.player_list.tail.player, self.players[5])
        self.player_list.delete_tail()
        self.assertIs(self.player_list.tail.player, self.players[4])

    def test_display_entire_list_forward(self):
        for player in self.players:
            self.player_list.append_tail(player)
        self.player_list.display()
        self.assertTrue(self.player_list, "0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None")
        self.player_list.display(False)
        self.assertTrue(self.player_list, "5 <-> 4 <-> 3 <-> 2 <-> 1 <-> 0 <-> None")