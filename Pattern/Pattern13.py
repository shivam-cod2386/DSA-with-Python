class Pattern13:
  def displayPattern(self, n):
    start = 1
    for i in range(1, n+1):
      for j in range(1, i+1):
        print(start, end = " ")
        start = start +1
      print("\n")

P13 = Pattern13()
P13.displayPattern(5)