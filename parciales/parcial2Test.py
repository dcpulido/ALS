import unittest
import parcial2

class parcial2Test(unittest.TestCase):
 def setUp(self):
 	self.p1 = parcial2.Pieza(1, "p1")
 	self.p2 = parcial2.Pieza(2, "p2")

 def test_get(self):
 	name = self.p1.nombre
 	self.assertEqual(name,"p1")

if __name__ == "__main__":
 unittest.main()