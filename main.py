# /bin/python3

import os
import subprocess
from strings import *
from termcolor import cprint


def checkStuff():
    i = 0
    output = " "
    if os.system(dockerVerCheck) ==0:
        verDict['dockerOK'] = True
        cprint("Docker is correctly installed", 'green')
    else:
        verDict['dockerOK'] = False
        cprint(dockerMissing, 'red')

    if os.system(npmVerCheck) ==0:
        verDict['npmOK'] = True
        cprint ("NPM is correctly installed", 'green')
    else:
        verDict['npmOK'] = False
        cprint(npmMissing, 'red')
    	
    if os.system(nodeVerCheck) ==0:
        verDict['nodeOK'] = True
        cprint ("NodeJS is correctly installed", 'green')
    else:
        verDict['nodeOK'] = False
        cprint(nodeMissing, 'red')

    for value in verDict.values():
        if value == False:
            i = i + 1

    if i == 0 :
        cprint ("Basic Dependencies are all there", 'green')
    else:
        cprint ("Basic Dependencies will be installed", 'red')


def installStuff():

    if verDict['dockerOK'] == False:
        try:
            os.system(installDocker)
        except:
            cprint("Something went wrong while installing Docker", 'red')
    if verDict['npmOK'] == False:
        try:
            os.system(installNpm)
        except:
            cprint("Something went wrong while installing NPM", 'red')

    if verDict['nodeOK'] == False:
        try:
            os.system(installNode)
        except:
            cprint("Something went wrong while installing Node JS", 'red')



def getContainers():
    print("Making Sure Docker Engine is running and enabled on reboot ..")
    if os.system(checkDocker) != 0:
        os.system(startDocker)
        os.system(enableDocker)
    else:
        print ("Downloading and Setting up Docker Containers..")
    os.system(getMySQL)
    os.system(getMongoDB)
    cprint("Containers are now up and running" 'green')

def downloadDVWS():
    os.system(getDVWS)

def installAndConfigurDVWS():
    os.system(installDVWSDependencies)

def runDVWS():
    os.system(startDVWS)
    cprint ("DVWS is now installed and running on localhost port 8000 ", 'green')
def clear():
    subprocess.call('clear')

def editDVWS():
    os.system(configPort)
    os.system(getSwagger)
    os.system(configSwagger)

def initializeDVWS():
    os.system(createTestDVWS)
def main():
    clear()
    cprint (introText, 'red')
    checkStuff()
    installStuff()
    getContainers()
    cprint("Now Downloading and configuring DVWS ..", 'green')
    downloadDVWS()
    installAndConfigurDVWS()
    initializeDVWS()
    editDVWS()
    runDVWS()


if __name__ == '__main__':
    main()



