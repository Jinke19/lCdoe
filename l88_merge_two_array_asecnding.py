## 利用第一个数组后为0的空间，将大的数字丢到该空间里
## 注意判断始末，当左指针走完，说明nums2中p2之前的数可以直接插到nums1头
## 当右指针走完，说明已经完成全部的插入



def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    if m + n == 0:
        return None
    p1, p2 = m-1, n-1 
    
    for i in range(m + n - 1, -1, -1):
        if p2 == -1:
            break 
        elif p1 == -1:
            nums1[0:i] = nums2[0:p2+1]
            break
        elif nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]
            p1 -= 1
        elif nums1[p1] <= nums2[p2]:
            nums1[i] = nums2[p2]
            p2 -= 1
    return nums1 

print(merge([1,2,3,4,0,0,0,0],4,[9,10,11,12],4))
print(merge([10,20,30,40,0,0,0,0],4,[9,10,10,11],4))