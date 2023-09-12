import argon2
from random import randrange
from random import choice

class Player:

    def __init__(self, uid: int, name: str):
        self._uid = uid
        self._name = name
        self._hashed_password = None
        self._score = 0

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @staticmethod
    def sort_by_descending(items: list):
        """Iterates left to right, checking if the current index value is greater than the previous and
        swapping these values if true"""
        for i in range(1, len(items)):
            a = items[i]
            j = i - 1
            while j >= 0 and a > items[j]:
                items[j + 1] = items[j]
                j -= 1
            items[j + 1] = a
        return items

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.score == other.score

    def __gt__(self, other):
        if isinstance(other, Player):
            return self.score > other.score

    def __lt__(self, other):
        if isinstance(other, Player):
            return self.score < other.score

    def add_password(self, password):
        """Adds a hashed password to the _hashed_password variable"""
        ph = argon2.PasswordHasher()
        hashed_password = ph.hash(password)
        self._hashed_password = hashed_password

    def verify_password(self, password):
        """Checks password passed into the method against the player's stored hashed password"""
        ph = argon2.PasswordHasher()
        if ph.verify(self._hashed_password, password):
            print('Success!')
            return True
        else:
            print("Failure!")
            return False

    def __repr__(self):
        return f"Player: {self._name} // Score: {self.score}"

    @property
    def hashed_password(self):
        return self._hashed_password


if __name__ == '__main__':

    player_names = ['Oliver', 'Tamara', 'Sarah', 'Matt', 'Michael', 'David']

    players = [Player(int(i), choice(player_names)) for i in range(6)]

    for player in players:
        player.score = randrange(0, 10)

    print(players)

    Player.sort_by_descending(players)

    print(players)




