from Persona import Persona
import unittest

class TestPersona(unittest.TestCase):
	def setUpClass():
		print("Comenzando clase...")
	def setUp(self):
		print("Comenzando...")
	def test_persona_str(self):
		print("Testing...")
	def test_persona_other(self):
		print("Testing...")
	def tearDown(self):
		print("Finalizando...")
	def tearDownClass():
		print("Finalizando clase...")

unittest.main()