def count_distinct_numbers(starting_position, hops):
    # Dictionary to map each digit for its corresponding possible moves
    digit_moves = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        0: [4, 6]
    }

