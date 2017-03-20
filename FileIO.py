# -*- coding: utf-8 -*-
import unicodecsv as csv
import numpy as np
from Verb import Verb
import wave
import pyaudio

def import_verb_list(list_csv):
    verb_list = csv.reader(open(list_csv),encoding='utf-8')
    next(verb_list, None)
    return verb_list

def get_verb_array(list_of_chapters,u=True,ru=True,irr=True):
    selected_verbs = list()
    for chapter in list_of_chapters:
        for row in import_verb_list("Verbs//genki_verbs_chapter_%s.csv" %chapter):
            if u and row[2] == u"u":
                selected_verbs.append(Verb(*row))
            if ru and row[2] == u"ru":
                selected_verbs.append(Verb(*row))
            if irr and row[2] == u"i":
                selected_verbs.append(Verb(*row))
    return selected_verbs

 
        



