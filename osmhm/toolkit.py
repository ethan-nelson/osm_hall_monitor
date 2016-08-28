import math


def distance_between_nodes(node1, node2):
    dlat = math.fabs(node1['lat'] - node2['lat'])
    dlon = math.fabs(node1['lon'] - node2['lon'])
    return math.hypot(dlat, dlon)
