'''Problem 15
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?'''

'''Permutation with repetitions'''

def fat(num):
    return reduce(lambda x,y:x*y ,range(1,num+1) )


grid_width = 20
grid_height = 20
grid_total = grid_width + grid_height

# n!/(n1! x n2!)

n = grid_total
n1 = grid_height
n2 = grid_width

routes = fat(n)/(fat(n1)*fat(n2))

print "routes in %dx%d grid with 2 variations: %d" % (grid_width, grid_height, routes)
