import mindmeld
import unittest
import mapping

class TestAll(unittest.TestCase):
    
    def testlewi(self):
        res = mindmeld.calculate('19730424')
        print res
        self.assertTrue(22 in res['lewi'])
        self.assertTrue(167 in res['lewi'])
        self.assertEquals(30,res['millman'][0])
        self.assertTrue('Ox' in res['chinese'])
        self.assertTrue('Capricorn' in res['spiller'])
        res = mindmeld.get_lewi('19730424')
        self.assertTrue('22' in res)
        self.assertTrue('167' in res)        
        
    def testmap(self):
        m = mapping.init()
        self.assertEquals(m.ix['mo','tick']['ven'],146)
        self.assertEquals(m.ix['sun','*']['ur'],176)
        self.assertEquals(m.ix['mar','sq']['ur'],225)

    def testmbti(self):
        input = [1,1,1,0,1,0,1,
                 1,1,0,-1,1,1,-1,
                 1,1,0,-1,-1,1,-1,
                 1,1,1,-1,-1,0,-1,
                 1,0,1,0,1,1,-1,          
                 1,-1,1,-1,-1,1,1,
                 1,-1,1,1,-1,-1,1,
                 1,1,-1,-1,1,-1,1,
                 -1,-1,-1,1,-1,-1,0,
                 -1,-1,-1,1,1,1,-1]

        self.assertEquals('INTP',mindmeld.calculate_mb(input))
        
    def testmbtiaccess(self):
        self.assertEquals(mindmeld.mbti['infp'][3],'te')


    def testbad(self):
        res = mindmeld.calculate('19290925')
        print res['spiller']
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAll)
    unittest.TextTestRunner(verbosity=2).run(suite)
