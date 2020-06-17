def largestRectangleArea(heights):
    stack = [-1]
    heights.append(0)
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans,h * w)
        stack.append(i)
    heights.pop()
    return ans