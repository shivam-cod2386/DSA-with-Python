class Pattern3:
  def displayPattern(self, n):
    for i in range(1, n+1):
      for j in range(1, i+1):
        print(j, end = ' ')

      print("\n")

P3 = Pattern3()
P3.displayPattern(9)