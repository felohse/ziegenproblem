import lib

total_games_switched = 0
total_games_switched_won = 0

total_games_stayed = 0
total_games_stayed_won = 0

for i in range(100):
    game = lib.Game()
    result = game.result()
    # result = ('tactic', won?)
    if result[0] == 'stay':
        total_games_stayed = total_games_stayed + 1
        if result[1]:
            total_games_stayed_won = total_games_stayed_won + 1
    elif result[0] == 'switch':
        total_games_switched = total_games_switched + 1
        if result[1]:
            total_games_switched_won = total_games_switched_won + 1
    if total_games_switched != 0 and total_games_stayed != 0:
        print(f"Total switched: {total_games_switched} Total switched won: {total_games_switched_won} Switched win percentage: {total_games_switched_won/total_games_switched} "
          f"Total stayed: {total_games_stayed} Total stayed won: {total_games_stayed_won} Stayed win percentage: {total_games_stayed_won/total_games_stayed}")


