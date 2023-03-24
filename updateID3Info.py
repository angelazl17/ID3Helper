from mutagen.easyid3 import EasyID3
import os


def updateTitle(filename,title):
    audio = EasyID3(filename)
    audio["title"] = title
    audio.save()

def updateAlbum(filename,album):
    audio = EasyID3(filename)
    audio["album"] = album
    audio.save()

def updateArtist(filename,artist):
    audio = EasyID3(filename)
    audio["artist"] = artist
    audio.save()

def getFileNameList(path):
    fileNamelist = os.listdir(path)
    return fileNamelist

def printFileNameList(fileNamelist):
    for x in fileNamelist:
        if x.endswith(".mp3"):
            # Prints only text file present in My Folder
            print(x)

def createNewFileName(oldFileName):
    newFileName=oldFileName.replace("添加微信：xy112271 新品免费领取","")\
        .replace("【起点视觉】","")
    return newFileName

def getFileFullName(path, fileName):
    return path + "/"+fileName

def getTitle(fileName):
    title=fileName.replace(".mp3","")
    return title

def processFile(path,album,artist):
    fileNamelist = os.listdir(path)
    for oldFileName in fileNamelist:
        if oldFileName.endswith(".mp3"):
            newFileName=createNewFileName(oldFileName)

            oldFullName=getFileFullName(path,oldFileName)
            newFullName=getFileFullName(path,newFileName)
            title=getTitle(newFileName)
            os.rename(oldFullName, newFullName)

            # Prints only text file present in My Folder
            print(oldFileName)
            updateAlbum(newFullName,album)
            updateTitle(newFullName,title)
            updateArtist(newFullName,artist)
def demo():
    filename = "./mp3/006齊物論02.mp3"
    title = u"006齊物論02"
    album = u"庄子"
    artist = u"JT叔叔"
    updateAlbum(filename, album)
    updateTitle(filename, title)
    updateArtist(filename, artist)
    path = "D:\mp3\百家讲坛\MP3版-JT叔叔(谭杰中)讲庄子"
    fileNamelist = getFileNameList(path)
    printFileNameList(fileNamelist)
    processFile(path, album, artist)

def main():


    album=u"汉武帝的三张面孔"
    artist=u"姜鹏"

    path="D:\\MP3\\百家讲坛\\12姜鹏《汉武帝的三张面孔》29集全"
    fileNamelist=getFileNameList(path)
    printFileNameList(fileNamelist)
    processFile(path,album,artist)


main()