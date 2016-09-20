# -*- coding: utf-8 -*-

import cnvk

from nose.tools import *


def test_zen_to_han():
    eq_(u'abcdefghijklmnopqrstuvwxyz', cnvk.convert(u'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ', cnvk.H_ALPHA))
    eq_(u'abcdefghijklmnopqrstuvwxyz1234567890', cnvk.convert(u'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０',
        cnvk.H_ALPHA, cnvk.H_NUM))
