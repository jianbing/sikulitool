#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys


if sys.platform == 'win32':
    separator = ';'
else:
    separator = ':'

sikuli_jar = os.path.join(separator + os.path.dirname(os.path.realpath(__file__)), "sikulixapi.jar")

if 'CLASSPATH' not in os.environ:
    os.environ['CLASSPATH'] = sikuli_jar
else:
    os.environ['CLASSPATH'] += sikuli_jar

from jnius import autoclass
