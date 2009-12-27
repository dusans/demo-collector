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

    def __str__(self):
        return "<Demo: name: %s, startDate: %s, endDate: %s>" % (self.name, self.startDate, self.endDate)

    def hasShots(self):
        return len(self.screenShots) > 0

    def getScreenShots(self, screenShots):
        return [s for s in screenShots if self.startDate < s.date < self.endDate - 15 ]

class ScreenShot:
    def __init__(self, path):
        self.path = path
        self.name = ".".join(re.split('\\\\|/', path)[-1].split(".")[:-1])
        self.ext =  re.split('\\\\|/', path)[-1].split(".")[-1]
        self.date = os.stat(path).st_ctime

    def __str__(self):
        return "<ScreenShot: name: %s, date: %s>" % (self.name, self.date)

class Game():
    def __init__(self, name, demoFolder, screenShotFolder, outputFolder, gameDemoExt):
        self.name = name
        self.demoFolder = demoFolder
        self.screenShotFolder = screenShotFolder
        self.outputFolder = outputFolder
        self.gameDemoExt = gameDemoExt
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
                return False
        return True

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

    def getScreenShots(self):
        self.screenShots = [ScreenShot("%s/%s" % (self.screenShotFolder, s)) for s in os.listdir(self.screenShotFolder)]

    def getDemos(self):
        demos = [d for d in os.listdir(self.demoFolder) if d.endswith(self.gameDemoExt)]
        demos = [Demo("%s/%s" % (self.demoFolder, d), self.screenShots) for d in demos]
        self.demos = [d for d in demos if d.endDate > self.lastCopyDate]

    def setCounterAndDate(self):
        open(self.countFile, "w").write(str(self.counter))
        open(self.lastCopyDateFile, "w").write(str(datetime.datetime.now()))


    def setup(self):
        if self.test():
            self.getLastCopyDate()
            self.getCounter()
            self.getScreenShots()
            self.getDemos()

    def copy(self):
        for d in self.demos:
            if d.hasShots():
                #print "Copy %s" % d
                deltas = []
                # Copy screenShots
                for s in d.screenShots:
                    #print "Copy", s
                    delta = s.date - d.startDate
                    delta = datetime.time(minute=int(delta/60), second=int(delta%60))
                    shutil.copyfile(s.path, "%s/%s-%s__%s__.%s" % (self.outputFolder, self.counter, d.name, delta.strftime("%M.%S"), s.ext))
                    deltas.append(delta.strftime("%M.%S"))
                # Copy demo
                yield d
                shutil.copyfile(d.path, "%s/%s-%s__%s__.%s" % (self.outputFolder, self.counter, d.name, "_".join(deltas), d.ext))
                self.counter += 1
        # After copy set counter and date files
        self.setCounterAndDate()


#-------------------------------------------------------------------------------
# TEST
#-------------------------------------------------------------------------------
##name = "quakelive"
##demoFolder = "c:/Documents and Settings/Dule/Application Data/id Software/quakelive/home/baseq3/demos/"
##screenShotFolder = "c:/Documents and Settings/Dule/Application Data/id Software/quakelive/home/baseq3/screenshots/"
##outputFolder = "d:/dev/pyGameDemoCollector/output/"
##gameDemoExt = "dm_73"
##
##quakelive = Game(name, demoFolder, screenShotFolder, outputFolder, gameDemoExt)
##
##
##for d in quakelive.copy():
##    print d
##    for p in d.screenShots:
##            print "\t", p

