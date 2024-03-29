#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-pi-main.
# https://github.com/easyNav/easyNav-pi-main.git

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org

from preggy import expect

from easyNav_pi_main import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal("0.1.0")
