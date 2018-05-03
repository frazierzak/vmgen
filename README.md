# vmgen
VersionManifest.csv generator for Battletech (2018) PC Game. Helps those who mod their game quickly generate the CSV file needed to load files.

1. Clone or Download my github files
2. Extract compareTree.py, defaultManifest.csv, and defaultTree.txt to your root Battletech folder. 
3. [Install Python 3.6](https://www.python.org/downloads/)! (this won't be required in the future once I compile)
4. Run compareTree.py
5. Copy VersionManifest.csv from your root Battletech folder to your BATTLETECH\BattleTech_Data\StreamingAssets\data folder and overwrite

How it works
compareTree.py searches through your /data/ folder for any new files and creates a list which it appends to a vanilla VersionManifest.csv file in your root Battletech folder. Copy this folder over to your BATTLETECH\BattleTech_Data\StreamingAssets\data folder and overwrite the old one.

Current bugs
Hard to say atm. There's a few filetypes I need to narrow down my checks for (Sprites, Texture2D) but I haven't seen too many mods using them. It's my #1 priority besides compiling so people don't need Python.

You broke my game!
It's cool, just copy defaultManifest.csv to your BATTLETECH\BattleTech_Data\StreamingAssets\data folder and rename it to VersionManifest.csv after deleting the broken one. My bad!

Let me know how it works. If you have any python experience hit me up if you have suggestions, especially for the fileType checks! That took forever to go through!
