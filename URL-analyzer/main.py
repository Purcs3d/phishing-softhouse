#!/usr/bin/env python
# -*- coding: utf-8 -*-
import src.algorithmManager as am


def main():
    #Website
    URLstring = "https://cloud.timeedit.net/bth/web/sched1/ri1f6X615XZZYYQv6X0661Z0yQY5554531QQ255Q6Y7Y7375ul03x55332YY15X5X643563.html"

    #URL-analyzing
    ex = am.algorithmManager(URLstring) #create object
    ex.printMsg()
    print("Is website fishy?",ex.run())


if __name__ == '__main__':
    main()
