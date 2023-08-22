from player import *

player = Player(1, 'Oliver')

if __name__ == "__main__":
    player.add_password('spagooli')
    print(player.hashed_password)
    player.verify_password('spagooli')
