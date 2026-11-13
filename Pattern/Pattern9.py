class Pattern9:
  def displayPattern(self, n):
    for i in range(1, n+1):
      for j in range(1, n-i+1):
        print(" ", end = "")

      for k in range(1, 2*i):
        print("*", end = "")
      for j in range(1, n-i+1):
        print(" ", end = "")
      print("\n")

    for i in range(1, n+1):
      for j in range(1, i):
        print(" ", end = "")
      for k in range(1, 2*(n - i)+2):
        print("*", end = "")

      print("\n")

P9 = Pattern9()
P9.displayPattern(5)