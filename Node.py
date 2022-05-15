class Node:
   def __init__(self, v = -1, l=None, m=None, r=None):
      self.val = v
      self.left = l
      self.right = r;
      self.mid = m

   def is_terminal(self):
      return self.left == None and self.mid == None and self.right == None

   def evaluation(self):
      return self.val

class Tree:
   def __init__(self):
      self.root = None