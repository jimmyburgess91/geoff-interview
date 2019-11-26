from pprint import pprint
grid = [
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
        ['R', 'R', 'Y', 'Y', 'Y', 'Y', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'R', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'Y', 'Y', 'Y', 'Y', 'R', 'R'],
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
]


def fill(row, col, new_color, old_color):
        directions = [(-1, 0),  # north
                      (1, 0),   # south
                      (0, 1),   # east
                      (0, -1)   # west
                      ]

        for direction in directions:
                if grid[row][col] == old_color:
                        grid[row][col] = new_color
                        print("Just changed grid[{}][{}]".format(row, col))
                try:
                        if grid[row + direction[0]][col + direction[1]] == old_color:
                                fill(row + direction[0], col + direction[1], new_color, old_color)
                except IndexError:
                        continue
        return grid


def main():
        print("GRID:")
        pprint(grid)

        while True:
                try:
                        row = int(input("What row would you like to start on?\n"))
                        test_row = grid[row]
                        break
                except ValueError:
                        print("That entry can't be converted to a number. Please try again.")
                except IndexError:
                        print("That entry is out of range. Please try again.")
                        continue

        while True:
                try:
                        col = int(input("What row would you like to start on?\n"))
                        old_color = test_row[col]
                        break
                except ValueError:
                        print("That entry can't be converted to a number. Please try again.")
                except IndexError:
                        print("That entry is out of range. Please try again.")
                        continue
        new_color = input("And what color should we fill with?\n")

        result = fill(row, col, new_color, old_color)

        print("\nFILLED:")
        pprint(result)


if __name__ == '__main__':      main()
