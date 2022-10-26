"""
Question:
There is one meeting room in a firm. There are N meetings in the form
of (start[i], end[i]) where start[i] is start time of meeting i and end[i]
is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the
meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of
the other chosen meeting.

Example 1:
Input:
N = 6
start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]
Output:
4

Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

Input:
N = 3
start= [10, 12, 20]
end = [20, 25, 30]
Output:
1

Explanation:
Only one meetings can be held
with given start and end timings.


Approach:

The idea is to solve problem using greedy way.
i.e. sort the meetings by their finish time and the start
selecting meetings, starting with one with least end time and the select
other meetings such that the start time of current meeting is greater
than the last meeting selected
"""


from typing import List


def maximumMeetings(n: int, start: List[int], end: List[int]) -> int:
    """
    >>> maximumMeetings(6, [1,3,0,5,8,5], [2,4,6,7,9,9])
    4

    >>> maximumMeetings(3, [10, 12, 20], [20, 25, 30])
    1
    """
    all_meetings = [(start_time,end_time) for start_time,end_time in zip(start, end)]
    all_meetings.sort(key=lambda x:(x[1],x[0]))

    possible_meet = 1
    prev = all_meetings[0]
    for each in range(1, n):
        if all_meetings[each][0] > prev[1]:
            possible_meet += 1
            prev = all_meetings[each]
    return possible_meet


if __name__ == "__main__":
    import doctest

    doctest.testmod()
