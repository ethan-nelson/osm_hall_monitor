import math


def distanceBetweenNodes(node1, node2):
    dlat = math.fabs(node1['lat'] - node2['lat'])
    dlon = math.fabs(node1['lon'] - node2['lon'])
    return math.hypot(dlat, dlon)
