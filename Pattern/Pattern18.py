class Pattern18:
  def displayPattern(self, n):
    x = 65+(n-1)
    for i in range(1,n+1):
      x = 65+n-i
      for j in range(1,i+1):
        print(chr(x), end = "")
        x = x+1

      print("\n")

P18 = Pattern18()
P18.displayPattern(2)