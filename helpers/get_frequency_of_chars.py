from collections import Counter 

def get_frequency_of_chars(array_of_text):
  combined_text =  "".join(array_of_text)

  letters = Counter(combined_text)
  sorted_common_letters = letters.most_common()

  return sorted_common_letters