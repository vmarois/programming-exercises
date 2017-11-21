def closestToZero(temps):
    """
    This function returns the closest temperature to zero among the ones in temps.
    :param temps: an iterator (list) containing the temperatures
    :return: the temperature closest to zero. If 2 temperatures have the same absolute value closest to zero, returns
    the positive one.
    """
    if len(temps) != 0:
        result = min((abs(x), x) for x in temps)[1]
        for x in temps:
            if (abs(x) == abs(result)) & (x > result):
                result = x
        return result
    else:
        return 0


temps = [2, 92, 21, -1.3, 1.2, 0.9, -0.9, 21]

print('\nClosest temperature to zero in ', temps, 'is ', closestToZero(temps))
