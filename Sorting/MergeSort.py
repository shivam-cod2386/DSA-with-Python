class MergeSort:
  def mergeSort(self, arr=None):
    if arr is None:
      arr = []
      print("Enter the length of array: ")
      n = int(input())
      print("Enter the elements of the array: ")
      for i in range(0, n):
        arr.append(int(input()))
    if len(arr) <=1:
      return arr
    mid = len(arr)//2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    sortedleftArr = self.mergeSort(leftArr)
    sortedrightArr = self.mergeSort(rightArr)

    return self.merge(sortedleftArr, sortedrightArr)

  def merge(self, left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        result.append(left[i])
        i+= 1
      else:
        result.append(right[j])
        j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


ms = MergeSort()
print(ms.mergeSort())