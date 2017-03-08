# -*- coding: utf-8 -*-
import unicodecsv as csv

def import_verb_list(list_csv):
    verb_list = csv.reader(open(list_csv),encoding='utf-8')
    next(verb_list, None)
    return verb_list
