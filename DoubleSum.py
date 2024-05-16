#-------------------------------------------------------------- BST solution
from collections import deque

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.index = 0

class BST:
  def __init__(self,value):
    self.root = Node(value)

  def insert(self, value,index):
    new_node = Node(value)
    new_node.index = index
    if self.root is None:
      self.root = new_node
      return

    parent = None
    current = self.root
    while current is not None:
      parent = current
      if value < current.value:
        current = current.left
      else:
        current = current.right

    if value < parent.value:
      parent.left = new_node
    else:
      parent.right = new_node

  def search(self, value):
    current = self.root
    while current is not None:
      if value == current.value:
        return True
      elif value < current.value:
        current = current.left
      else:
        current = current.right
    return False

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    bst = BST(target)
    for i in range(len(nums)):
      bst.insert(nums[i], i)

    curr = bst.root.left
    found = False
    t = []
    while curr != None and not found:
      if curr.right != None:
        r = (curr.right.value + curr.value)
        if r < target:
          curr = curr.right
        elif r > target:
          curr = curr.left
        else:
          t.append(curr.right.index)
          t.append(curr.index)
          found = True  # Set found to True after finding a pair
      if curr.left != None and not found:  # Check for left child only if not found yet
        l = (curr.left.value + curr.value)
        if l == target:
          t.append(curr.left.index)
          t.append(curr.index)
          found = True

    return t if found else []  # Return empty list if no pair is found

nums = [2,7,11,15]
target = 9

s = Solution()
l = s.twoSum(nums,target)
print(l)


#-------------------------------------------------------------- optimized solution
def Sum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        t = []
        c = []
        
        for i in range(len(nums)):
            m[nums[i]] = i
            c.append(0)
        
        for i in range(len(nums)):
            try:
                if c[i] == 1:
                    continue
                if target-nums[i] in m and m[target-nums[i]] != i:
                    t.append(i)
                    t.append(m[target-nums[i]])
                    return t
            except:
                pass
            c[i] = 1
        return t
      
