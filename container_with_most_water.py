from typing import List

def maxArea(height: List[int]) -> int:
    # IDK
    # start = 0
    # startIndex = 0
    # maxVolume = 0
    # for i, h in enumerate(height):
    #     # print(h)
    #     if h > start:
    #         startIndex = i
    #         start = h
        
    #     if i == 0:
    #         continue

    #     volume = (i - startIndex) * h
    #     print(volume)
    #     if volume > maxVolume:
    #         maxVolume = volume

    # return maxVolume

    # O(n^2)
    # length = len(height)
    # maxVolume = 0
    # for i in range(length):
    #     for j in range(length - i):
    #         lowestLine = height[i] if height[i] < height[i + j] else height[i + j]
    #         width = (i+j) - i
    #         volume = lowestLine * width
    #         if volume > maxVolume:
    #             maxVolume = volume
    #         print(f"I {i} J {j} lowestLine {lowestLine} startIndex {i} endIndex {i+j} startHeight {height[i]} endHeight {height[i+j]} range {width} max volume {maxVolume}")

    # 2 pointer (SOLVED)
    # length = len(height)
    # maxVolume = 0
    # startHeight = 0
    # endHeight = 0
    # for i in range(length):
    #     check = height[startHeight] > height[(length - 1) - endHeight]
    #     volume = min(height[startHeight], height[(length - 1 - endHeight)]) * ((length - 1 - endHeight) - startHeight)
    #     if volume > maxVolume:
    #         maxVolume = volume
    #     if check:
    #         endHeight += 1
    #     else:
    #         startHeight += 1
    # return maxVolume

    # 2 Pointer improvement
    mx = 0
    l, r = 0, len(height) - 1
    for i in range(r + 1):
        v = min(height[l], height[r]) * (r - l)
        if v > mx:
            mx = v
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return mx

if __name__ == "__main__":
    # input = [1,3,1] # Output 2
    input = [1,8,6,2,5,4,8,3,7] # Output 49
    res = maxArea(input)
    print(res)
        