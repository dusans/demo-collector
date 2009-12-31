import os
import re
import shutil
import datetime

class Demo:
    def __init__(self, path, screenShots=[]):
        self.path = path
        self.name = ".".join(re.split('\\\\|/', path)[-1].split(".")[:-1])
        self.ext =  re.split('\\\\|/', path)[-1].split(".")[-1]
        self.startDate = os.stat(path).st_ctime
        self.endDate = os.stat(path).st_mtime
        self.screenShots = self.getScreenShots(screenShots)

    def hasShots(self):
        return len(self.screenShots) > 0

    def getScreenShots(self, screenShots):
        return [s for s in screenShots if self.startDate < s.date < self.endDate - 15 ]

    def __str__(self):
        return "<Demo: name: %s, startDate: %s, endDate: %s>" % (self.name, self.startDate, self.endDate)

class ScreenShot:
    def __init__(self, path):
        self.path = path
        self.name = ".".join(re.split('\\\\|/', path)[-1].split(".")[:-1])
        self.ext =  re.split('\\\\|/', path)[-1].split(".")[-1]
        self.date = os.stat(path).st_ctime

    def __str__(self):
        return "<ScreenShot: name: %s, date: %s>" % (self.name, self.date)

class Game:
    def __init__(self, name, demoFolder, screenShotFolder, outputFolder, gameDemoExt, nameShorteners=[], grouper=[""]):
        self.name = name
        self.demoFolder = demoFolder
        self.screenShotFolder = screenShotFolder
        self.outputFolder = outputFolder
        self.gameDemoExt = gameDemoExt
        self.nameShorteners = nameShorteners
        self.grouper = grouper
        #self SET
        self.countFile = "%s/%s" % (outputFolder, "demoIndex.count")
        self.lastCopyDateFile = "%s/%s" % (demoFolder, "lastCopy.date")
        self.lastCopyDate = 1140000000
        self.counter = 0
        self.demos = []
        self.setup()

    def __str__(self):
        return """<Game: name: %s,
                    demoFolder: %s,
                    screenShotFolder: %s,
                    outputFolder: %s,
                    gameDemoExt: %s>""" % ( self.name,
                                            self.demoFolder,
                                            self.screenShotFolder,
                                            self.outputFolder,
                                            self.gameDemoExt)

    # Test if all folders exist
    def test(self):
        for folder in [self.demoFolder, self.screenShotFolder, self.outputFolder]:
            if not os.path.isdir(folder):
                return (False, "%s doesnt exist" % folder)
        return (True, "OK")

    #=============== COUNTER ===============
    def getCounter(self):
        # If counter exists it gets its value else its set to 0
        if os.path.isfile(self.countFile):
            self.counter = int(open(self.countFile).readline())
        else:
            open(self.countFile, "w").write("0")

    #=============== LAST COPY ===============
    def getLastCopyDate(self):
        if os.path.isfile(self.lastCopyDateFile):
            self.lastCopyDate = os.stat(self.lastCopyDateFile).st_atime

    # Recursively get files from a directory with the desired extension
    def getFiles(self, directory, ext):
        for directory in os.walk(directory):
            for f in directory[2]:
                if f.endswith(ext):
                    yield "%s/%s" % (directory[0], f)

    def getScreenShots(self):
        self.screenShots = [ScreenShot("%s/%s" % (self.screenShotFolder, s)) for s in os.listdir(self.screenShotFolder)]

    def getDemos(self):
        demos = [Demo(f, self.screenShots) for f in self.getFiles(self.demoFolder, self.gameDemoExt)]
        self.demos = [d for d in demos if d.endDate > self.lastCopyDate]

    def setCounterAndDate(self):
        open(self.countFile, "w").write(str(self.counter))
        open(self.lastCopyDateFile, "w").write(str(datetime.datetime.now()))

    def setup(self):
        if self.test()[0]:
            self.getLastCopyDate()
            self.getCounter()
            self.getScreenShots()
            self.getDemos()

    def group(self, grouper, name):
        #print grouper, name
        if grouper != None:
            for folder in grouper:
                if re.search(grouper[folder].get('v', 'xgoOwnsU'), name):
                    #print "Match", grouper[folder]['v']
                    return folder + "/" + self.group(grouper[folder].get('c'), name)
        return ""

    def copy(self):
        for d in self.demos:
            if d.hasShots():
                deltas = []
                name = d.name.replace("__", "_")
                # GROUP, SORT DEMO INTO FOLDER
                groupDir = self.group(self.grouper[0], name)
                try:
                    groupPath = "%s/%s" % (self.outputFolder, groupDir)
                    if not os.path.exists(groupPath):
                        os.makedirs(groupPath)
                except:
                    groupDir = ""
                    print "Error at makedirs... dir maybe already exists"

                # SHORT DEMO NAME, BASSED ON REGEX IN nameShorteners
                if len(self.nameShorteners) > 0:
                    for r in self.nameShorteners.values():
                        name = re.sub(r, "", name)
                # Copy screenShots
                for s in d.screenShots:
                    #print "Copy", s
                    delta = s.date - d.startDate
                    delta = datetime.time(minute=int(delta/60), second=int(delta%60))
                    shutil.copyfile(s.path, "%s/%s/%s-%s__%s__.%s" % (self.outputFolder, groupDir, self.counter, name, delta.strftime("%M.%S"), s.ext))
                    deltas.append(delta.strftime("%M.%S"))
                # Copy demo
                yield d
                shutil.copyfile(d.path, "%s/%s/%s-%s__%s__.%s" % (self.outputFolder, groupDir, self.counter, name, "_".join(deltas), d.ext))
                self.counter += 1
        # After copy set counter and date files
        self.setCounterAndDate()

#-------------------------------------------------------------------------------
# TEST
#-------------------------------------------------------------------------------
##import yaml
##settings = yaml.load(open("../files/settings.yml"))
##games = [Game(**setting) for setting in settings['games']]
##
##grouper = settings['games'][0]['grouper'][0]
####[('root', '.*', [('TDM', '$TDM')])]
####{'root': '.*', 'childs':{'TDM': '/TDM'}}
####for d in quakelive.copy():
####    print d
####    for p in d.screenShots:
####            print "\t", p
##
##def group(grouper, name):
##    #print grouper, name
##    if grouper != None:
##        for folder in grouper:
##            if re.search(grouper[folder]['v'], name):
##                #print "Match", grouper[folder]['v']
##                return folder + "/" + group(grouper[folder]['c'], name)
##    return ""
