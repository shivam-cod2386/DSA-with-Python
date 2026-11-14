class Pattern11:
  start = 0
  def displayPattern(self, n):
    for i in range(1, n+1):
      if(i%2==0):
        start = 0
      else:
        start = 1
      for j in range(1, i+1):
        print(start, end = "")
        start = 1-start

      print("\n")

P11 = Pattern11()
P11.displayPattern(5)