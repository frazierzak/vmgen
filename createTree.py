import os, glob, re # Imports python modules

cwd = os.path.dirname(os.path.realpath(__file__)) # Grabs current working directory
cwd = cwd + '\BattleTech_Data\StreamingAssets\data\**\**' # Appends data path plus wildcards to current directory

files = glob.glob (cwd, recursive=True) # Creates file tree
files = [re.sub(r'.*StreamingAssets\\', '', eachfile) for eachfile in files] # Removes folder path up to data\
files = filter(None, files) #Removes blanks lines

with open ('defaultTree.txt', 'w') as in_files: # Creates defaultTree.txt
    for eachfile in files: in_files.write(eachfile+'\n') # Writes each array from files into seperate lines in defaultTree.txt