def largestRectangleUnderSkyline(buildings):
    # O(n^2) time | O(1) space - where n is the number of buildings
    maxArea = 0
    for pillarIdx in range(len(buildings)):
        currentHeight = buildings[pillarIdx]

        furthestLeft = pillarIdx
        while furthestLeft > 0 and buildings[furthestLeft - 1] >= currentHeight:
            furthestLeft -= 1

        furthestRight = pillarIdx

        while furthestRight < len(buildings) - 1 and buildings[furthestRight + 1] >= currentHeight:
            furthestRight += 1

        areaWithCurrentBuilding = (furthestRight - furthestLeft + 1) * currentHeight
        maxArea = max(areaWithCurrentBuilding, maxArea)

    return maxArea
