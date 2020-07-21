import math

def solve(a, b, c, alpha, beta, gamma):
    xpos = 0 
    ypos = 0

    xpos += a * math.cos(math.radians(alpha))
    ypos += a * math.sin(math.radians(alpha))
    print(xpos, ypos)

    xpos -= b * math.sin(math.radians(beta))
    ypos += b * math.cos(math.radians(beta))
    print(xpos, ypos)

    xpos -= c * math.cos(math.radians(gamma))
    ypos -= c * math.sin(math.radians(gamma))
    print(xpos, ypos)

    angle = 180 + math.degrees(math.atan(ypos / xpos))
    degrees = int(math.floor(angle))
    minutes = int(math.floor((angle - degrees) * 60))
    seconds = int(math.floor((angle - degrees - (minutes / 60)) * 3600))
    print(seconds)

    return [int(round((xpos**2 + ypos**2)**0.5)), degrees, minutes, seconds]

def dotest(a, b, c, A, B, C, expect):
    print("testing "+str(a)+","+str(b)+','+str(c)+","+str(A)+","+str(B)+","+str(C))
    actual = solve(a, b, c, A, B, C)
    print('Actual ', actual)
    print('Expect ', expect)
    print("#")


def tests():
    dotest(12, 20, 18, 45, 30, 60, [15, 135, 49, 18])
    dotest(15,15,19,50,29,55, [12, 133, 18, 44])
    dotest(14,25,17,41,35,59, [20, 129, 41, 57])
    
tests()
