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


def fill(row, col, new_color):
        old_color = grid[row][col]
        navigate(row, col, new_color, old_color)
        return grid


def navigate(row, col, new_color, old_color):

        print("Checking grid[{}][{}]".format(row, col))
        directions = {"north": ["row", -1], "south": ["row", 1], "east": ["col", 1], "west": ["col", -1]}
        for direction in directions.values():
                if grid[row][col] == old_color:
                        grid[row][col] = new_color
                        print("Just changed grid[{}][{}]".format(row, col))
                if direction[0] == "row":
                        try:
                                if grid[row + direction[1]][col] != old_color:
                                        continue
                                else:
                                        navigate(row + direction[1], col, new_color, old_color)
                        except IndexError:
                                continue
                if direction[0] == "col":
                        try:
                                if grid[row][col + direction[1]] != old_color:
                                        continue
                                else:
                                        navigate(row, col + direction[1], new_color, old_color)
                        except IndexError:
                                continue


        return


def main():
        print("GRID:")
        pprint(grid)

        while True:
                try:
                        row = int(input("What row would you like to start on?\n"))
                        test_row = grid[row][0]
                        break
                except ValueError:
                        print("That entry can't be converted to a number. Please try again.")
                except IndexError:
                        print("That entry is out of range. Please try again.")
                        continue

        while True:
                try:
                        col = int(input("What row would you like to start on?\n"))
                        test_col = grid[0][col]
                        break
                except ValueError:
                        print("That entry can't be converted to a number. Please try again.")
                except IndexError:
                        print("That entry is out of range. Please try again.")
                        continue
        new_color = input("And what color should we fill with?\n")

        # new_color = "G"
        # row = 7
        # col = 3

        result = fill(row, col, new_color)

        print("\nFILLED:")
        pprint(result)


if __name__ == '__main__':      main()
