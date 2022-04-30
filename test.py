from game import Game

#checking to make sure each game is played with a new set of dice
def test_rollable_die():
    test_game = Game(4)

    for _ in range(100):
        test_game.play_round()
        check = True

        for player in test_game.players:
            if player.rollable_die != []:
                check = False
    
    assert check