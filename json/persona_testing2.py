from Persona import Persona
import unittest

class TestPersona(unittest.TestCase):

	def test_persona_str(self):
		self.assertEqual("Baltasar18",str(Persona("Baltasar",18)))

	def test_persona_edad(self):
		p=Persona("Baltasar",18)
		self.assertEqual(18,p.edad)

if __name__ == "__main__":
	unittest.main()