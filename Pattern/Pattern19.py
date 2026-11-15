class Pattern19:
  def displayPattern(self, n):
    for i in range(0, n):
      for j in range(n, i, -1):
        print("*", end = "")

      for k in range(0, 2*i):
        print(" ", end = "")

      for j in range(n, i, -1):
        print("*", end = "")

      print("\n")

    for i in range(1, n+1):
      for j in range(1, i+1):
        print("*", end = "")
      for k in range(2*(n-i), 0, -1):
        print(" ", end = "")
      for j in range(1, i+1):
        print("*", end = "")

      print("\n")
      

P19 = Pattern19()
P19.displayPattern(4)