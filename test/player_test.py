import unittest
from player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, "Oliver")

    def test_player_uid_is_string(self):
        self.assertTrue(self.player._uid, str)

    def test_player_name_is_string(self):
        self.assertTrue(self.player._name, str)

    def test_password_is_hashed(self):
        self.player.add_password('spagooli')
        self.assertIsNot(self.player.hashed_password, 'spagooli')

    def test_hashed_password_is_verified(self):
        self.player.add_password('spagooli')
        self.assertTrue(self.player.verify_password('spagooli'))


