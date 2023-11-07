import sys


def applicationPairs(deviceCapacity, foregroundAppList, backgroundAppList):

    result = []  # if empty return pair of list
    optimalProcessPair = []
    minCapacityLeft = sys.maxsize
    for foregroundApp in foregroundAppList:
        for backgroundApp in backgroundAppList:
            consumedMemory = foregroundApp[1] + backgroundApp[1]
            if consumedMemory <= deviceCapacity:
                currentMinCapacityLeft = deviceCapacity - consumedMemory
                if currentMinCapacityLeft <= minCapacityLeft:
                    minCapacityLeft = currentMinCapacityLeft
                result.append([foregroundApp, backgroundApp])

    for foregroundApp, backgroundApp in result:
        consumedMemory = foregroundApp[1] + backgroundApp[1]
        capacityLeft = deviceCapacity - consumedMemory
        if capacityLeft == minCapacityLeft:
            optimalProcessPair.append([foregroundApp[0], backgroundApp[0]])
    if len(optimalProcessPair) == 0:
        optimalProcessPair.append([])
    return optimalProcessPair


def applicationPairsOptimal(deviceCapacity, foregroundAppList,
                            backgroundAppList):

    foregroundAppMapper = {}
    backgroundAppMapper = {}
    result = []
    optimalProcessPair = []
    minCapacityLeft = sys.maxsize

    for foregroundApp in foregroundAppList:
        if foregroundApp[1] <= deviceCapacity:
            foregroundAppMapper[foregroundApp[0]] = foregroundApp[1]

    for backgroundApp in backgroundAppList:
        if backgroundApp[1] <= deviceCapacity:
            backgroundAppMapper[backgroundApp[0]] = backgroundApp[1]

    foregroundAppMapperList = sorted(foregroundAppMapper.items(),
                                     key=lambda x: x[1])

    backgroundAppMapperList = sorted(backgroundAppMapper.items(),
                                     key=lambda x: x[1])

    for foregroundApp in foregroundAppMapperList:
        for backgroundApp in backgroundAppMapperList:
            consumedMemory = foregroundApp[1] + backgroundApp[1]
            if consumedMemory <= deviceCapacity:
                currentMinCapacityLeft = deviceCapacity - consumedMemory
                if currentMinCapacityLeft <= minCapacityLeft:
                    minCapacityLeft = currentMinCapacityLeft
                result.append([foregroundApp, backgroundApp])
            else:
                break

    for foregroundApp, backgroundApp in result:
        consumedMemory = foregroundApp[1] + backgroundApp[1]
        capacityLeft = deviceCapacity - consumedMemory
        if capacityLeft == minCapacityLeft:
            optimalProcessPair.append([foregroundApp[0], backgroundApp[0]])
    if len(optimalProcessPair) == 0:
        optimalProcessPair.append([])
    return optimalProcessPair