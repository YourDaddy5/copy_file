import shutil
try:
    walk = input('Enter the path to the file to be copied: ')
    where = input('Enter the path where to copy: ')
    shutil.copy(walk,where)
except FileNotFoundError:
    print("file not found, correct the path")

except:
    pass