class Pattern21:
  def displayPattern(self, n):
    for i in range(1, n+1):
      if i == 1 or i == n:
        for j in range(1, n+1):
          print("*", end = "")

      else:
        for j in range(1, n+1):
          if j == 1 or j == n:
            print("*", end = "")
          else:
            print(" ", end = "")

      print("\n")

P21 = Pattern21()
P21.displayPattern(5)