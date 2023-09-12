import unittest
from player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player(1, "Oliver")
        self.player_2 = Player(2, "Tamara")
        self.player_3 = Player(3, "Sarah")

        self.players = [self.player_1, self.player_2, self.player_3]

    def test_player_uid_is_string(self):
        self.assertTrue(self.player_1._uid, str)

    def test_player_name_is_string(self):
        self.assertTrue(self.player_1._name, str)

    def test_password_is_hashed(self):
        self.player_1.add_password('spagooli')
        self.assertIsNot(self.player_1.hashed_password, 'spagooli')

    def test_hashed_password_is_verified(self):
        self.player_1.add_password('spagooli')
        self.assertTrue(self.player_1.verify_password('spagooli'))

    def test_gt_method(self):
        self.player_2.score = 3
        self.assertTrue(self.player_2 > self.player_1)

    def test_lt_method(self):
        self.player_2.score = 3
        self.assertTrue(self.player_1 < self.player_2)

    def test_eq_method(self):
        self.player_2.score = 3
        self.player_1.score = 3
        self.assertTrue(self.player_2 == self.player_1)

    def test_descending_sort_method(self):
        self.player_1.score = 1
        self.player_2.score = 5
        self.player_3.score = 3

        Player.sort_by_descending(self.players)

        self.assertEqual(self.players[0].score, 5)
        self.assertEqual(self.players[-1].score, 1)
