class LargestElement:
    def arr(self):
        nums = []
        print('Enter array size')
        n = int(input())
        print(f"Enter {n} elements in the array: ")
        for i in range(0, n):
            nums.append(int(input()))

        largest = nums[0]
        for i in range(0, n):
            
            if(nums[i]> largest):
                largest = nums[i]

        print("Largest element of array is: ", largest)

le = LargestElement()
le.arr()

        