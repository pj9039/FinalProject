from fastpip import pip

# pattern; sample array
__PATTERN_DOUBLE_BOTTOM = [[0, 8000], [1, 4000], [2, 4000], [3, 8000], [4, 4000], [5, 4000], [6, 8000]]
__TRIANGLES_DESCENDING = [[0, 8000], [1, 5500], [2, 6500], [3, 5500], [4, 6000], [5, 5000], [6, 4000]]
__THREE_RIGING_VALLEYS = [[0, 6000], [1, 5500], [2, 6500], [3, 6000], [4, 7000], [5, 6500], [6, 8000]]
__ROUNDING_BOTTOMS = [[0, 8000], [1, 6000], [2, 6500], [3, 5000], [4, 6500], [5, 6000], [6, 8000]]

# Adapt pip algorithm & choose pattern by x value
def patterntype(x):
    if x == 1:      # Double Bottom Pattern
        return pip(__PATTERN_DOUBLE_BOTTOM, 7), 7
    if x == 2:      #
        return 2, 7
    if x == 3:      #
        return 3, 5
    if x == 4:      #
        return pip(__THREE_RIGING_VALLEYS, 7), 7
    if x == 5:      #
        return pip(__ROUNDING_BOTTOMS, 7), 7
    if x == 6:      #
        return pip(__TRIANGLES_DESCENDING, 7), 7
    if x == 7:      #
        return 7, 7
    if x == 8:      #
        return 8, 7
    if x == 9:      #
        return 9, 7
    else:           # DEFAULT. exception route
        return None
