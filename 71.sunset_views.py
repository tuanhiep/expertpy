def sunsetViews(buildings, direction):
    if len(buildings) == 0:
        return []
    if "WEST" == direction:
        start = 0
        end = len(buildings)
        step = 1
    else:
        start = len(buildings) - 1
        end = -1
        step = -1

    maxHeight = buildings[start]
    result = [start]
    for idx in range(start, end, step):
        if buildings[idx] > maxHeight:
            maxHeight = buildings[idx]
            result.append(idx)
    if "EAST" == direction:
        result = result[::-1]
    return result
