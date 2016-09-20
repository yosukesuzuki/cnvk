# -*- coding: utf-8 -*-

import cnvk

from nose.tools import *


def test_zen_to_han():
    eq_(u'abcdefghijklmnopqrstuvwxyz', cnvk.convert(u'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ', cnvk.H_ALPHA))
    eq_(u'abcdefghijklmnopqrstuvwxyz1234567890', cnvk.convert(u'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ１２３４５６７８９０',
        cnvk.H_ALPHA, cnvk.H_NUM))


def test_zen_to_han_custom():
    custom_rule = (
        (u'．', u'.'), (u"，", u","), (u"：", u":"), (u"；", u";"), (u"’", u"'"),
        (u"”", u'"'), (u"／", u"/"), (u"＝", u"="), (u"＆", u"&"), (u"＠", u"@"),
        (u"％", u"%"),
        )
    eq_(u'abc123.,:;\'"/=&@%？！（）', cnvk.convert(u'ａｂｃ１２３．，：；’”／＝＆＠％？！（）', cnvk.H_ALPHA, cnvk.H_NUM, custom_rule))
