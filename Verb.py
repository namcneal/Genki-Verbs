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
                           u"ぐ" : u"げる"}

            return self.dict[:-1] + all_endings[ending]
                           

        # Irregular
        else:
            all_possible = {u"いく" : u"いける",
                            u"する" : u"できる",
                            u"くる" : u"こられる"
                            }
            return all_possible[self.dict]

    def causative(self):
        # Ichidan
        if self.group == "ru":
            return self.dict[:-1] + u"させる"

        #Godan
        elif self.group == 'u':
            ending = self.dict[-1]

            all_endings = {u"う" : u"わせる",
                           u"つ" : u"たせる",
                           u"る" : u"らせる",
                           u"む" : u"ませる",
                           u"ぶ" : u"ばせる",
                           u"ぬ" : u"なせる",
                           u"す" : u"させる",
                           u"く" : u"かせる",
                           u"ぐ" : u"がせる"}

            return self.dict[:-1] + all_endings[ending]
                           

        # Irregular
        else:
            all_possible = {u"いく" : u"いかせる",
                            u"する" : u"させる",
                            u"くる" : u"こさせる"
                            }
            return all_possible[self.dict]
        

