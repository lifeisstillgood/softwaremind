
'''mkdocs.sh will `make json` giving us a directory of json based
chapters that are html frags in json format.  It is OK as a form of
processing - I do want to look at emitters more at some point.

We get back a nodes.document
We can d.walk(visitor) the tree, but visitor needs to be a 
NodeVisitor object.

THis implies we know what we are trying to do - I think first is to get list of all H1???


'''

import json
import docutils
import sphinx.util.nodes

def main():
    pass

def doctree_resolved(app, doctree, docname):
    for section in doctree.traverse(docutils.nodes.section):
        title = section.next_node(docutils.nodes.Titular)
        if title:
            print(title.asText())

def setup(app):
    app.connect('doctree-resolved', doctree_resolved)

    
if __name__ == '__main__':
    main()
