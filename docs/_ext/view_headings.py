
'''

Sphinx - the missing manual
---------------------------

I am writing a book (or two), and using `Sphinx` to do the heavy
lifting of layout etc for me.  But as a good hacker, I want to dive
below the surface - to get hold of the tree of nodes that docutils
creates, to extract my own meaning, help me understand my layout and
so forth.

We start with a simple traversal:

We are going to add an extension (this is the general term for any 
thing that is custom built and used by us to do something)

* we need to 

1. write the extension code (must have a `setup` function)
2. save the file in `_ext` folder, in the sphinx dir (next to conf.py)
3. tell conf.py to load that code
4. run `make`

Simplest possible atom of usefulness
------------------------------------

List all the sections in our book
Once the doctree has been fully processed, grab it and walk it and 
print out each section name.





Biblio
------
https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html
https://www.sphinx-doc.org/en/master/extdev/index.html#dev-extensions
https://docutils.readthedocs.io/en/sphinx-docs/dev/hacking.html

Nota Bene
---------

I generally use `sphinx` to refer to an eco-system of text
manipulation and layout tools that goes back genuinely decades.
Sphinx build heavily on Python's `docutils`, I use charts, image
processing and my final book output leans on, of course, `LaTex` and
`Tex` to get anywhere.  I find that trying to remember and explicitly
call out which component does what at any point in time takes away
from the main point I am making in the text - and so everything gets
lumped under `Sphinx`.

'''

import json
import docutils
import sphinx.util.nodes
from pprint import pprint as pp

def main():
    pass

def write_out(msg):
    with open('foo.txt', 'a') as fo:
        fo.write(msg)
        fo.write("\n")
    

def doctree_resolved(app, doctree, docname):
    if docname != "index": return
    s = ''
    s += docname + "\n"
    for section in doctree.traverse(docutils.nodes.section):
#        print(section.starttag, section.tagname)
        title = section.next_node(docutils.nodes.Titular)
        if title:
#            print("--------------------")
            s += "    " + title.astext() + "\n"
#            print("--------------------")            
#            pp(dir(title))
#            print("--------------------")            
    write_out(s)
    
def setup(app):
    app.connect('doctree-resolved', doctree_resolved)

    
if __name__ == '__main__':
    main()
