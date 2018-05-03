import os, glob, re, csv, datetime # Imports python modules
from datetime import tzinfo

cwd = os.path.dirname(os.path.realpath(__file__)) # Grabs current working directory
cwd = cwd + '\BattleTech_Data\StreamingAssets\data\**\**' # Appends data path plus wildcards to current directory

defaultTree = open("defaultTree.txt", "r")

defaultFiles = defaultTree.read().split('\n')

vmo = open("defaultManifest.csv")
lines = vmo.readlines()
vmo.close()

vmw = open("VersionManifest.csv","w")
vmw.writelines([item for item in lines[:-2]])
vmw.close()

currentFiles = glob.glob (cwd, recursive=True) # Creates file tree
currentFiles = [re.sub(r'.*StreamingAssets\\', '', eachfile) for eachfile in currentFiles] # Removes folder path up to data\
currentFiles = filter(None, currentFiles) #Removes blanks lines

addedFiles = set(defaultFiles) ^ set(currentFiles)
addedFiles = filter(None, addedFiles) #Removes blanks lines

for x in addedFiles: 
    fileID = os.path.basename(x)
    fileID = os.path.splitext(fileID)[0]
    fileType = "ERROR:TYPE NOT DEFINED!"
    while True:
        if "\\Prefabs\\" in x: 
            fileType = "Prefab" 
            break
        if "\\Moods\\" in x: 
            fileType = "MoodSettings" 
            break
        if "\\Sprites\\" in x: 
            fileType = "Sprite" 
            break #Need exception for .dds, .png
        if "\\player\\" in x: 
            fileType = "Sprite" 
            break #Need .dds exception
        if "\\UnlockedAssets\\" in x: 
            fileType = "Sprite" 
            break #Need .png exception, add twice for Texture2D
        if "\\SVGs\\" in x: 
            fileType = "SVGAsset" 
            break
        if "\\Swatches\\" in x: 
            fileType = "ColorSwatch" 
            break
        if "\\UIModules\\" in x: 
            fileType = "UIModulePrefabs" 
            break
        if "\\abilities\\" in x: 
            fileType = "AbilityDef" 
            break
        if "\\ammunition\\" in x: 
            fileType = "AmmunitionDef" 
            break
        if "\\ammunitionBox\\" in x: 
            fileType = "AmmunitionBoxDef" 
            break
        if "\\audioevents\\" in x: 
            fileType = "AudioEventDef" 
            break
        if "\\backgrounds\\" in x: 
            fileType = "BackgroundDef" 
            break
        if "\\behaviorVariables\\" in x: 
            fileType = "BehaviorVariableScope" 
            break
        if "\\buildings\\" in x: 
            fileType = "BuildingDef" 
            break
        if "\\cast\\" in x: 
            fileType = "CastDef" 
            break
        if "\\chassis\\" in x: 
            fileType = "ChassisDef" 
            break
        if "\\constants\\" in x: 
            fileType = "ApplicationConstants" 
            break
        if "\\contracts\\" in x: 
            fileType = "ContractOverride" 
            break
        if "\\conversationBuckets\\" in x: 
            fileType = "DialogBucketDef" 
            break
        if "\\conversations\\" in x: 
            fileType = "ConversationContent" 
            break
        if "\\descriptions\\" in x: 
            fileType = "BaseDescriptionDef" 
            break
        if "\\designMasks\\" in x: 
            fileType = "DesignMaskDef" 
            break
        if "\\dropship\\" in x: 
            fileType = "DropshipDef" 
            break
        if "\\events\\" in x: 
            fileType = "SimGameEventDef" 
            break
        if "\\factions\\" in x: 
            fileType = "FactionDef" 
            break #need exception for .json files here or it will break with Texture2D
        if "\\genderedoptions\\" in x: 
            fileType = "GenderedOptionsListDef" 
            break
        if "\\hardpoints\\" in x: 
            fileType = "HardpointDataDef" 
            break
        if "\\heatsinks\\" in x: 
            fileType = "HeatSinkDef" 
            break
        if "\\heraldry\\" in x: 
            fileType = "HeraldryDef" 
            break
        if "\\jumpjets\\" in x: 
            fileType = "JumpJetDef" 
            break
        if "\\lance\\" in x: 
            fileType = "LanceDef" 
            break
        if "\\lifepathNode\\" in x: 
            fileType = "LifepathNodeDef" 
            break
        if "\\mech\\" in x: 
            fileType = "MechDef" 
            break
        if "\\mechlabincludes\\" in x: 
            fileType = "MechLabIncludeDef" 
            break
        if "\\milestones\\" in x: 
            fileType = "SimGameMilestoneDef" 
            break # .json files
        if "\\movement\\" in x: 
            fileType = "MovementCapabilitiesDef" 
            break
        if "\\nameLists\\" in x: 
            fileType = "SimGameStringList" 
            break
        if "\\pathing\\" in x: 
            fileType = "PathingCapabilitiesDef" 
            break
        if "\\pilot\\" in x: 
            fileType = "PilotDef" 
            break
        if "\\portraits\\" in x: 
            fileType = "PortraitSettings" 
            break
        if "\\shipUpgrades\\" in x: 
            fileType = "ShipModuleUpgrade" 
            break
        if "\\shops\\" in x: 
            fileType = "ShopDef" 
            break
        if "\\simGameConstants\\" in x: 
            fileType = "SimGameConstants" 
            break
        if "\\simGameConversations\\" in x: 
            fileType = "SimGameConversations" 
            break #.convo.bytes files
        if "\\simGameStatDesc\\" in x: 
            fileType = "SimGameStatDescDef" 
            break
        if "\\starsystem\\" in x: 
            fileType = "StarSystemDef" 
            break
        if "\\turretChassis\\" in x: 
            fileType = "TurretChassisDef" 
            break
        if "\\turrets\\" in x: 
            fileType = "TurretDef" 
            break
        if "\\upgrades\\" in x: 
            fileType = "UpgradeDef" 
            break
        if "\\vehicle\\" in x: 
            fileType = "VehicleDef" 
            break
        if "\\vehicleChassis\\" in x: 
            fileType = "VehicleChassisDef" 
            break
        if "\\weapon\\" in x: 
            fileType = "WeaponDef" 
            break
        if "\\factions\\" in x: 
            fileType = "Texture2D" 
            break # need exception for .dds files here or it will break with FactionDef. Also needs to add line twice for Texture2D and Sprite if in emblems/player/ folder
        if "\\assetbundles\\" in x: 
            fileType = "AssetBundle" 
            break
        if "\\maps\\" in x: 
            fileType = "LayerData" 
            break # ...LayerData.bin files
        if "\\maps\\" in x: 
            fileType = "TerrainData" 
            break # ...TerrainData.bin files
    filePath = x
    fileDate = str(datetime.datetime.now().isoformat()) + "Z"
    fileDate = fileDate.replace(' ', '-')
    x = "{0},{1},{2},8,{3},{3},,,False,0,False".format(fileID, fileType, filePath, fileDate)
    vma = open('VersionManifest.csv','a')
    vma.write(x)

lastLine = "\n,"
vma.write(lastLine)
vma.close()