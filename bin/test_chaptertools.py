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

