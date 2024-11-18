from typing import List

def decrypt(self, code: List[int], k: int) -> List[int]:
    if k == 0:
        return [0 for x in code]
    elif k > 0 or k < 0:
        res = []
        length = len(code)
        kAbs = abs(k)
        fullCode = code + code
        for i in range(1, length + 1):
            res.append(sum(fullCode[i:kAbs + i]))
        return res
    else:
        res = []
        length = len(code)
        kAbs = abs(k)
        fullCode = code + code
        for i in range(0, length):
            res.append(sum(fullCode[length - kAbs + i:length + i]))
        return res
        
if __name__ == "__main__":
    input = [10,5,7,7,3,2,10,3,6,9,1,6]
    k = -4
    res = decrypt(input, k)
    print(res)