def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                water += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1
    return water
