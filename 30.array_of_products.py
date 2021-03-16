def arrayOfProducts(array):
    # Write your code here.
    product = 1
    count = 0
    for i in range(len(array)):
        if array[i] != 0:
            product *= array[i]
        else:
            count += 1
    if count > 1:
        return [0] * len(array)
    elif count == 1:
        result = []
        for a in array:
            if a != 0:
                result.append(0)
            else:
                result.append(product)
        return result
    else:
        result = []
        for a in array:
            result.append(product / a)
        return result
