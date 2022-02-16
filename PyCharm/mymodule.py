#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def first(tip):
    def second(spisok):
        if tip == list:
            return list(map(int, spisok.split()))
        return tuple(map(int, spisok.split()))

    return second

