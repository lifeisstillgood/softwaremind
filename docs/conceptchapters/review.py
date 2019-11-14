
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
    f = '/var/projects/softwaremind/docs/_build/json/conceptchapters/sm_software_literacy.fjson'
    with open(f, mode='rb') as fo:
        d = json.load(fo)
    print(d.keys())
    m = sphinx.util.nodes.NodeMatcher(sphinx.util.nodes.reference,
                                      refdomain='std',
                                      reftype='citation')
    x = d.traverse(m)
    print(x)
    
if __name__ == '__main__':
    main()
