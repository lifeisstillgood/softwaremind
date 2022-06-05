import docutils.nodes
import docutils.parsers.rst
import docutils.utils
import docutils.frontend

def parse_rst(text: str) -> docutils.nodes.document:
    parser = docutils.parsers.rst.Parser()
    components = (docutils.parsers.rst.Parser,)
    settings = docutils.frontend.OptionParser(components=components).get_default_values()
    document = docutils.utils.new_document('<rst-doc>', settings=settings)
    parser.parse(text, document)
    return document

class MyVisitor(docutils.nodes.NodeVisitor):

    def visit_reference(self, node: docutils.nodes.reference) -> None:
        """Called for "reference" nodes."""
        print(node)

    def unknown_visit(self, node: docutils.nodes.Node) -> None:
        """Called for all other node types."""
        pass

def myparse():
    s = ''
    f = '../docs/conceptchapters/introduction.rst'
    #f = 'foo.txt'
    with open(f) as fo:
        s = fo.read()
    doc = parse_rst(s)
    visitor = MyVisitor(doc)
    return doc, visitor

if __name__ == '__main__':
    d,v = myparse()
    for x in d.ids:
        print(x)
