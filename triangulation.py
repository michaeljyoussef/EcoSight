import math

def triangulate(poleHeight, angleVert, angleHoriz):
    b = 90-angleVert
    depth = poleHeight/(math.tan(b))
    side = depth/math.tan(angleHoriz)

    # change from feet to geo-coordinates
    deltaLatitude = 2.74*math.pow(10,-6)*depth
    deltaLongitude = 2.74*math.pow(10,-6)*side

