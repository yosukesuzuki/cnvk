# -*- coding: utf-8 -*-

import cnvk

from nose.tools import *


def test_zen_to_han_alpha():
    eq_(u'abcdefghijklmnopqrstuvwxyz', cnvk.convert(u'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ', cnvk.H_ALPHA))
