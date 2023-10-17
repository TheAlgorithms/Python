"""
You are given a list of segments, where each segment is represented by its
left and right endpoints.
The task is to find the minimum number of points needed to
cover all the segments.
If you can cover all the segments with points, return the points' positions;
otherwise, return -1.

Implement the SegmentIntersection class with the following methods:

 1. __init__(self, segments): The constructor that initializes the
 SegmentIntersection object with a list of segments.

 2. find_min_points(self): A method that finds the minimum number of points
 needed to coverall the segments and returns both the count of
 points and their positions as a list.

Use the following implementation notes as a guide:

1. Sort the segments by their right endpoints.
2. Initialize an empty list called points to store the positions of points.
3. While there are segments left in the list:
4. Take the segment with the smallest right endpoint, x.
5. Add the right endpoint of x to the points list.
6. Remove any segments in the list that intersect with x.
7. Return the count of points and the list of points.
"""


class SegmentIntersection:
     def __init__(self, segments: List[Tuple[int, int]]) -> None:
        """
        Initialize a SegmentIntersection object with a list of segments.

        Args:
        segments (List[Tuple[int, int]]): A list of segments, where each segment is
        represented by a tuple containing its left and right endpoints.

        Example:
        >>> segment_intersection = SegmentIntersection([(1, 3), (2, 5), (5, 6), (7, 8)])
        """
        self.segments = segments

    def find_min_points(self) -> Tuple[int, List[int]]:
        """
        Find the minimum number of points needed to cover all the segments and return both
        the count of points and their positions as a list.

        Returns:
        Tuple[int, List[int]]: A tuple containing the count of points and their positions.

        Example:
        >>> segment_intersection = SegmentIntersection([(1, 3), (2, 5), (5, 6), (7, 8)])
        >>> min_points, points = segment_intersection.find_min_points()
        >>> min_points
        3
        >>> points
        [3, 6, 8]
        """
        self.segments.sort(key=lambda x: x[1])
        points = []
        while self.segments:
            x = self.segments.pop(0)
            x1 = x[1]
            points.append(x1)
            self.segments = [seg for seg in self.segments if seg[0] > x1]
        return len(points), points


if __name__ == "__main__":
    import doctest

    doctest.testmod()
