
"""
Approach one

-------------------------------------------//*ALGORITHM*\\----------------------------------------------------------------

1) We start with two pointers, left_left and right_right initally pointing the first element of the string S_S

2) We use the right_right pointer to expand the window until we get a desirable window i.e a window that contains all the characters of TT.

3) Once we have a window with all the characters, we can move left pointer ahead one by one. if the window is still a desirable one we keep on updating the minimum window size.

4) If the window is not desirable any more, we repeat step2 onwards.
"""
from collections import Counter
def minimum_window_substring(S_S,T_T):

    if not T_T or not S_S:
        return " "

    # Dictonary which keeps the count of all unique characters in t.
    dict_t = Counter(T_T)

    # number of unique characters in t, which need to be present in the desired window

    required = len(dict_t)

    # left and right pointers
    l,r = 0,0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency
    formed = 0


    # dictonary which keeps count of all unique characters in the current window 

    window_counts = {}

    # ans tuple of the form (window length,left,right)
    ans = float("inf"),None,None

    while r < len(s):
        # add one character from the right to the window
        characters = S_S[r]
        window_counts[character] = window_counts.get(characters,0) + 1

        # if the frequency of the current character adds equal to the desired count in t than increment the formed count by 1
        if characters in dict_t and window_counts[characters] == dict_t[characters]:
            formed+= 1

        # try and contract the window till the point where it ceases to be desirable

        while l <= r and formed == required:
            character = S_S[l]

            # save the smallest window until now
            if r - l + 1 < ans[0]:
                ans = (r - l + 1,l,r)

            # the character at the position pointed by the left pointer is no longer the part of the window
            window_counts[characters] -= 1
            if characters in dict_t and window_counts[characters] < dict_t[characters]:
                formed -= 1

            # move the left pointer ahead, this would help to look for a new window.
            l += 1

        # keep expanding the window once we are done with contracting
        r += 1
    return "" if ans[0] == float("inf") else S_S[ans[1] : ans[2] + 1]

