class Pattern15:
  def displayPattern(self, n):
    for i in range(n, 0, -1):
      for j in range(0, i):
        print(chr(65 + j), end = " ")

      print("\n")

P15 = Pattern15()
P15.displayPattern(5)