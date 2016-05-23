#! /usr/bin/env python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from sikulitool.sikuli import *
    s = Screen()

    s.dragDrop("as.png", "dir.png")
    s.sleep(0.5)
    s.dragDrop("qq.png", "dir.png")

    s.find("dir.png").highlight().sleep(1).doubleClick()

    for i in s.findAll(Pattern('doc.png').similar(0.5)):
        i.highlight().sleep(1).hover()



