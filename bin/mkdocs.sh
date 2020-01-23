#. /home/pbrian/venvs/devmanual/bin/activate

## This is the *production* process for the book
## 
## ref: https://digitalsuperpowers.com/blog/2019-02-16-publishing-ebook.html

BOOKNAME=TheSoftwareMind

# Get back out of bin
cd ..
REPODIR=`pwd`
echo "Run PreProcess"
#prepare by putting it all in one big file
python $REPODIR/bin/preprocess.py docs/index.pre

echo "Make Sphinx Docs"
cd $REPODIR/docs/
make clean
make html
make latex
cd $REPODIR/docs/_build/latex
pdflatex --interaction=nonstopmode $BOOKNAME.tex

#I expect to run this in a docker instacne on my laptop
#so i need to run it on here like a server

cd $REPODIR/docs
wordcount=`cat index.rst | wc -w`

echo "Run post Process (build marketing site)"
#build it as a book marketring site
cd $REPODIR/
python $REPODIR/bin/postprocess.py

# prep as a zip file to mail to work for printing
zip /var/data/book.zip docs/_build/latex/TheSoftwareMind.pdf

echo "############################################"
echo "Wordcount: $wordcount"
echo "Book zipped onto data dir"
