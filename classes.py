import json

class Leaf:
  def __init__(self, occurency_tuple):
    self.char = occurency_tuple[0]
    self.value = occurency_tuple[1]

class Node:
  def __init__(self, left = None, right = None):
    self.left = left
    self.right = right
    self.value = left.value + right.value

  def __get_code(self, code = "", codes_ref = None):
    if (isinstance(self.left, Leaf)):
      codes_ref[self.left.char] = code + "1"

    if (isinstance(self.left, Node)):
      self.left.__get_code(code + "1", codes_ref)

    if(isinstance(self.right, Leaf)):
      codes_ref[self.right.char] = code + "0"

    if (isinstance(self.right, Node)):
      self.right.__get_code(code + "0", codes_ref)

  def get_codes(self):
    codes = {} # array that reference is passed to __get_code method
    self.__get_code("", codes)
    return codes
    
  def toJSON(self): # helper that allows to see whole Tree in JSON
    return json.dumps(self, default=lambda o: o.__dict__, 
      sort_keys=True, indent=4)

class Huffman:
  def index_two_min_nodes(self, node_arr): # method that gets two minimum nodes from the tree
    sorted_array = sorted(node_arr, key=lambda leaf: leaf.value)

    i1, i2 = [node_arr.index(sorted_array[0]), node_arr.index(sorted_array[1])]

    return [i1, i2]


  def build_tree(self, leaf_arr): # method that builds tree
    tree_arr = leaf_arr

    while(len(tree_arr) > 1):
      i1, i2 = self.index_two_min_nodes(tree_arr)
      new_node = Node(tree_arr[i1], tree_arr[i2])

      tree_arr[i1] = new_node # insert node in place of smallest item
      del tree_arr[i2] # remove second smallest item since it is already in the node

    return tree_arr[0]
