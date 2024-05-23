#!/usr/bin/env python
"""
chaptertools


Usage:
  chaptertools.py build_book [--firstpara]
  chaptertools.py show_chapters
  chaptertools.py foo
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

ROOTPATH='/home/pbrian/projects/softwaremind/docs/newbook'
BACKUPLOCATION="/tmp/chaptertools/"




def parse_doc(doc_txt, filename):
    from docutils import frontend, utils
    from docutils.parsers.rst import Parser
    settings = frontend.get_default_settings(Parser)
    document = utils.new_document(filename, settings)
    Parser().parse(doc_txt, document)
    nodestrings = document.pformat() 
    st = nodestrings.find("<paragraph>")
    ed = nodestrings.find("<paragraph>", st+1)
    firstpara = nodestrings[:ed].replace("<paragraph>","")

    return firstpara

def first_para(txt, numparas=3):
    
    paras = txt.split("\n\n")
    returnable_paras = paras[:numparas-1]
    returnstr = '\n\n'.join(returnable_paras)
    return returnstr

def show_chapters():
    filesd = find_all_chapters()
    for file, paras in filesd.items():
        print("<<<" + file + ">>>\n")
        #print(first_para(paras))
        #print("###############\n\n")

def find_all_chapters(firstpara=False):
    rootdir = '/home/pbrian/projects/softwaremind/docs/newbook'

    filesd = {}
    for f in sorted(os.listdir(rootdir)):
        if f.startswith('.'): continue
        try:
            txt = open(os.path.join(rootdir,f), encoding='utf-8').read()
            if firstpara:
                txt = first_para(txt)
            filesd[f] = txt

        except Exception as e:
            print(e, f)
            raise

    return filesd

def build_one_pager(firstpara=False):
    """Build a single page by combining lots of files """
    all_chaptersd = find_all_chapters(firstpara=firstpara)
    with open('/home/pbrian/projects/softwaremind/docs/index.pre') as fo:
        introtext = fo.read()
    outputtext = ''

    
    tgtfilepath = '/home/pbrian/projects/devmanual/all.txt'
    html = ''
    toc = ''

    for line in introtext.split("\n"):
        if line.startswith("<<<"):
            filetoken = line.strip().replace("<<<","").replace(">>>","")
            replacetext = all_chaptersd.get(filetoken, f"NOTFOUND-{filetoken}")
            outputtext += '\n.. ' + line + "\n\n"  
            outputtext += replacetext + "\n"
            outputtext += '\n.. ' + line + "\n\n"
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

#    shutil.copyfile(filepath,
#                    os.path.join(BACKUPLOCATION,
#                    os.path.basename(filepath)) )
    #: get text
    txt = open(filepath).read()
    try:
        newtxt = fn.__call__(txt)
    except Exception as e:
        print(e)
        import pdb; pdb.set_trace()

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

# work direct on text?
def simple_header_spacer(txt):
    """Given text, ensure a --- or === has blank line after it """
    newtxt = ''
    previousline = None
    thisline = None
    import pdb;pdb.set_trace()
    for line in txt.split("\n"):
        previousline = thisline
        thisline = line
        if not previousline: continue
        if previousline.endswith("===") or previousline.endswith("---"):
            if thisline.strip() == '': # ie  blank line, so thats good
                thisline = thisline
            elif len(thisline) == len(previousline):
                thisline = thisline  #BEst guess as double header
            else:
                previousline += "\n"
        newtxt += previousline + "\n"
    #finally
    newtxt += thisline
    return newtxt

############################ end


if __name__ == '__main__':
    args = docopt(__doc__)
    firstpara = args['--firstpara']
    if args['build_book']:
        build_one_pager(firstpara=firstpara)
    elif args['show_chapters']:
        show_chapters()
    elif args['foo']:
        walk_apply(simple_header_spacer)
