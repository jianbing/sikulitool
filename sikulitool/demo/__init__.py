#! /usr/bin/env python
# -*- coding: UTF-8 -*-


if __name__ == '__main__':
    from sikulitool.sikuli import *
    s = Screen()
    print s.exists('pc.png')
    s.getLastMatch().hover()

