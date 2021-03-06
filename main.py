
from helpers.get_text_from_file import get_text_from_file
from helpers.get_frequency_of_chars import get_frequency_of_chars
from classes import Leaf, Huffman

all_lines = get_text_from_file("./example-text-file.txt")
chars_frequency = get_frequency_of_chars(all_lines)
leaf_arr = []

for el in chars_frequency:
  leaf_arr.append(Leaf(el))
    
huffman = Huffman()
tree = huffman.build_tree(leaf_arr)

dictionary = tree.get_codes()

print("Generated codes for letters: ", dictionary)