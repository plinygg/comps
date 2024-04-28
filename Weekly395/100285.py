# You are given two arrays of equal length, nums1 and nums2.

# Each element in nums1 has been increased 
# (or decreased in the case of negative) by an integer, 
# represented by the variable x.
# As a result, nums1 becomes equal to nums2. 
# Two arrays are considered equal when they contain the same 
# integers with the same frequencies.

# 
# Return the integer x.
# 3131

class Solution:
    def addedInteger(self, nums1, nums2):
        numsone = sorted(nums1)
        numstwo = sorted(nums2)
        return (numstwo[0]-numsone[0])