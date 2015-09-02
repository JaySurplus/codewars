"""
	The Millionth Fibonacci Kata
	http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
"""

# following not working , took too much time to compute.
"""
def fib(n):
  if n == 1 or n == 0:
        return n
  a = 0
  b = 1
  i = 2
  result = 0
  if n < 0:
    return -fib(-n) if n%2==0 else fib(-n)

  while i <= n:
    result=a + b
    a=b
    b=result
    i+=1

  return result
"""


def main():
    print fib(-6)

if __name__ == '__main__':
	main()
