import os

def is_valid_directory(directory_path):
  """
  Checks if the given directory exists and is a directory.

  Args:
    directory_path: The path to the directory to check.

  Returns:
    True if the directory exists and is a directory, False otherwise.
  """

  if not os.path.exists(directory_path):
    return False

  if not os.path.isdir(directory_path):
    return False

  return True

def remove_commas(directory):
  change_made = False

  if is_valid_directory(directory):
    for filename in os.listdir(directory):
      if ',' in filename:
        new_filename = filename.replace(",", "")
        print("Replacing " + filename + "with " + new_filename)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        change_made = True
  else:
    print("Invalid directory I'm afraid.  Did you include quotation marks, perhaps?")
    wait_to_quit()

  return change_made

def wait_to_quit():
  input("\n \nPress Enter to end the program.")

if __name__ == "__main__":
  try:
    directory = input("Enter the directory path: ")
    removal = remove_commas(directory)
    if removal == True:
      print("Changes completed.")
      wait_to_quit()
    else:
      print("No changes made.")
      wait_to_quit()
  except:
    print("An error has ocurred")
    wait_to_quit()
