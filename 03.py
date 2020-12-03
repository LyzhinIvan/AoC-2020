def count_trees_for_slope(forest, slope):
    height, width = len(forest), len(forest[0])
    slope_x, slope_y = slope
    x, y, trees = 0, 0, 0
    while y < height:
        if forest[y][x] == '#':
            trees += 1
        x = (x + slope_x) % width
        y += slope_y
    return trees


def part1(data):
    '''
    Count trees on the path in the forest moving with slope (right 3, down 1).
    '''
    forest = data.split('\n')[:-1]
    return count_trees_for_slope(forest, (3, 1))


def part2(data):
    '''
    For the given slopes count trees on the path in the forest moving with these slopes.
    Return a product of the obtained numbers.
    '''
    forest = data.split('\n')[:-1]
    product = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        product *= count_trees_for_slope(forest, slope)
    return product
