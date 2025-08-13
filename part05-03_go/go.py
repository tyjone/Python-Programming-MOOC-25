# Write your solution here

def who_won(game_board: list):
    flat = [cell for row in game_board for cell in row]
    p1 = sum(1 for cell in flat if cell == 1)
    p2 = sum(1 for cell in flat if cell == 2)

    return 1 if p1 > p2 else 2 if p2 > p1 else 0


if __name__ == "__main__":
    who_won([[9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]])

    


