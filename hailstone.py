def hailstone(n):
  # Initialize a counter to keep track of steps
  steps = 0

  # Loop until n becomes 1
  while n != 1:
      # If n is even
      if n % 2 == 0:
          n = n // 2
      # If n is odd
      else:
          n = 3 * n + 1

      
      steps += 1

  return steps