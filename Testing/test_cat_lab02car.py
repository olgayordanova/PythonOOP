from cat_02_lab import Cat
import unittest

class CatTests(unittest.TestCase):

    def setUp(self):
        self.cat = Cat("Olga")

    def test_cat_initialized(self):
        self.assertEqual ( self.cat.name, "Olga" )


    def test_size_increased_after_eating(self):
        result = self.cat.size
        self.cat.eat()
        expected_result = self.cat.size
        self.assertEqual(result+1, expected_result)

    def test_fed_after_eating(self):
        self.fed = False
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cannot_eat_if_already_fed(self):
        self.cat.eat ()
        with self.assertRaises ( Exception ) as exp:
            self.cat.eat()
        self.assertEqual ( exp.exception.args[0], 'Already fed.' )

    def test_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises ( Exception ) as exp:
            self.cat.sleep()
        self.assertEqual ( exp.exception.args[0], 'Cannot sleep while hungry' )

    def test_cannot_sleepy_after_sleeping(self):
        self.cat.eat ()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()

# •	Cat is not sleepy after sleeping