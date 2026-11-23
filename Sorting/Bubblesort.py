class BubbleSort:
    def Sort(self, n):
        nums = []
        print("Enter array elements: ")
        for i in range(0, n):
            nums.append(int(input()))

        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if(nums[j]> nums[j+1]):
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp

        print("Sorted array will be: ")
        for val in nums:
            print(val, end  = " ")

bs = BubbleSort()
bs.Sort(6)
