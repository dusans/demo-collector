import yaml
settings = yaml.load(open("../files/settings.yml"))

for game in settings['games']:
    print game['name']
    print game['demoFolder']
    try:
        print "Remove - %s/%s" % (game['demoFolder'], "lastCopy.date")
        os.remove("%s/%s" % (game['demoFolder'], "lastCopy.date"))
        print "Empty outputFolder"
        shutil.rmtree(game['outputFolder'])
        os.mkdir(game['outputFolder'])
    except:
        print "\tError"