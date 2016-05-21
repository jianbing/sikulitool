#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
from win32api import GetSystemMetrics

sikuli_jar = os.path.join(";" + os.path.dirname(os.path.realpath(__file__)), "sikulixapi.jar")

if 'CLASSPATH' not in os.environ:
    os.environ['CLASSPATH'] = sikuli_jar
else:
    os.environ['CLASSPATH'] += sikuli_jar

from jnius import autoclass

