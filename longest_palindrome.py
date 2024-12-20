# NOT SOLVED YET

class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = {}
        res = ""
        maxPalindrome = ""
        currentPalindrome = ""
        start = 0
        end = 0        
        for i, c in enumerate(s):
            print("+")
            print(c)
            val = temp.get(ord(c))
            if val == None:
                temp[ord(c)] = i
                # if i > start:
                #     currentPalindrome = c
                # else:
                currentPalindrome += c
            else:
                if val == i-1:
                    end = i-1
                    # temp[ord(c)] = i
                    currentPalindrome += c
                    # continue
                else:
                    # end - (i - (end + 1))
                    print(temp[ord(c)])
                    print(f"Start {start}")
                    if temp[ord(c)] == end - (i - (end + 1)):
                        print("hehe")
                        currentPalindrome += c
                        # continue
                    elif temp[ord(c)] == start:
                        print("COK")
                        currentPalindrome += c
                        # currentPalindrome = currentPalindrome[start+1::] + c
                        start = start + 1
                        end = 0
                    
            temp[ord(c)] = i
            
            print(currentPalindrome)
            
            if len(currentPalindrome) > len(maxPalindrome):
                maxPalindrome = currentPalindrome
            
        return maxPalindrome
    
    def longestPalindrome2(self, s: str) -> str:
        temp = {}
        maxPalindrome = ""
        currentPalindrome = ""
        startLeft = 0
        endLeft = 0
        startRight = None
        endRight = None

        for i, c in enumerate(s):
            val = temp.get(ord(c))
            print("+")
            print(c)
            print(i)
            if val == None:
                temp[ord(c)] = i
                # if not startRight:
                #     startLeft = endLeft
                #     currentPalindrome = s[endLeft]
                if startRight != None:
                    print(f"StartRight {startRight}")
                    startLeft = startRight
                    currentPalindrome = s[startRight] + c

            else:
                print(f"StartLeft {startLeft}")
                checkCharEndOf3Palindrome = i - (startLeft + 1)
                print(f"checkCharEndOf3Palindrome {checkCharEndOf3Palindrome} i {i} startLeft {startLeft}")
                if checkCharEndOf3Palindrome == 1 and val == c  :
                    currentPalindrome = s[startLeft:i] + c
                    startLeft = startLeft + 1
                    endLeft = 0
                    startRight = i
                    endRight = None
                else:
                    checkIsCharSameWithItsLeft = i - val == 1
                    print(f"checkIsCharSameWithItsLeft {checkIsCharSameWithItsLeft} i {i} val {val}")
                    if checkIsCharSameWithItsLeft:
                        endLeft = val
                        startRight = i
                        currentPalindrome = s[startLeft:startRight] + c
                        print(f"EndLeft {endLeft} startRight {startRight}")
                    else:
                        offsetLeft = (endLeft - (i - startRight))
                        print(f"OffsetLeft {offsetLeft} val {val}")
                        if offsetLeft == val:
                            currentPalindrome += c
                        else:
                            pass
                            # print("asd")
                            # endLeft = val
                            # startLeft = 
                            # startRight = i
                            # currentPalindrome = s[startLeft:startRight] + c
            
            print(f"Current {currentPalindrome}")
            if len(currentPalindrome) > len(maxPalindrome):
                maxPalindrome = currentPalindrome
        
        return maxPalindrome

# text = "babad"
text = "abcddcbaxfabcdeedcbay"
# text = "cbbc"
res = Solution().longestPalindrome2(text)
print(f"Max palindrome {res}")