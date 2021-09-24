
# Fibonacci Given a positive integer n, 
# write a function that returns the n-th number of the Fibonacci sequence.
def n_fibo(n):
  """
  O(n) in space, O(n) in time
  """
  fibo = [0, 1]
  i = 0
  while i < n:
    fibo.append(fibo[i] + fibo[i+1])
    i += 1
  
  return fibo[i]

def n_fibo_recursive(n, fibo_last_2, fibo_last_1):
  """
  O(1) in space, O(n) in time
  """
  if n == 0:
    return fibo_last_2
  elif n == 1:
    return fibo_last_1
  else:    
    return n_fibo_recursive(n-1, fibo_last_1, fibo_last_2 + fibo_last_1)
    

if __name__ == "__main__":
  indices = [1,2,3,4,5,6,7,8]
  for n in indices:
    print("n-th number of Fibonacci sequence for {}".format(n))
    print("\titerative:", n_fibo(n))
    print("\trecursive:", n_fibo_recursive(n, 0, 1))
