class Pattern5:
  def displayPattern(self, n):
    for i in range(1, n+1):
      for j in range(n, i-1, -1):
        print("*", end = " ")

      print("\n")

P5 = Pattern5()
P5.displayPattern(6)