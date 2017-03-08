# -*- coding: utf-8 -*-

class Verb(object):
    def __init__(self, dictionary,kanji, group,meaning):
        self.dict = dictionary
        self.kanji = kanji
        self.group = group
        self.meaning = meaning

    def potential(self):
        # Ichidan
        if self.group == "ru":
            return self.dict[:-1] + u"られる"

        #Godan
        elif self.group == 'u':
            ending = self.dict[-1]

            all_endings = {u"う" : u"える",
                           u"つ" : u"てる",
                           u"る" : u"れる",
                           u"む" : u"める",
                           u"ぶ" : u"べる",
                           u"ぬ" : u"ねる",
                           u"す" : u"せる",
                           u"く" : u"ける",
                           u"ぐ" : u"ける"}

            return self.dict[:-1] + all_endings[ending]
                           

        # Irregular
        else:
            all_possible = {u"いく" : u"いける",
                            u"する" : u"できる",
                            u"くる" : u"こられる"
                            }
            return all_possible[self.dict]

