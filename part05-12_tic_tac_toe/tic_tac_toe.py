# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in range(3) or y not in range(3):
        return False
    if game_board[y][x] != "":
        return False
    game_board[y][x] = piece
    return True

if __name__ == "__main__":
    game_board = [["X", "O", "O"], ["O", "", "X"], ["X", "", "X"]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)
