'''
Created on 2013-04-01

@author: Nich
'''
import os
import unittest
from pynlg.realizer import Clause, NounPhrase, PrepositionalPhrase, VerbPhrase, NounConjunction
from pynlg.lexicon import Word, XMLLexicon, Noun, Determiner, Adjective

class Test(unittest.TestCase):


    def setUp(self):
        #A young girl with red hair and green eyes is sitting in one of three chairs by the fireplace in the northern part of this room.

        lex_path = os.path.join(os.path.dirname(__file__), '../../res/default-lexicon.xml')
        lex = XMLLexicon(lex_path)
        self.lex = lex

        self.np_a_young_girl = NounPhrase(lex.getWord("girl"), determiner = lex.getWord("a"), adjectives=[lex.getWord("young")])
        self.np_red_hair = NounPhrase(lex.getWord("hair"), adjectives=[lex.getWord("red", "ADJECTIVE")])
        self.np_glasses = NounPhrase(lex.getWord("glasses"))
        
        
        self.pp_with_red_hair_and_glasses = PrepositionalPhrase(lex.getWord("with"), [self.np_red_hair, self.np_glasses])
        
        self.np_the_fire = NounPhrase(lex.getWord("fire", "NOUN"), determiner=lex.getWord("the"))
        self.pp_by_the_fire = PrepositionalPhrase(lex.getWord("by", "PREPOSITION"), [self.np_the_fire])
        
        self.np_a_young_girl_with_red_hair_and_glasses = NounPhrase.from_nounphrase(self.np_a_young_girl, prepositional_phrases = [self.pp_with_red_hair_and_glasses])
        
        self.vp_is_sitting = VerbPhrase(lex.getWord("sit"), tense="present_progressive")
        
        self.vp_is_sitting_by_the_fire = VerbPhrase(lex.getWord("sit"), tense="present_progressive", prepositional_phrases = [self.pp_by_the_fire])
        
        self.np_a_young_girl_with_red_hair_and_glasses_is_sitting  = Clause(self.np_a_young_girl_with_red_hair_and_glasses, self.vp_is_sitting)
        
        
        self.np_a_young_girl_with_red_hair_and_glasses_is_sitting_by_the_fire  = Clause(self.np_a_young_girl_with_red_hair_and_glasses, self.vp_is_sitting_by_the_fire) 
        
        
        
    
    def testYoungGirl(self):
        self.assertEqual("a young girl", self.np_a_young_girl.realize())
    
    
    def testWithRedHairAndGlasses(self):
        self.assertEqual("with red hair and glasses", self.pp_with_red_hair_and_glasses.realize())
    
    
    def testYoungGirlWithRedHairAndGlasses(self):
        self.assertEqual("a young girl with red hair and glasses", self.np_a_young_girl_with_red_hair_and_glasses.realize())

    def testYoungGirlWithRedHairAndGlassesIsSitting(self):
        self.assertEqual("a young girl with red hair and glasses is sitting", self.np_a_young_girl_with_red_hair_and_glasses_is_sitting.realize())
    
    def testByTheFire(self):
        self.assertEqual("by the fire", self.pp_by_the_fire.realize())
        
    def testYoungGirlWithRedHairAndGlassesIsSittingByTheFire(self):
        self.assertEqual("a young girl with red hair and glasses is sitting by the fire", self.np_a_young_girl_with_red_hair_and_glasses_is_sitting_by_the_fire.realize())
        
    
    def testConjunction(self):
        nc = NounConjunction([self.np_a_young_girl, self.np_the_fire])
        self.assertEqual("a young girl and the fire", nc.realize())

        nc2 = NounConjunction([self.np_the_fire, self.np_a_young_girl])
        self.assertEqual("the fire and a young girl", nc2.realize())

        nc3 = NounConjunction([self.np_the_fire, self.np_a_young_girl, self.np_red_hair])
        self.assertEqual("the fire, a young girl, and red hair", nc3.realize())  
        
        nc1 = NounConjunction([self.np_the_fire])
        self.assertEqual("the fire", nc1.realize())


    def test_number(self):
        self.np_the_fire.set_number(5)
        self.assertEqual("the five fires", self.np_the_fire.realize())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()