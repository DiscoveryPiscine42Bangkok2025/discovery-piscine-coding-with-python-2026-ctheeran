def is_check(kr, kc, edge, coordinate, type, direction):
    for v, h in direction:
        for r in range (1, 2 if type == "P" else edge):
            new_r = kr + (v*r)
            new_c = kc + (h*r)

            if not (0 <= new_r < edge and 0 <= new_c < edge):
                break
            
            piece = coordinate.get((new_r, new_c))

            if piece:
                if piece == type:
                    return True
                else:
                    break


def checkmate(board):
    rook = [(0,1), (0,-1), (1,0), (-1,0)]
    bishop = [(-1,-1), (1,-1), (-1,1), (1,1)]
    queen = [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (1,-1), (-1,1), (1,1)]
    pawn = [(1,-1), (1,1)]
    piecetype = {"R" : rook, "B" : bishop, "Q" : queen, "P" : pawn}
    coordinate = {}

    lines = board.strip().split("\n")
    for row, line in enumerate(lines):
        for col, piece in enumerate(line):
            if piece in ("K", "R", "Q", "B", "P"):
                coordinate[(row, col)] = piece
                if list(coordinate.values()).count("K") > 1:
                    print("There is more than one King")
                    return
                if piece == "K":
                    kr = row
                    kc = col

    for line in lines:
        if not len(line) == len(lines):
            print("The board isn't a square")
            return
    
    edge = len(lines)

    for type, direction in piecetype.items():
        if is_check(kr, kc, edge, coordinate, type, direction):
            print("Success")
            break
        else:
            print("Failed")
