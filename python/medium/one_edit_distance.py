#!/usr/bin/env python
#
# Given two strings S and T, determine if they are both one edit distance apart.


def OneEditApart(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    if len(s1) - len(s2) > 1:
        return False

    alreadyEdited = False
    i = 0
    j = 0
    while i < len(s1):
        if s1[i] != s2[j]:
            if alreadyEdited:
                return False

            alreadyEdited = True
            if len(s1) < len(s2):
                i -= 1

        i += 1
        j += 1

    return alreadyEdited or len(s1) != len(s2)