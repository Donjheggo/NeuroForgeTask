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

    # Recursive function to count distinct numbers
    def count_numbers(position, remaining_hops):
        if remaining_hops == 0:
            return 1

        total_numbers = 0

        for move in digit_moves[position]:
            total_numbers += count_numbers(move, remaining_hops - 1)

        return total_numbers

    return count_numbers(starting_position, hops)
    
# Function test
starting_position = 0
hops = 10
distinct_numbers = count_distinct_numbers(starting_position, hops)
print(f"The number of distinct numbers dialed in {hops} hops from position {starting_position} is: {distinct_numbers}")

