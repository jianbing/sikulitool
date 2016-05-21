#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from sikulitool import autoclass, GetSystemMetrics
import time


class Region(object):
    def __init__(self, x, y, w, h):
        self._region = autoclass('org.sikuli.script.Region')(x, y, w, h)

    def click(self, target=None):
        if target:
            self._region.click(target)
        else:
            self._region.click()

    def hover(self, target=None):
        if target:
            self._region.hover(target)
        else:
            self._region.hover()

    def sleep(self, secs):
        time.sleep(secs)

    def doubleClick(self, target=None):
        if target:
            self._region.doubleClick(target)
        else:
            self._region.doubleClick()

    def rightClick(self, target):
        self._region.rightClick(target)

    def dragDrop(self, from_, to_):
        self._region.dragDrop(from_, to_)

    def exists(self, target, timeout=1.0):
        if not self._region.exists(target, timeout):
            return False
        else:
            return True

    def wait(self, target, timeout=1.0):
        try:
            self._region.wait(target, timeout)
        except Exception as e:
            return False
        else:
            return True

    def waitVanish(self, target, timeout=5.0):
        return self._region.waitVanish(target, timeout)

    def getLastMatch(self):
        return Match(self._region.getLastMatch())

    def find(self, target):
        return Match(self._region.find(target))

    def findAll(self, target):
        _iter = self._region.findAll(target)
        while _iter.hasNext():
            yield Match(_iter.next())

    def highlight(self):
        self._region.highlight()

    def type(self, astr):
        self._region.type(astr)

    def pressKey(self, key):
        self._region.keyDown(key)
        self._region.keyUp(key)


class Match(object):
    def __init__(self, match_obj):
        self._match = match_obj

    def hover(self):
        self._match.hover()
        return self

    def click(self):
        self._match.click()
        return self

    def highlight(self):
        self._match.highlight()
        return self

    def sleep(self, secs):
        time.sleep(secs)
        return self

    def type(self, astr):
        self._match.type(astr)
        return self


class Pattern(object):
    def __init__(self, target):
        self._pattern = autoclass('org.sikuli.script.Pattern')(target)

    def similar(self, sim=0.7):
        return self._pattern.similar(sim)


class Screen(Region):
    def __init__(self):
        super(Screen, self).__init__(0, 0, GetSystemMetrics(0), GetSystemMetrics(1))


class Key(object):
    BackSpace = 8
    Enter = 13






