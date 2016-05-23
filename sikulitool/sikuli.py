#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from sikulitool import autoclass
import time


class RegionMixin(object):

    def __init__(self):
        self._wrapper = None

    def click(self, target=None):
        if target:
            self._wrapper.click(target)
        else:
            self._wrapper.click()
        return self

    def hover(self, target=None):
        if target:
            self._wrapper.hover(target)
        else:
            self._wrapper.hover()
        return self

    def sleep(self, secs):
        time.sleep(secs)
        return self

    def doubleClick(self, target=None):
        if target:
            self._wrapper.click(target)
            self._wrapper.doubleClick(target)
        else:
            self._wrapper.click()
            self._wrapper.doubleClick()
        return self

    def rightClick(self, target):
        self._wrapper.rightClick(target)
        return self

    def dragDrop(self, from_, to_):
        self._wrapper.dragDrop(from_, to_)
        return self

    def exists(self, target, timeout=1.0):
        if not self._wrapper.exists(target, timeout):
            return False
        else:
            return True

    def wait(self, target, timeout=1.0):
        try:
            self._wrapper.wait(target, timeout)
        except Exception as e:
            return False
        else:
            return True

    def waitVanish(self, target, timeout=5.0):
        return self._wrapper.waitVanish(target, timeout)

    def getLastMatch(self):
        return Match(self._wrapper.getLastMatch())

    def find(self, target):
        return Match(self._wrapper.find(target))

    def findAll(self, target):
        _iter = self._wrapper.findAll(target)
        while _iter.hasNext():
            yield Match(_iter.next())

    def highlight(self):
        self._wrapper.highlight()
        return self

    def type(self, astr):
        self._wrapper.type(astr)
        return self

    def pressKey(self, key):
        self._wrapper.keyDown(key)
        self._wrapper.keyUp(key)
        return self


class Region(RegionMixin):
    def __init__(self, x, y, w, h):
        super(Region, self).__init__()
        self._wrapper = autoclass('org.sikuli.script.Region')(x, y, w, h)


class Screen(RegionMixin):
    def __init__(self):
        super(Screen, self).__init__()
        self._wrapper = autoclass('org.sikuli.script.Screen')()

# class Screen(Region):
#     def __init__(self):
#         super(Screen, self).__init__(0, 0, GetSystemMetrics(0), GetSystemMetrics(1))


class Match(RegionMixin):
    def __init__(self, match_obj):
        super(Match, self).__init__()
        self._wrapper = match_obj


class Pattern(object):
    def __init__(self, target):
        self._pattern = autoclass('org.sikuli.script.Pattern')(target)

    def similar(self, sim=0.7):
        return self._pattern.similar(sim)


class Key(object):
    BackSpace = 8
    Enter = 13






