class SelectionSort:
    def Sort1(self, n):
        arr = []
        print("Enter array elements: ")
        for i in range(0, n):
            arr.append(int(input()))

        for i in range(0, n):
            mini = i
            for j in range(i+1, n):
                if(arr[j] < arr[mini]):
                    temp = arr[mini]
                    arr[mini] = arr[j]
                    arr[j] = temp

        print("Sorted Array is: ")
        for val in arr:
            print(val, end =  " ")

ss =  SelectionSort()
ss.Sort1(5)