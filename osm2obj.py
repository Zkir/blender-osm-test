import bpy
import sys
import os 
import random


print("osm2blender scripts, (c) Zkir 2018")

#===============================================================
# get parameters and default values.
#===============================================================
#get the names of the input and output files
#we obtain them from blender command line
strInputFileName=sys.argv[5] 

#WorkDir = os.getcwd(strInputFileName)
#WorkDir = os.path.dirname(strInputFileName)
WorkDir = sys.argv[6]
print("we will load osm file " + strInputFileName)
print("current directory: " + WorkDir ) 

strObjectName=strInputFileName
if strObjectName[-4:len(strObjectName)] ==".osm":
    strObjectName=strObjectName[0:-4]  

#get row object name, osm file name without extention and path.
k=-1
for i in range(len(strObjectName)):
    if strObjectName[i]=="\\" or strObjectName[i]=="//":
        k=i  
if k!=-1:
    strObjectName=strObjectName[k+1:len(strObjectName)] 


strOutputFileName =  os.path.join(WorkDir, strObjectName +".blend")
strMainTextureName = os.path.join(WorkDir, strObjectName +".png")
strX3dFileName = os.path.join(WorkDir, strObjectName +".x3d")
print(strX3dFileName)



#===============================================================
# import osm file and create mesh
# blender-osm plugin is used.
#===============================================================
#bpy.ops.object.mode_set(mode='OBJECT') 
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.data.scenes["Scene"].blosm.osmSource = 'file'
bpy.data.scenes["Scene"].blosm.highways = False
bpy.data.scenes["Scene"].blosm.vegetation = False
bpy.data.scenes["Scene"].blosm.osmFilepath = strInputFileName
bpy.data.scenes["Scene"].blosm.singleObject = False

bpy.data.scenes["Scene"].blosm.mode = '3Drealistic'

#we need to make the process deterministic
random.seed(0)

#run the blender-osm plug-in
bpy.ops.blosm.import_data()


#===============================================================
# save the resulting file as blender file, we can only export after save
#===============================================================
print("saving as blender file "+ strOutputFileName)
bpy.ops.wm.save_as_mainfile(filepath=strOutputFileName)

#===============================================================
# export to  OBJ format. 
#===============================================================
print ("export to x3d")
bpy.ops.export_scene.x3d(filepath=strX3dFileName)


print ("done")




