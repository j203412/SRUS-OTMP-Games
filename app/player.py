class Player:

    def __init__(self, uid: int, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"{self._name}"


