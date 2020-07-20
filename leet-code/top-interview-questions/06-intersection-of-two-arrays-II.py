from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        RUN TIME: O(n * log n)
        """

        # always keep the smaller array in nums1
        # find smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # sort the smaller array
        nums1 = sorted(nums1)

        intersection = []

        for number in nums2:
            index_in_nums1 = self.binary_search(nums1, number)

            if index_in_nums1 is not None:
                del nums1[index_in_nums1]
                intersection.append(number)

        return intersection

    def binary_search(self, nums: List[int], target: int, index_offset: int = 0) -> int:
        """
        find the number from array and return it's index

        @index_offset - offset to get the index from original array length

        RUN TIME: O(log n)
        """

        # if no item left in array, return None
        if len(nums) == 0:
            return None

        # if only one item inside, check by index 0
        if len(nums) == 1:
            if nums[0] == target:
                return index_offset
            else:
                return None

        # get center index of the array
        center = len(nums) // 2

        # - if the center is more than target; check left slice
        # - if the center is less than target; check right slice
        # - else; we found the number. so return the center index + offset
        if nums[center] > target:
            return self.binary_search(
                nums=nums[:center],
                target=target,
                index_offset=index_offset
            )
        elif nums[center] < target:
            return self.binary_search(
                nums=nums[center:],
                target=target,
                index_offset=center + index_offset
            )
        else:
            return center + index_offset


solution = Solution()

# Test Cases
case1 = {
    "nums1": [1, 2, 2, 1],
    "nums2": [2, 2],
}
case2 = {
    "nums1": [4, 9, 5],
    "nums2": [9, 4, 9, 8, 4],
}

assert sorted(solution.intersect(case1["nums1"], case1["nums2"])) == [2, 2]
assert sorted(solution.intersect(case2["nums1"], case2["nums2"])) == [4, 9]
