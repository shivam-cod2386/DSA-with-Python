class Pattern16:
  def displayPattern(self, n):
    x = 65
    for i in range(1, n+1):
      
      for j in range(1, i+1):
        print(chr(x), end = " ")

      print("\n")
      x = x +1

P16 = Pattern16()
P16.displayPattern(5)