"""
Import python modules
"""
import os
import glob
import re
import csv
import datetime
import createTree
from configparser import ConfigParser

"""
Mapping for File Extensions
"""
file_type_map = {
    ".png": "",
    ".dds": "",
    ".json": "",
    ".prefab": "",  #.prefab files not found in data folder, must be compiled
    ".asset": "",  #.asset files not found in data folder, must be compiled
    ".LayerData.bin": "",
    ".TerrainData.bin": ""
}

"""
Mapping for File Categories
"""
file_cat_map = {
    "\\Prefabs\\": "Prefab",
    "\\Moods\\": "MoodSettings",
    "\\Sprites\\": "Sprite",
    "\\player\\": "Sprite",
    "\\UnlockedAssets\\": "Sprite",
    "\\SVGs\\": "SVGAsset",
    "\\Swatches\\": "ColorSwatch",
    "\\UIModules\\": "UIModulePrefabs",
    "\\abilities\\": "AbilityDef",
    "\\ammunition\\": "AmmunitionDef",
    "\\ammunitionBox\\": "AmmunitionBoxDef",
    "\\audioevents": "AudioEventDef",
    "\\backgrounds\\": "BackgroundDef",
    "\\behaviorVariables\\": "BehaviorVariableScope",
    "\\buildings\\": "BuildingDef",
    "\\cast\\": "CastDef",
    "\\chassis\\": "ChassisDef",
    "\\constants\\": "ContractOverride",
    "\\conversationBuckets\\": "DialogBucketDef",
    "\\descriptions\\": "BaseDescriptionDef",
    "\\designMasks\\": "DesignMaskDef",
    "\\dropship\\": "DropshipDef",
    "\\events\\": "SimGameEventDef",  # need exception for .json files here or it will break with Texture2D
    "\\factions\\": "FactionDef",
    "\\genderedoptions\\": "GenderedOptionsListDef",
    "\\hardpoints\\": "HardpointDataDef",
    "\\heatsinks\\": "HeatSinkDef",
    "\\jumpjets\\": "JumpJetDef",
    "\\lance\\": "LanceDef",
    "\\lifepathNode\\": "LifepathNodeDef",
    "\\mech\\": "MechDef",
    "\\mechlabincludes\\": "MechLabIncludeDef",
    "\\milestones\\": "SimGameMilestonDef",
    "\\movement\\": "MovementCapabilitiesDef",
    "\\nameLists\\": "SimGameStringList",
    "\\pathing\\": "PathingCapabilitiesDef",
    "\\pilot\\": "PilotDef",
    "\\portraits\\": "PortraitSettings",
    "\\shipUpgrades\\": "ShipModuleUpgrade",
    "\\shops\\": "ShopDef",
    "\\simGameConstants\\": "SimGameConstants",
    "\\simGameConversations\\": "SimGameConversations",  # .convo.bytes files
    "\\simGameStatDesc\\": "SimGameStatDescDef",
    "\\starsystem\\": "StarSystemDef",
    "\\turretChassis\\": "TurretChassisDef",
    "\\turrets\\": "TurretDef",
    "\\upgrades\\": "UpgradeDef",
    "\\vehicle\\": "VehicleDef",
    "\\vehicleChassis\\": "VehicleChassisDef",
    "\\weapon\\": "WeaponDef",
    "\\factions\\": "Texture2D",  # need exception for .dds files here or it will break with FactionDef. Also needs to add line twice for Texture2D and Sprite if in emblems/player/ folder
    "\\assetbundles\\": "AssetBundle",
    "\\maps\\": "LayerData",  # ...LayerData.bin files
    "\\maps2\\": "TerrainData"  # ...TerrainData.bin files
}
"""
returns FileType (extension) from file_type_map
"""
def get_file_type(file_path):
    for key, value in file_type_map.items():
        if key in file_path:
            return value
    return "ERROR: TYPE NOT DEFINED!"


"""
returns the FileCat (category) from the file_cat_map
"""
def get_file_cat(file_path):
    for key, value in file_cat_map.items():
        if key in file_path:
            return value
    return "ERROR: CAT NOT DEFINED!"


"""
Copies the contents of defaultManifest.csv into our new VersionManifest.csv, in preparation for 
appending the added files to it
"""
def copy_original_manifest():
    original_version_manifest = open("defaultManifest.csv", 'r')
    lines = original_version_manifest.readlines()
    original_version_manifest.close()

    new_version_manifest = open("VersionManifest.csv", "w")
    # omit last two lines of original, since we'll be appending to it
    new_version_manifest.writelines([item for item in lines[:-2]])
    new_version_manifest.close()


"""
returns the list of added files that don't appear in a default installation
"""
def get_added_file_list():
    default_tree = open("defaultTree.txt", "r")
    default_files = default_tree.read().split('\n')
    default_tree.close()

    current_files = createTree.generate_data_file_list(battletech_home)

    # not sure about how efficient this is, maybe a list comprehension could be faster?
    added_files = [file for file in current_files if file not in default_files]
    # something like added_files = [file for file in current_files if file not in default_files]
    # Removes blanks lines : unsure if needed with list comprehension / refactored file list reading code
    added_files = filter(None, added_files)
    return added_files


def get_new_manifest_lines(added_files):
    new_lines = []
    for added_file_path in added_files:
        fileID = os.path.basename(added_file_path)
        fileID = os.path.splitext(fileID)[0]
        fileType = get_file_type(added_file_path)
        fileCat = get_file_cat(added_file_path)
        fileDate = str(datetime.datetime.now().isoformat()) + "Z"
        fileDate = fileDate.replace(' ', '-')
        new_manifest_line = "{0},{1},{2},8,{3},{3},,,False,0,False".format(fileID, fileType, added_file_path, fileDate)
        new_lines.append(new_manifest_line)
    return new_lines


def write_new_manifest(new_manifest_lines):
    copy_original_manifest()
    new_manifest = open('VersionManifest.csv', 'a')
    for new_line in new_manifest_lines:
        new_manifest.write(new_line)
        new_manifest.write('\n')
    new_manifest.write(',\n')
    new_manifest.close()


if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')
    battletech_home = config.get('directories', 'battletech_home')
    added_files = get_added_file_list()
    new_manifest_lines = get_new_manifest_lines(added_files)
    write_new_manifest(new_manifest_lines)
