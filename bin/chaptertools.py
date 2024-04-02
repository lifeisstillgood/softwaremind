#!/usr/bin/env python
"""
chaptertools


Usage:
  chaptertools.py build_book
  chaptertools.py (-h | --help)
  chaptertools.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt
import os
import shutil
from pprint import pprint as pp
import docutils.core

ROOTPATH='/home/pbrian/projects/devmanual/docs'
BACKUPLOCATION="/tmp/chaptertools/"

def find_all_chapters():
    rootdir = '/home/pbrian/projects/softwaremind/docs/newbook'

    filesd = {}
    for f in os.listdir(rootdir):
        if f.startswith('.'): continue
        try:
            txt = open(os.path.join(rootdir,f), encoding='utf-8').read() 
            filesd[f] = txt
        except Exception as e:
            print(e, f)
            raise

    return filesd

def build_one_pager():
    """Build a single page by combining lots of files """
    all_chaptersd = find_all_chapters()
    with open('/home/pbrian/projects/softwaremind/docs/newbook/intro.rst') as fo:
        introtext = fo.read()
    outputtext = ''

    
    tgtfilepath = '/home/pbrian/projects/devmanual/all.txt'
    html = ''
    toc = ''

    for line in introtext.split("\n"):
        if line.startswith("<<<"):
            filetoken = line.strip().replace("<<<","").replace(">>>","")
            replacetext = all_chaptersd.get(filetoken, f"NOTFOUND-{filetoken}")
            outputtext += '.. ' + line + "\n"  
            outputtext += replacetext + "\n"
            outputtext += '.. ' + line + "\n"
        else:
            outputtext += line + "\n"


    fo = open(tgtfilepath, 'w')
    fo.write(outputtext)
    fo.close()
    import webbrowser;webbrowser.open(tgtfilepath)
    convert_onepager_to_html_publish(tgtfilepath)

def convert_onepager_to_html_publish(rst_filepath):
    rsttext = open(rst_filepath, encoding="utf-8").read()
    htmlfrag = build_html_body_from_rst(rsttext)
    f = '/home/pbrian/foo.html'
    with open(f, 'w') as fo:
        fo.write(htmlfrag)
    import webbrowser; webbrowser.open(f)


def build_html_body_from_rst(rst_fragment):
    '''
'''
    app_defaults = {'keep_warnings': True, 'halt_level': 5}
    #output = publish_string(..., settings_overrides=app_defaults)
    try:
        htmlfrag = docutils.core.publish_parts(rst_fragment, 
                                            writer_name='html',
                                            settings_overrides=app_defaults
                                            )['html_body']
    except Exception as e:
        htmlfrag = str(e)
    return htmlfrag




def mkdir_backup():
    try:
        os.makedirs(BACKUPLOCATION)
    except OSError:
        pass #ignore we want to recreate idempotent


def update_a_file(filepath, fn):
    """Grab the text in filepath, pass text to `fn` and write the result back to filepath
    """
    #: check exists
    if not os.path.isfile(filepath):
        raise Exception("File not found at {0}".format(filepath))
    #: backup file
    shutil.copyfile(filepath, os.path.join(BACKUPLOCATION, os.path.basename(filepath)))
    #: get text
    txt = open(filepath).read()
    try:
        newtxt = fn.__call__(txt)
    except Exception as e:
        print(e)

    fo = open(filepath, 'w')
    fo.write(newtxt)
    fo.close()

def walk_apply(fn):
    files_to_use = []
    notin = ['.git', '_build']
    for dirpath, dirnames, filenames in os.walk(ROOTPATH):
        for notintoken in notin:
            for dirname in dirnames:
                if dirname.find(notintoken) >= 0:
                    #get rid
                    dirnames.remove(dirname)

        for file in filenames:
            if file.endswith(".rst"):
                files_to_use.append(os.path.join(dirpath, file))
    for filepath in files_to_use:
        update_a_file(filepath, fn)

def run():
    """We want to backup our files (incase) and apply a fn to each file
    """
    mkdir_backup()
    walk_apply(mktitle)

def test():
    import doctest
    doctest.testmod()

############################ text altering functions to call
def clear_tokens(text):
    """
    >>> clear_tokens(':main fskjdkfjsdlkkfjsdlfj')
    ':main fskjdkfjsdlkkfjsdlfj'
    >>> clear_tokens(':mind fskjdkfjsdlkkfjsdlfj')
    ' fskjdkfjsdlkkfjsdlfj'
    """
    tokens = [':mind',]
    for token in tokens:
        if text[:len(token)] == token:
            text = text[len(token):]
    return text

def rmblankline(txt):
    firstline = txt.split("\n")[0]
    if firstline.strip() == '':
        newtxt = '\n'.join(txt.split("\n")[1:])
    else:
        newtxt = txt
    return newtxt

def mktitle(txt):
    newtxt = ''
    firstline = txt.split("\n")[0]
    if firstline.find("===") == 0:
        newtxt = txt
    else:
        newtxt = "="*len(firstline) + '\n'
        newtxt += firstline + '\n'
        newtxt += '='*len(firstline) + '\n'
        newtxt += txt[len(firstline):]
    return newtxt


############################ end


if __name__ == '__main__':
    args = docopt(__doc__)
    if args['build_book']:
        build_one_pager()
