#!/usr/bin/env python
#
# description: Minimum Time Difference
# difficulty: Medium
# leetcode_num: 539
# leetcode_url: https://leetcode.com/problems/minimum-time-difference/
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find
# the minimum minutes difference between any two time points in the list.
#
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.


def MinimumTimeDifference(times):
    totalMins = 24 * 60
    minutesSeen = [False for _ in range(totalMins)]
    for t in times:
        hour, minute = t.split(":")
        minutes = (int(hour) * 60) + int(minute)
        minutesSeen[minutes] = True

    firstTimeSeen = None
    prevTimeSeen = None
    minimumTimeDiff = totalMins

    for i, m in enumerate(minutesSeen):
        if m:
            if firstTimeSeen == None:
                firstTimeSeen = i
                prevTimeSeen = i
            else:
                minimumTimeDiff = min(minimumTimeDiff, min(i - prevTimeSeen, totalMins - i + prevTimeSeen))
                prevTimeSeen = i

    minimumTimeDiff = min(minimumTimeDiff, min(prevTimeSeen - firstTimeSeen, totalMins - prevTimeSeen + firstTimeSeen))
    return minimumTimeDiff