class Solution:

    def twoSum(self,nums, target) -> list:
        num_as_index = {}
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in num_as_index:
                return [num_as_index[compliment], index]
            num_as_index[num] = index
        return []


def main():
        soln = Solution()
        twoSum = soln.twoSum
        nums = [1, 2, 3, 4, 5]
        target = 9
        print(twoSum(nums, target))


if __name__ == "__main__":
        main()
