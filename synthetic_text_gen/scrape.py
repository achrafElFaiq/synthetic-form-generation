from urllib.error import HTTPError
import re
import sys
import wget
import zipfile
import os
import shutil

'''This script is for scraping fonts of a specific stype from 1001fonts.com
    Usage: type-keyword num-pages start-page(optional)
'''

url ='http://www.1001fonts.com/{}-fonts.html?page={}&items={}' #tag,page,num on page
url_all ='http://www.1001fonts.com/?page={}&items={}' #tag,page,num on page

def moveEverythingToParentDirectory(parentDirectory, directory):
    while len(os.listdir(directory)) > 0:
        filename = os.listdir(directory)[0]
        if os.path.isdir(os.path.join(directory, filename)):
            moveEverythingToParentDirectory(directory, os.path.join(directory, filename))
        elif os.path.isfile(os.path.join(directory, filename)):
            os.rename(os.path.join(directory, filename), os.path.join(parentDirectory, filename))
    os.rmdir(directory)


def getFonts(typ,page,num,commercial=False):
    downloadURLs=[]
    try:
        if typ=='all':
            wordurl=url_all.format(page,num)
        else:
            wordurl=url.format(typ,page,num)
        print(wordurl)
        filename = wget.download(wordurl)
        with open(filename) as f:
            pp=f.read()
        if commercial:
            ms = re.findall('font-toolbar-wrapper.+?commercial use.+?href=([^"]*/[^/"]*\.zip)',pp)
            if len(ms)==0:
                ms = re.findall('font-toolbar-wrapper.+?commercial use.+?href="([^"]*/[^/"]*\.zip)"',pp)
        else:
            ms = re.findall('href=([^"]*/[^/"]*\.zip)',pp) #newline dependent
        for m in ms:
            downloadURL = 'http://www.1001fonts.com'+m
            downloadURLs.append(downloadURL)

        os.remove(filename)
    except HTTPError:
        print('failed for : ')
    for downloadURL in downloadURLs:
        try:
            filename = wget.download(downloadURL)
            print("\n", filename)
            with zipfile.ZipFile(filename, "r") as zip_ref:
                zip_ref.extractall("./tmp")
            os.remove(filename)
            while len(os.listdir('tmp')) > 0:
                filename = os.listdir('tmp')[0]
                f = os.path.join('./tmp', filename)
                if os.path.isdir(f):
                    moveEverythingToParentDirectory('./tmp', f)
                elif os.path.isfile(f) and not( (f.lower().endswith('.ttf')) or (f.lower().endswith('.otf')) or (f.lower().endswith('.woff')) ):
                    os.remove(f)
                else:
                    os.rename(f, '../data/fonts/'+filename)
        except Exception as e:
            if os.path.isfile(filename):
                os.remove(filename)
            elif os.path.isdir(filename):
                shutil.rmtree(filename)
            print(e)
            print('Couldnt download/unzip '+downloadURL)


typ = sys.argv[1]
count = int(sys.argv[2])
per = 10
start = int(sys.argv[3]) if len(sys.argv)>3 else 0

try:
    os.mkdir('tmp')
except FileExistsError:
    pass
try:
    os.mkdir('../data')
except FileExistsError:
    pass
try:
    os.mkdir('../data/fonts')
except FileExistsError:
    pass

for i in range(start,count):
    print('NEW PAGE ({}/{})'.format(i+1,count))
    getFonts(typ, i+1, per, True)

shutil.rmtree('./tmp')
