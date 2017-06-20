from fastpip import pip

# pattern; sample array
__PATTERN_DOUBLE_BOTTOM = [[0, 8000], [1, 4000], [2, 4000], [3, 8000], [4, 4000], [5, 4000], [6, 8000]]
__PATTERN_TRIPLE_BOTTOM = [[0, 8000], [1, 4000], [2, 4000], [3, 8000], [4, 4000], [5, 4000], [6, 8000], [7, 4000], [8, 4000], [9, 8000]]
__PATTERN_SCALLOPS = [[0, 3000], [1, 6000], [2, 8000], [3, 8500], [4, 8500], [5, 8000], [6, 7000]]
__TRIANGLES_DESCENDING = [[0, 8000], [1, 5500], [2, 6500], [3, 5500], [4, 6000], [5, 5000], [6, 4000]]
__THREE_RISING_VALLEYS = [[0, 6000], [1, 5500], [2, 6500], [3, 6000], [4, 7000], [5, 6500], [6, 8000]]
__ROUNDING_BOTTOMS = [[0, 8000], [1, 6000], [2, 6500], [3, 5000], [4, 6500], [5, 6000], [6, 8000]]
__CUP_WITH_HANDLE = [[0, 4000], [1, 5250], [2, 6500], [3, 5000], [4,6500], [5, 6000], [6, 7500]]
__ROUNDING_TOPS = [[0, 4000], [1, 4700], [2, 5400], [3, 6000], [4,5400], [5, 4700], [6, 7000]]
__BUMP_AND_RUN_REVERSAL_BOTTOM = [[0, 6000], [1, 6500], [2, 6000], [3, 6250], [4,5000], [5, 6250], [6, 6000]]

# Adapt pip algorithm & choose pattern by x value
def patterntype(x):
    if x == 1:      # Double Bottom Pattern
        return pip(__PATTERN_DOUBLE_BOTTOM, 7), 7
    if x == 2:      #
        return pip(__CUP_WITH_HANDLE, 7), 7
    if x == 3:      # Scallops Pattern
        return pip(__PATTERN_SCALLOPS, 7), 7
    if x == 4:      # Three Rising Valleys Pattern
        return pip(__THREE_RISING_VALLEYS, 7), 7
    if x == 5:      # Round Bottoms Pattern
        return pip(__ROUNDING_BOTTOMS, 7), 7
    if x == 6:      # Triangles Descending Pattern
        return pip(__TRIANGLES_DESCENDING, 7), 7
    if x == 7:      #
        return pip(__ROUNDING_TOPS, 7), 7
    if x == 8:      #
        return pip(__BUMP_AND_RUN_REVERSAL_BOTTOM, 7), 7
    if x == 9:      # Triple Bottom Pattern
        return pip(__PATTERN_TRIPLE_BOTTOM, 10), 10
    else:           # DEFAULT. exception route
        return None

