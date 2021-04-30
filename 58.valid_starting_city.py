# My Solution: randomly pick a starting city, go forward in clockwise direction, if you still move forward. Whenener you
# don't have enough gas to move forward, just backward 1 step to change the starting city 1 postion in count-clockwise
# direction. Check if the end city is already the starting city. Continue if not, return the current starting city if ok
#
# This solution taks O(n)

# Another Solution

# O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    numberOfCities = len(distances)
    minimumRemainingMiles = 0
    startingCityIdx = 0
    remainingMiles = 0

    for cityIdx in range(1, numberOfCities):
        distanceFromPreviousCity = distances[cityIdx - 1]
        fuelFromPreviousCity = fuel[cityIdx - 1]
        remainingMiles += fuelFromPreviousCity * mpg - distanceFromPreviousCity
        if remainingMiles < minimumRemainingMiles:
            minimumRemainingMiles = remainingMiles
            startingCityIdx = cityIdx

    return startingCityIdx
