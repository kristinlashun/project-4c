def hailstone(n): 
  
    # Base case 
    if n == 1: 
        return 1
  
    # If n is even 
    if n % 2 == 0: 
        return hailstone(n // 2) 
  
    # If n is odd 
    else: 
        return hailstone(3 * n + 1)