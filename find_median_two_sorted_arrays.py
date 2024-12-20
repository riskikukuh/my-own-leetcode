# NOT SOLVED YET

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        
        total = l1 + l2
        mid = int(total/2)
        if total % 2 == 1:
            mid += 1
        
        if l1 > 0 and l2 == 0:
            if total % 2 == 0:
                return (nums1[mid] + nums1[mid + 1]) / 2
            return nums1[mid]
        elif l2 > 0 and l1 == 0:
            if total % 2 == 0:
                return (nums2[mid] + nums2[mid + 1]) / 2
            return nums2[mid]
        
        m1 = nums1[l1-1]
        m2 = nums2[l2-1]
        
        if nums2[0] > m1:
            return nums2[mid - l1]
        # else:
        #     pass
            
        med = float(0)
        temp = nums1[0]
                
        for i in range(mid):
            if temp > nums2[i]:
                temp = nums1[i]
            else:
                temp = nums2[i]
                
            
                
            # print(temp)
            
            # if l2[i] > temp:
                # temp = l2[i]
                
            
        return med

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        print(merged)
        n = len(merged)
        if n % 2 == 0:
            div = int(n/2)
            return (merged[div-1] + merged[div]) / 2
        else:
            return float(merged[n/2])
            
        
input1 = [1,3]
input2 = [2,4]
res = Solution().findMedianSortedArrays2(input1, input2)
print(res)

# Usecase
# Ketika array2 index pertama lebih besar daripada angka terakhir dari array1 dan mid > len(array1) maka
    # Contohnya [1] [2,3,4,40]
    # nilai new mid = mid - len(array1)
    # median = array2[new mid]
# Jika array2 index pertama lebih besar namun mid < len(array1)
    # Contohnya [1,2,3,4] [40]
    # nilai new mid = mid - len(array2)
    # median = array1[new mid]

# Ketika array2 index pertama lebih kecil daripada angka terakhir dari array1
    # Lakukan merge array
        # Loop in median
        # melakukan pengecekan sebanyak `mid` kali / while True
            # Contoh
            # [1,2]
            # [3,4]
            
            # i=0
            # temp adalah tempat menyimpan angka terbesar dari pengecekan 2 angka
            # if temp = 0
                # temp = arr1[i]
            # else:
                # if temp < arr1[i]
                    # temp = arr1[i]
                # elif temp < arr2[i]
                    # temp = arr2[i]
    
    
    # Jika iya, maka nilai index median adalah pada
    # ketika tidak maka harus melakukan pengecekan satu satu
# Ketika 

# Usecase
# mid 4/2
# 1,2
# 3,4
# 1,2,3,4     2.5

# mid 7/2 + 1
# 1,2,3,4,5
# 1,2
# 1,1,2,2,3,4,5   2.0

# mid 7/2 + 1
# 1,2,3,4,5
# 60,70
# 1,2,3,4,5,60,70   4