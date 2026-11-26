class InsertionSort:
    def sort(self, n):
        nums = []
        print(f"Enter {n} elements in the array: ")
        for i in range(0, n):
            nums.append(int(input()))

        for i in range(0, n):
            for j in range(i, 0, -1):
                if(nums[j-1]> nums[j]):
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp

        print("Sorted Array will be")
        for val in nums:
            print(val, end = " ")

i_s = InsertionSort()
i_s.sort(6)