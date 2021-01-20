def get_text_from_file(path):
  try: 
    file = open(path)
    lines = file.readlines()
    return lines
  except:
    exit("File not found - try other path")
