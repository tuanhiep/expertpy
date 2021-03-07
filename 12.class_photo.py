def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    sign = redShirtHeights[0] - blueShirtHeights[0]
    for i in range(len(redShirtHeights)):
        if (redShirtHeights[i] - blueShirtHeights[i]) * sign <= 0:
            return False
    return True
