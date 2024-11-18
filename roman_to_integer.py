def romanToInt(s: str) -> int:
    # Solved
    # length = len(s)
    # res = 0
    # i = 0
    # while i < length:
    #     c = s[i]
    #     nc = None
    #     if i + 1 <= length -1:
    #         nc = s[i + 1]
    #     if c == "M":
    #         res += 1000
    #     elif c == "D":
    #         res += 500
    #     elif c == "C":
    #         if nc == "M":
    #             res += 900
    #             i+=2
    #             continue
    #         elif nc == "D":
    #             res += 400
    #             i+=2
    #             continue
    #         else:
    #             res += 100
    #     elif c == "X":
    #         if nc == "L":
    #             res += 40
    #             i+=2
    #             continue
    #         elif nc == "C":
    #             res += 90
    #             i+=2
    #             continue
    #         else:
    #             res += 10
    #     elif c == "I":
    #         if nc == "V":
    #             res += 4
    #             i+=2
    #             continue
    #         elif nc == "X":
    #             res += 9
    #             i+=2
    #             continue
    #         else:
    #             res += 1
    #     elif c == "L":
    #         res += 50
    #     elif c == "V":
    #         res += 5
    #     i+=1

    # Improvement using map
    length = len(s)
    res = 0
    i = 0
    obj = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    while i < length:
        c = s[i]
        if i+1 <= (length-1) and obj[s[i]] < obj[s[i+1]]:
            res += obj[s[i+1]] - obj[s[i]]
            i+=2
            continue
        res += obj[c]
        i+=1

    return res

if __name__ == "__main__":
    input = "MMMXLV" # Output 3045
    res = romanToInt(input)
    print(res)
        