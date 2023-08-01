import unittest
from player import Player
from player_list import PlayerList


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player("1", "Oliver")

    def test_player_uid_is_string(self):
        self.assertTrue(self.player._uid, str)

    def test_player_name_is_string(self):
        self.assertTrue(self.player._name, str)


class PlayerListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.player_list = PlayerList()
        self.player = Player("1", "Oliver")

    def test_head_initially_is_none(self):
        self.assertIsNone(self.player_list.head)

    def test_add_node_to_empty_head(self):
        self.player_list.add(self.player)
        self.assertIsNotNone(self.player_list.head)
        self.assertIs(self.player_list.head.player, self.player)
