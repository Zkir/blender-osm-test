"""
Test utility for blender-osm
(c) Zkir 2020
"""

import os,subprocess
import config

def compareFiles(strInputFile1, strInputFile2):
    filehandle1 = open(strInputFile1, 'r', encoding="utf-8")
    filehandle2 = open(strInputFile2, 'r', encoding="utf-8")
    txt1 = filehandle1.readline()
    while len(txt1) != 0:
        txt2 = filehandle2.readline() 
        if txt1 != txt2:
            print(txt1)
            print(txt2) 
            return False
        	 
        txt1 = filehandle1.readline()
    return True


print("Test utility for Blender-OSM, (c) Zkir 2020")
print("")

blenderExe=config.blenderExe
outputFolder=os.path.join(os.getcwd(), "output")
samplesFolder=os.path.join(os.getcwd(), "samples")

print("Running tests:")

for i in range(len(config.tests)):
    testName=config.tests[i]

    testFile=os.path.join(samplesFolder, testName+'.osm')
    strTargetFile = os.path.join(outputFolder, testName+'.x3d')
    strSampleFile = os.path.join(samplesFolder, testName+'.x3d')

    #cleanup working directory
    if os.path.isfile(strTargetFile):
        os.remove(strTargetFile)

    #test presence of blender.exe
    if not os.path.isfile(blenderExe):
        print("BLENDER executable is not found: " + blenderExe)
        exit(1)


    strCommand=blenderExe + ' --background --python osm2obj.py -- "' + testFile + '" "' + outputFolder  + '"'
    fhBlenderOut = open(os.path.join(outputFolder, testName+'.log'), 'w')
    #print(strCommand)
    subprocess.call(strCommand, cwd=os.getcwd(),stdout=fhBlenderOut, stderr=subprocess.STDOUT )
    fhBlenderOut.close()
    strResult = "OK"

    if not os.path.isfile(strTargetFile):
        strResult="FAIL: output file '" + testName +".x3d' is not created, see log"
    else:
        if not compareFiles(strTargetFile, strSampleFile):
            strResult="FAIL: result does not match sample"

    print ("  "+(testName+".osm...................................")[0:40]+strResult)

print ("Done")
