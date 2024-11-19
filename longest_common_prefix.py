from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    length = len(strs)
    if length < 1: return res

    res = strs[0]
    minimum = len(strs[0])
    stop = False
    for i in range(1, minimum+1):
        for string in strs[1:length]:
            if string[0:i] != res[0:i]:
                stop = True
                res = string[0:i-1]
                break
        if stop: break        
    return res

if __name__ == "__main__":
    input = ["flower","flow","flight"] # Output "fl"
    res = longestCommonPrefix(input)
    print(res)
        