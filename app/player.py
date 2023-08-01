class Player:

    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    def uid(self):
        return self._uid

    def name(self):
        return self._name

    def __str__(self):
        return f"{self._name}"


