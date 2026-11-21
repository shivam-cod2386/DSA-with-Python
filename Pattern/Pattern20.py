class Pattern20:
  def displayPattern(self, n):
    for i in range(1, n+1):
      for j in range(1, i+1):
        print("*", end = "")
      for k in range(1, 2*(n-i)+1):
        print(" ", end = "")
      for j in range(1, i+1):
        print("*", end = "")
      print("\n")

    for i in range(n-1, 0, -1):
      for j in range(1,i+1):
        print("*", end = "")
      for k in range(1, 2*(n-i)+1):
        print(" ", end = "")
      for j in range(1,i+1):
        print("*", end = "")
      print("\n")

P20 = Pattern20()
P20.displayPattern(5)
      
      