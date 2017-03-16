# -*- coding: utf-8 -*-
import unicodecsv as csv
import numpy as np

def import_verb_list(list_csv):
    verb_list = csv.reader(open(list_csv),encoding='utf-8')
    next(verb_list, None)
    return verb_list

def get_verb_array(list_of_chapters,u=True,ru=True,irr=True):
    full_list = list()
    for chapter in list_of_chapters:
        for row in import_verb_list("Verbs//genki_verbs_chapter_%s.csv" %chapter):
            row = np.array(row)
            full_list.append(row)

    full_array = np.vstack(full_list)
    indices = list()
    if u:
        indices  += list(np.array(np.where(full_array[:,2] == u"u")).reshape(-1,))
    if ru:
        indices += list(np.array(np.where(full_array[:,2] == u"ru")).reshape(-1,))
    if irr:
        indices +=  list(np.array(np.where(full_array[:,2] == u"i")).reshape(-1,))
    
    selected_verbs = full_array[indices]
    return list(selected_verbs)


