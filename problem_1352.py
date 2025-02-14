"""1352. Product of the Last K Numbers

Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. 
You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, 
the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
"""

class ProductOfNumbers:
  def __init__(self):
      self.product=[1]
      self.n=1

  def add(self, num: int) -> None:
      if num==0:
          self.product=[1]
          self.n=1
      else:
          self.product.append(self.product[-1]*num)
          self.n+=1

  def getProduct(self, k: int) -> int:
      if self.n<=k:
          return 0
      else:
          return self.product[-1]//self.product[-k-1]