# encoding: utf-8
import os
import sys
import unittest
import tkinter as tk
import tkinter.ttk as ttk

pygubu_basedir = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))
)
if pygubu_basedir not in sys.path:
    sys.path.insert(0, pygubu_basedir)

import pygubu
import support


class TestLabelframe(unittest.TestCase):
    def setUp(self):
        support.root_deiconify()
        xmldata = "test_labelframe.ui"
        self.builder = builder = pygubu.Builder()
        builder.add_from_file(xmldata)
        self.widget = builder.get_object("Labelframe")

    def tearDown(self):
        support.root_withdraw()

    def test_class(self):
        self.assertIsInstance(self.widget, ttk.Labelframe)
        self.widget.destroy()
