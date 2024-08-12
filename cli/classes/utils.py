import cli.constants.constants as c

def is_valid_entry(grid, x, y):
    return c.MIN_COORDINATE <= x <= c.MAX_COORDINATE and \
           c.MIN_COORDINATE <= y <= c.MAX_COORDINATE and \
           grid[x][y] == " "