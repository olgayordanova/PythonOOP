from mammal.project.mammal import Mammal
import unittest

class MammalTests(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal( "Katty", "cat", "meow")

    def test_mammal_initialized(self):
        self.assertEqual ( self.mammal.name, "Katty" )
        self.assertEqual ( self.mammal.type, "cat" )
        self.assertEqual ( self.mammal.sound, "meow" )

    def test_if_get_kingdom_method_is_private(self):
        result = self.mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual ( result, expected_result )

    def test_make_sound(self):
        self.assertEqual ( self.mammal.make_sound(), "Katty makes meow" )

    def test_get_kingdom(self):
        self.assertEqual ( self.mammal.get_kingdom (), "animals" )

    def test_info(self):
        self.assertEqual ( self.mammal.info(), "Katty is of type cat" )

if __name__ == "__main__":
    unittest.main()