def import_file(path):
  try: 
    file = open(path)

    return file
  except:
    exit("File not found - try other path")
