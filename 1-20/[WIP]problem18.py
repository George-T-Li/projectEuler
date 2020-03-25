# Maximum path sum 1

# compute total after each row
# use that sum to calculate the totals for the next row


def get_grid(fname):
    with open(fname, "r") as f:
        grid = []
        for line in f:
            row = line[:-1].split(" ")
            rowInt = list(map(int, row))
            grid.append(rowInt)
    return grid

grid = get_grid("problem18.txt")        
        