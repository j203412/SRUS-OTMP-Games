import argon2


class Player:

    def __init__(self, uid: int, name: str):
        self._uid = uid
        self._name = name
        self._hashed_password = None

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def add_password(self, password):
        ph = argon2.PasswordHasher()
        hashed_password = ph.hash(password)
        self._hashed_password = hashed_password

    def verify_password(self, password):
        ph = argon2.PasswordHasher()
        if ph.verify(self._hashed_password, password):
            print('Success!')
            return True
        else:
            print("Failure!")
            return False

    def __repr__(self):
        return f"{self._name}"

    @property
    def hashed_password(self):
        return self._hashed_password




