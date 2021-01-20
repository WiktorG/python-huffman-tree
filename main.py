
from helpers.get_text_from_file import get_text_from_file
from helpers.get_frequency_of_chars import get_frequency_of_chars
from operator import attrgetter
import json

all_lines = get_text_from_file("./example-text-file.txt")
chars_frequency = get_frequency_of_chars(all_lines)[::-1] # reverse array

print(chars_frequency)

class Node:
  def __init__(self = None, left = None, right = None):
    self.left = left
    self.right = right
    self.value = left.value + right.value

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, 
      sort_keys=True, indent=4)

class Leaf:
  def __init__(self, occurency_tuple):
    self.char = occurency_tuple[0]
    self.value = occurency_tuple[1]

leaf_arr = []
for el in chars_frequency:
  leaf_arr.append(Leaf(el))

class Tree:
  def index_two_min_nodes(self, node_arr):
    sorted_array = sorted(node_arr, key=lambda leaf: leaf.value)

    i1, i2 = [node_arr.index(sorted_array[0]), node_arr.index(sorted_array[1])]

    return [i1, i2]

  def build_tree(self, leaf_arr):
    tree_arr = leaf_arr

    self.index_two_min_nodes(tree_arr)

    while(len(tree_arr) > 1):
      i1, i2 = self.index_two_min_nodes(tree_arr)
      new_node = Node(tree_arr[i1], tree_arr[i2])

      tree_arr[i1] = new_node # insert node in place of smallest item
      del tree_arr[i2] # remove second smallest item since it is already in the node


    print(tree_arr[0].toJSON())
    
tree = Tree()

tree.build_tree(leaf_arr)
