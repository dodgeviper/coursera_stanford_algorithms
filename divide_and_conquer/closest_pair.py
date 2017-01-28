"""
Closest Pair Algorithm:
Relatively advanced.
Input:
a set of n points in the plain.
P = {p1, p2, ....pn} of n points. where
pi = {xi, yi} coordinates on the plain.
Notation:
d(pi, pj) = euclidean distance between two points.

Output:
Find the pair of points which are closest to each other in terms
of euclidean distance.

Assumption:
for convenience all points are distinct i.e. there are no ties.
"""
import math

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def GetDistanceFromPoint(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)



"""
Brute force: takes O(n^2) time.
"""

def BruteForceClosestPair(input):
    min_distance = float('inf')
    closest_pair = []
    for p in input:
        for q in input:
            if p != q:
                distance = GetDistanceFromPoint(p, q)
                if min_distance > distance:
                    closest_pair.append((p, q))
                    min_distance = distance
    return closest_pair




"""
Lets take 1-D version of closest pair.
1. Sort points. O(nlogn) time.
2. Then do a linear scan to find closest pair of adjacent points O(n)time.
So the 1-D version can be reduced to O(nlogn)time however brute force for 1-d
version as well is still  O(n^2)
"""

"""
Now lets tackle the problem for 2-D version.
1. make copies of points sorted by x-cordinate Px and y-coordinate Py.
so O(nlogn) time. this is not enough!
2. Use divide and conquer again on sorted arrays.

ClosestPair(Px, Py)
1. Let Q = left half of P, R = right half of P.
 Form Qx, Qy, Rx, Ry sorted on x and y respectively {takes linear time}
2. (p1, q1) = ClosestPair(Qx, Qy)
3. (p2, q2) = ClosetPair(Rx, Ry)
4. If the cloest pair happens to be in the split then:
    (p3, q3) = ClosetSplitPair(Px, Py)
5. compare (p1, q1), (p2, q2), (p3, q3)

Key Idea:
only need to bother computing the closest split pair in "unlucky case" where
its distance is less than d(p1, q1) or d(p2,q2)

Calculate the l = min{d(p1,q1), d(p2, q2)}
then pass this delta to ClosesSplitPair(Px, Py, l) and then return best
of (p1, q1), (p2, q2), (p3, q3)
"""

def ClosestSplitPair(Px, Py, delta):
    """
    Let x_bar = biggest x-cordinate in left of P (O(1) time)
    Let delta_y = points of p with x-coordinate in [x_bar - delta, x_bar + delta]
        sorted by y-coordinate. O(n) time
    Initialize best = delta, best_pair = None.
    for i=1 to delta_y - 1:
        for j = 1 to min{7, delta_y - i}:
            let p, q = ith, (i +j)th points of delta_y
            if d(p, q) < best:
                best_pair = (p,q), best = d(p,q)
    :param Px:
    :param Py:
    :param delta:
    :return:
    """
    pass

