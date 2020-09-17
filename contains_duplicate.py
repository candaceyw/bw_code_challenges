class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # create a dict for dups
        duplicates = {}

        # iterate through nums
        for num in nums:

            if num in duplicates:
                # then we have matching pair so return True
                return True

            else:
                duplicates[num] = 1  # <--- number doesn't matter
        # else no matching pair so return false
        return False

# if any value repeats

# Return True

# if no value repeats
# Return False