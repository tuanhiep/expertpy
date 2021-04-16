def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()
    result = 0
    for i in range(len(blueShirtSpeeds)):
        result += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return result
