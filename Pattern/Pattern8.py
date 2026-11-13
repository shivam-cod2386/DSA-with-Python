class Pattern8:
  def displayPattern(self, n):
    for i in range(1, n+1):
      for j in range(1, i):
        print(" ", end = " ")

      for k in range(1, 2*(n-i)+2):
        print("*", end = " ")
      for j in range(1, i):
        print(" ", end = " ")
      print("\n")

P8 = Pattern8()
P8.displayPattern(5)