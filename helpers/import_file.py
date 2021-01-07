def import_file(path):
  try: 
    file = open(path)

    return file
  except:
    print("Something went wrong - file not found")
