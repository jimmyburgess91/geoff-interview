from pprint import pprint
grid = [
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
        ['R', 'R', 'Y', 'Y', 'Y', 'Y', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'R', 'R', 'R', 'Y', 'R', 'R'],
        ['R', 'R', 'Y', 'Y', 'Y', 'Y', 'Y', 'R', 'R'],
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
]


def fill(row, col, new_color):
        global grid
        old_color = grid[row][col]
        direction = ["row", -1]
        navigate(row, col, direction, new_color, old_color)
        return grid


def navigate(row, col, direction, new_color, old_color):
        global grid
        print("Checking grid[{}][{}]".format(row, col))
        if grid[row][col] == old_color:
                grid[row][col] = new_color
                print("Just changed grid[{}][{}]".format(row, col))
                if direction[0] == "row":
                        if grid[row + direction[1]][col] not in [old_color, new_color]:
                                # check ahead for the boundary color and turn right
                                direction[0] = "col"
                                direction[1] = direction[1] * -1
                                navigate(row, col + direction[1], direction, new_color, old_color)
                        elif grid[row + direction[1]][col] == new_color:
                                # turn right then left
                                print("Current direction:", direction)
                                navigate(row, col + (direction[1]*-1), direction, new_color, old_color)
                        else:
                                # keep going in the same direction
                                navigate(row + direction[1], col, direction, new_color, old_color)
                if direction[0] == "col":
                        if grid[row][col + direction[1]] not in [old_color, new_color]:
                                # check ahead for the boundary color and turn right
                                direction[0] = "row"
                                navigate(row + direction[1], col, direction, new_color, old_color)
                        elif grid[row][col + direction[1]] == new_color:
                                # turn right then left
                                print("Current direction:", direction)
                                direction[1] = direction[1] * -1
                                navigate(row + (direction[1]*-1), col, direction, new_color, old_color)
                        else:
                                # keep going in the same direction
                                navigate(row, col + direction[1], direction, new_color, old_color)

        return


def main():
        global grid
        print("GRID:")
        pprint(grid)

        # new_color = input("What color would you like to change to?")
        # while True:
        #         try:
        #                 row = int(input("What row would you like to start on?\n"))
        #                 test_row = grid[row][0]
        #                 break
        #         except ValueError:
        #                 print("That entry can't be converted to a number. Please try again.")
        #         except IndexError:
        #                 print("That entry is out of range. Please try again.")
        #                 continue
        #
        # while True:
        #         try:
        #                 col = int(input("What row would you like to start on?\n"))
        #                 col = grid[0][col]
        #                 break
        #         except ValueError:
        #                 print("That entry can't be converted to a number. Please try again.")
        #         except IndexError:
        #                 print("That entry is out of range. Please try again.")
        #                 continue
        # new_color = input("And what color should we fill with?\n")

        new_color = "G"
        row = 3
        col = 3

        result = fill(row, col, new_color)

        print("\nFILLED:")
        pprint(result)


if __name__ == '__main__':      main()
