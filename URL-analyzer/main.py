#!/usr/bin/env python
# -*- coding: utf-8 -*-
import src.algorithmManager as am


def main():
    #Website
    URLstring = "https://www.sweclockers.com/nyhetsbrev"

    #URL-analyzing
    ex = am.algorithmManager(URLstring)
    print("Is website fishy?",ex.run())


if __name__ == '__main__':
    main()
