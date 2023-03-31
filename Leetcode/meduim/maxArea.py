"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1



Mio tarda mucho en ejecutarse
def maxArea(height):
    a = 0
    max = 0
    for i in range(len(height)):
        a = 0
        for k in range(i+1, len(height)):
            if height[i] < height[k]:
                a = height[i] * (k-i)
            elif height[k] < height[i]:
                a = height[k] * (k-i)
            else:
                a = height[i] * (k-i)
            if a > max:
                max  = a
    print(max)
    return max

maxArea([1,1])


En cambio este otro tarda menos y se maneja con 2 punteros
"""
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    print(max_area)
    return max_area

maxArea([1,1])