class Pattern6:
  def displayPattern(self, n):
    for i in range(n, 0, -1):
      for j in range(1, i+1):
        print(j, end = " ")

      print("\n")

P6 = Pattern6()
P6.displayPattern(6)