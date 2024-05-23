import pytest

import chaptertools

def test_first():
    txt = 'hello'
    result = chaptertools.simple_header_spacer(txt)
    assert result == txt

def test_first():
    data = [
['''
hello
=====
weee
    ''',
'''
hello
=====

weee
    '''],

['''
=====
hello
=====
weee
    ''',
'''
=====
hello
=====

weee
    '''],

['''
Is thistitle
hello
-----
weee
    ''',
'''
Is thistitle
hello
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

]
    for txt, expected in data:
        result = chaptertools.simple_header_spacer(txt)

        assert result == expected

