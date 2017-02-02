# -*- coding: utf-8 -*-
# Copyright 2017 Christoph Reiter
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

import sys

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def test_gtk():
    window = Gtk.Window(title="foo")
    window.show()
    assert window.get_title() == "foo"
    window.destroy()


def test_locale():
    assert sys.getfilesystemencoding().upper() == "UTF-8"
