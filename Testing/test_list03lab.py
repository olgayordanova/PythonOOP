from List.extended_list import IntegerList
import unittest

class IntegerListTest(unittest.TestCase):

    def setUp(self):
        self.list = IntegerList([])

    def test_add(self):
        self.assertEqual ( self.list.add(5), [5])

    def test_add_raise_error(self):
        self.assertRaises ( ValueError,self.list.add, 'SomeValue')

    def test_remove_index(self):
        self.list.add(5)
        el =  self.list.remove_index(0)
        self.assertEqual ( el, 5 )

    def test_remove_raise_error(self):
        self.assertRaises ( IndexError, self.list.remove_index, 0)

    def test_init_only_integers(self):
        my_list = IntegerList(1, 'some value', 32, 'other value')
        self.assertEqual ( my_list.get_data(), [1, 32] )

    def test_get(self):
        self.list.add(5)
        self.assertEqual ( self.list.get(0), 5 )

    def test_get_index_raise_error(self):
        self.assertRaises ( IndexError, self.list.get, 0)

    def test_insert_indexerror(self):
        self.assertRaises ( IndexError, self.list.insert,0,5)

    def test_insert(self):
        self.list.add ( 5 )
        self.list.insert(0,3)
        self.assertEqual ( self.list.get_data(), [3, 5] )


    def test_insert_valueerror(self):
        self.list.add ( 5 )
        self.assertRaises ( ValueError, self.list.insert,0,'some value')

    def test_get_bigest(self):
        self.list.add ( 5 )
        self.list.add ( 8 )
        self.assertEqual ( self.list.get_biggest(), 8 )

    def test_get_index(self):
        self.list.add ( 8 )
        self.assertEqual ( self.list.get_index(8), 0 )

if __name__ == "__main__":
    unittest.main ()
