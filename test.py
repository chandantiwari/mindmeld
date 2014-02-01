import mindmeld
import unittest

class TestAll(unittest.TestCase):
    
    def testlewi(self):
        res = mindmeld.calculate('19730424')
        self.assertTrue('22' in res['lewi'])
        res = mindmeld.get_lewi('19730424')
        self.assertTrue('22' in res)
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAll)
    unittest.TextTestRunner(verbosity=2).run(suite)
