class LinearSearchArray:
    def arr(self):
        nums = []
        print("Enter the array size: ")
        n = int(input())
        print(f"Enter {n} elements in the array: ")
        for i in range(0, n):
            nums.append(int(input()))
        print("Enter target element: ")
        target = int(input())
        for i in range(0, n):
            if(nums[i] == target):
                return i
                break
            
        return -1
ls = LinearSearchArray()
print(ls.arr())