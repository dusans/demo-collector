from collectDemos import Game
#-------------------------------------------------------------------------------
# TEST
#-------------------------------------------------------------------------------
name = "quakelive"
demoFolder = "c:/Documents and Settings/Dule/Application Data/id Software/quakelive/home/baseq3/demos/"
screenShotFolder = "c:/Documents and Settings/Dule/Application Data/id Software/quakelive/home/baseq3/screenshots/"
outputFolder = "d:/dev/pyGameDemoCollecter/output/"
gameDemoExt = "dm_73"

quakelive = Game(name, demoFolder, screenShotFolder, outputFolder, gameDemoExt)


for d in quakelive.copy():
    print d
    for p in d.screenShots:
            print "\t", p