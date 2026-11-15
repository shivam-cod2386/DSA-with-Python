class Pattern17:
  def displayPattern(self, n):
    
    for i in range(1, n+1):
      x = 65
      for j in range(1, n-i+1):
        print(" ", end = "")
      for k in range(1, 2*i):
        if(k<=i):
          print(chr(x), end = "")
          x = x+1
        elif(k == i+1):
          x = x-2
          print(chr(x), end = "")
        else:
          x = x-1
          print(chr(x), end = "")

      print("\n")

P17 = Pattern17()
P17.displayPattern(5)