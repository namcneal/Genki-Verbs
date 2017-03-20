# -*- coding: utf-8 -*-
import unicodecsv as csv, codecs, cStringIO

for num in range(3,25):
    new = open("genki_verbs_chapter_%d.csv" %num, "w+")
    writer = csv.writer(new)
    writer.writerow([u"﻿DictionaryKanji",u"DictionaryKana",u"Type",u"Meaning"])
    writer.writerow([u"行く",u"いく",u"u",u"to go%d" %num])
    writer.writerow([u"帰る",u"かえる",u"u",u"to return%d" %num])
    writer.writerow([u"食べる",u"たべる",u"ru",u"to eat%d" %num])
    writer.writerow([u"する",u"する",u"i",u"to do%d" %num])

