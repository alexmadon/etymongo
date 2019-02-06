#!/usr/bin/python3
# https://tomassetti.me/parsing-in-python/
# https://github.com/alexmadon/atpic_photosharing/blob/master/python/atpic/queryparser.py

from pyparsing import *


astring="""LATIN:primus(EN:first) + INDO:*KAP(FR:prendre,attraper)>LATIN:capere(EN:take)
>LATIN:princeps,princip(EN:first,chief,sovereign)
>OLDFRENCH:prince
>MIDDLEENGLISH:prince
>EN:prince"""
