import unittest
from player import Player
from player_list import PlayerList


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, "Oliver")

    def test_player_uid_is_string(self):
        self.assertTrue(self.player._uid, str)

    def test_player_name_is_string(self):
        self.assertTrue(self.player._name, str)


class PlayerListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.player_list = PlayerList()
        self.players = [Player(int(i), str(i)) for i in range(3)]

    def test_head_is_initially_none(self):
        self.assertIsNone(self.player_list.head)

    def test_tail_is_initially_none(self):
        self.assertIsNone(self.player_list.tail)

    def test_head_has_player_instance(self):
        for player in self.players:
            self.player_list.add(player)
        self.assertIsNotNone(self.player_list.head)
        self.assertIs(self.player_list.head.player, self.players[0])

    def test_tail_has_player_instance(self):
        for player in self.players:
            self.player_list.add(player)
        self.assertIsNotNone(self.player_list.tail)
        self.assertIs(self.player_list.tail.player, self.players[-1])

