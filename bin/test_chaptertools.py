import pytest

import chaptertools

data = [
['''
wibble
hello1
======
weee
''',
'''
wibble
hello1
======

weee
'''],

['''
=====
hello2
=====
weee
    ''',
'''
=====
hello2
=====

weee
    '''],
#really I dont wanst this but thats a lot of worl
['''
Is thistitle
hello3
-----
weee
    ''',
'''
Is thistitle
hello3
-----

weee
    '''],

['''
now everything must be much more explicit.

The code is the design
=========================
foo
    ''',
'''
now everything must be much more explicit.

The code is the design
=========================

foo
    '''],

['''
now everything must be much more explicit.

The code is the design
=========================

foo
    ''',
'''
now everything must be much more explicit.

The code is the design
=========================

foo
    '''],


]




def test_first():

    for txt, expected in data:
        result = chaptertools.simple_header_spacer(txt)

        assert result == expected

wordwrap_data= [
['======\n\nthisis line',
 '======\n\nthisis line'],
['''Hello \n this is a paragrapah\n with several lines\n that must be broken
into 80 char lines correctly\n even with lots of breaks in it\n because thats
\n\n
the correct way of looking at things even if I keep typing till\n I hit a
whole sentence that is liner than 8 chars I am going to have to break that as
best I can ok make sense''',

'''Hello  this is a paragrapah with several lines that must be broken into 80 char
lines correctly even with lots of breaks in it because thats

the correct way of looking at things even if I keep typing till I hit a whole
sentence that is liner than 8 chars I am going to have to break that as best I
can ok make sense''']
    ]

def test_wordwrap():
    para = '''HELLO
lkfjdljflksdjf
fds sfd dhfsjdh
sdjfhskj sdfjh
sdjfhkdshfsjhsd
sdfkhsdjkdsf
hkdsfhkj dskfh '''

    expected = 'HELLO lkfjdljflksdjf fds sfd dhfsjdh sdjfhskj sdfjh sdjfhkdshfsjhsd sdfkhsdjkdsf\nhkdsfhkj dskfh '
    val = chaptertools.wrappara(para)

    assert val == expected
    for txt, expected in wordwrap_data:
        result = chaptertools.wordwrapper(txt)
        assert result == expected

