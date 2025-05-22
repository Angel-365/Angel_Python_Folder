def parse_fen(fen):
    fen_parts = fen.split(" ")
    if len(fen_parts) < 1:
        return None  # not enough parts

    fen_pieces = fen_parts[0]
    board = []

    rows = fen_pieces.split("/")
    if len(rows) != 8:
        return None  # invalid number of rows

    for row in rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend(["."] * int(char))
            elif char.isalpha():
                board_row.append(char)
            else:
                return None  # invalid character
        if len(board_row) != 8:
            return None  # invalid row length
        board.append(board_row)

    return board

def draw_board(board):
    print("  +------------------------+")
    for i in range(8):
        print(f"{8 - i} |", end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print("|")
    print("  +------------------------+")
    print("    a b c d e f g h")


print("lets play Chess!")
print("Type a Fen string to see the board. Type exit to quit.\n")

while True:
    user_input = input("Enter FEN: ").strip()
    if user_input.lower() == "exit":
        print("Bye Bye")
        break

    board = parse_fen(user_input)
    if board is None:
        print("Wrong Fen format. Please try again.\n")
    else:
        draw_board(board)



# test fen 
# rnb2bnr/ppppkppp/8/4p3/3P2Pq/3Q4/PPP1PP1P/RNB1KBNR w KQ - 1 4
# rnb1kbnr/pppp1ppp/8/4p3/3P2Pq/3Q4/PPP1PP1P/RNB1KBNR b KQkq - 0 3
# rnbqkbnr/pppp1ppp/8/4p3/3P4/3Q4/PPP1PPPP/RNB1KBNR b KQkq - 1 2
# rnbqkbnr/pppp1ppp/8/4p3/3P4/3Q4/PPP1PPPP/RNB1KBNR w KQkq - 0 2
# rnbqkbnr/pppp1ppp/8/4p3/3P4/3Q4/PPP1PPPP/RNB1KBNR b KQkq - 1 2
# rnb1kbnr/pppp1ppp/8/4p3/3P3q/3Q4/PPP1PPPP/RNB1KBNR w KQkq - 2 3
# rnbqkbnr/pppp1ppp/8/4p3/3P4/3Q4/PPP1PPPP/RNB1KBNR b KQkq - 1 2