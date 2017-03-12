# -*- coding: utf-8 -*-

class Verb(object):
    def __init__(self, dictionary,kanji, group,meaning):
        self.dict = dictionary
        self.kanji = kanji
        self.group = group
        self.meaning = meaning

    def __unicode__(self):
		return u"%s(%s): %s"%(self.kanji, self.dict,self.meaning)
	
    def __str__(self):
		return self.__unicode__().encode("utf-8")

    ## Verb conjugation methods

    # Potential Form
    def potential(self):
        new_dict = u""
        new_kanji = u""
        new_meaning = u""

        # Ichidan
        if self.group == "ru":
            new_dict = self.dict[:-1] + u"られる"
            new_kanji = self.kanji[:-1] + u"られる"


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

            new_dict = self.dict[:-1] + all_endings[ending]
            new_kanji = self.kanji[:-1] + all_endings[ending]               
            
        # Irregular
        else:
            irregular_kana = {u"いく" : u"いける",
                              u"する" : u"できる",
                              u"くる" : u"こられる"
                             }
            irregular_kanji = {u"いく" : u"行ける",
                                u"する" : u"できる",
                              u"くる" : u"来られる"
                             }

            new_dict = irregular_kana[self.dict]
            new_kanji = irregular_kanji[self.dict]
        
        new_meaning = u"To be able " + self.meaning
        return Verb(new_dict, new_kanji, u"ru", new_meaning)
    

    # Passive Form
    def passive(self):
        new_dict = u""
        new_kanji = u""
        new_meaning = u""

        # Ichidan
        if self.group == "ru":
            new_dict = self.dict[:-1] + u"られる"
            new_kanji = self.kanji[:-1] + u"られる"

        #Godan
        elif self.group == 'u':
            ending = self.dict[-1]

            all_endings = {u"う" : u"われる",
                           u"つ" : u"たれる",
                           u"る" : u"られる",
                           u"む" : u"まれる",
                           u"ぶ" : u"ばれる",
                           u"ぬ" : u"なれる",
                           u"す" : u"される",
                           u"く" : u"かれる",
                           u"ぐ" : u"がれる"}
            new_dict = self.dict[:-1] + all_endings[ending]
            new_kanji = self.kanji[:-1] + all_endings[ending]

        # Irregular
        else:
            irregular_kana = {u"いく" : u"いかれる",
                              u"する" : u"される",
                              u"くる" : u"こられる"
                             }
            irregular_kanji = {u"いく" : u"行かれる",
                              u"する" : u"される",
                              u"くる" : u"来られる"
                             }
            new_dict = irregular_kana[self.dict]
            new_kanji = irregular_kanji[self.dict]
            
        new_meaning = self.meaning + " (passive)"
        return Verb(new_dict, new_kanji, u"ru", new_meaning)

    def causative(self):
        new_dict = u""
        new_kanji = u""
        new_meaning = u""

        # Ichidan
        if self.group == "ru":
            new_dict = self.dict[:-1] + u"させる"
            new_kanji = self.kanji[:-1] + u"させる"

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

            new_dict = self.dict[:-1] + all_endings[ending]
            new_kanji = self.kanji[:-1] + all_endings[ending]               

        # Irregular
        else:
            irregular_kana = {u"いく" : u"いかせる",
                              u"する" : u"させる",
                              u"くる" : u"こさせる"
                              }
            irregular_kanji = {u"いく" : u"行かせる",
                              u"する" : u"させる",
                              u"くる" : u"来させる"
                              }
            new_dict = irregular_kana[self.dict]
            new_kanji = irregular_kanji[self.dict] 

        new_meaning = self.meaning + u" (causative)"
        return Verb(new_dict, new_kanji, u"ru", new_meaning)

    def causative_passive(self):
        new_dict = u""
        new_kanji = u""
        new_meaning = u""

        # Ichidan
        if self.group == "ru":
            new_dict = self.dict[:-1] + u"させられる"
            new_kanji = self.kanji[:-1] + u"させられる"

        #Godan
        elif self.group == 'u':
            ending = self.dict[-1]

            all_endings = {u"う" : u"わされる",
                           u"つ" : u"たされる",
                           u"る" : u"らされる",
                           u"む" : u"まされる",
                           u"ぶ" : u"ばされる",
                           u"ぬ" : u"なされる",
                           u"す" : u"させられる",
                           u"く" : u"かされる",
                           u"ぐ" : u"がされる"}

            new_dict = self.dict[:-1] + all_endings[ending]
            new_kanji = self.kanji[:-1] + all_endings[ending]               

        # Irregular
        else:
            irregular_kana = {u"いく" : u"いかされる",
                              u"する" : u"させられる",
                              u"くる" : u"こさせられる"
                              }
            irregular_kanji = {u"いく" : u"行かせる",
                              u"する" : u"させる",
                              u"くる" : u"来させられる"
                              }
            new_dict = irregular_kana[self.dict]
            new_kanji = irregular_kanji[self.dict] 

        new_meaning = self.meaning + u" (causative-passive)"
        return Verb(new_dict, new_kanji, u"ru", new_meaning)



