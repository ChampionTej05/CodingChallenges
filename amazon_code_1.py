def isPrimeOrder(order):
    print("Order [1]", order)
    return not order.isnumeric()


def sortOrders(orderList):
    primeOrders = []  #sorted list
    nonPrimeOrders = []
    for order in orderList:
        orderItems = order.split(" ")
        print(orderItems)
        if isPrimeOrder(orderItems[1]):
            primeOrders.append(' '.join(orderItems[1:]) + ',' + orderItems[0])
        else:
            nonPrimeOrders.append(order)
    # print("prime order", primeOrders)
    orderCart = []
    primeOrderValues = primeOrders.copy()
    primeOrderValues.sort()

    for order in primeOrderValues:
        value, id = order.split(",")
        # print(value, id)
        orderCart.append(id + ' ' + value)

    # print("prder cart", orderCart)
    orderCart = orderCart + nonPrimeOrders
    # print("Total cart", orderCart)
    return orderCart


def sortOrdersMap(orderList):
    primeOrders = {}
    nonPrimeOrders = []
    for order in orderList:
        orderItems = order.split(" ")
        print(orderItems)
        if isPrimeOrder(orderItems[1]):
            primeOrders[orderItems[0]] = ' '.join(orderItems[1:])
        else:
            nonPrimeOrders.append(order)

    sortedOrdersDict = sorted(primeOrders.items(),
                              key=lambda x: (x[1], x[0]),
                              reverse=False)
    print(sortedOrdersDict)
    orders = [x[0] + " " + x[1] for x in sortedOrdersDict]
    print("Order o", orders)
    orderCart = orders + nonPrimeOrders
    return orderCart


orderList = [
    'mi2 jog mid pet', 'wz3 34 54 398', 'a1 alps cow bar', 'x4 45 21 7',
    'fn4 n unacn boh jtzn'
]
result = sortOrdersMap(orderList)
print(result)