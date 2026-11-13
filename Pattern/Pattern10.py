class Pattern10:
  def displayPattern(self, n):
    for i in range(1, n+1):
      for j in range(1, i+1):
        print("*", end = "")
      print("\n")

    for i in range(1, n):
      for j in range(1, n-i+1):
        print("*", end = "")

      print("\n")

P10 = Pattern10()
P10.displayPattern(2)
    