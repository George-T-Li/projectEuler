# Largest product in a grid
def get_grid(fname):
    """Generates a 2d array of numbers from the fname text file"""
    with open(fname, "r") as f:
        grid = []
        for line in f:
            row = line[:-1].split(" ")
            grid.append(row)
    return grid

def largest_product_in_grid(fname, n):
    """Finds the largest product of n adjacent numbers in a grid provided by fname"""
    grid = get_grid(fname)
    xsize = len(grid[0])
    ysize = len(grid)
    limit = n - 1
    largest = 0
    for x in range(xsize):
        for y in range(ysize):
            if y + limit < ysize:
                downProduct = int(grid[x][y]) * int(grid[x][y+1]) * int(grid[x][y+2]) * int(grid[x][y+3])
            else:
                downProduct = 0
            if x + limit < xsize:
                rightProduct = int(grid[x][y]) * int(grid[x+1][y]) * int(grid[x+2][y]) * int(grid[x+3][y])
            else:
                rightProduct = 0

            if x + limit < xsize and y + limit < ysize:
                diagonalProductNWSE = int(grid[x][y]) * int(grid[x+1][y+1]) * int(grid[x+2][y+2]) * int(grid[x+3][y+3])
            else:
                diagonalProductNWSE = 0
            if x + limit < xsize and y >= limit:
                diagonalProductSWNE = int(grid[x][y]) * int(grid[x+1][y-1]) * int(grid[x+2][y-2]) * int(grid[x+3][y-3])
            else:
                diagonalProductSWNE = 0
            tempLargest = max(downProduct, rightProduct, diagonalProductNWSE, diagonalProductSWNE)
            if tempLargest > largest:
                largest = tempLargest
    return largest

#print(largest_product_in_grid("problem11.txt", 4))
