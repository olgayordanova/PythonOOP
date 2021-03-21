from CarManager.car_manager import Car
import unittest

class CarTest(unittest.TestCase):

    def setUp(self):
        self.car = Car("a", "b", 1, 4)

    def test_car_initialized(self):
        self.assertEqual ( self.car.make, "a" )
        self.assertEqual ( self.car.model, "b" )
        self.assertEqual ( self.car.fuel_consumption, 1 )
        self.assertEqual ( self.car.fuel_capacity, 4 )

    def test_make_empty_exeption(self):
        with self.assertRaises ( Exception ):
            self.car.make=''

    def test_model_empty_exeption(self):
        with self.assertRaises ( Exception ):
            self.car.model=''

    def test_fuel_consumption_bz_exeption(self):
        with self.assertRaises ( Exception ):
            self.car.fuel_consumption=-1

    def test_fuel_capacity_bz_exeption(self):
        with self.assertRaises ( Exception ):
            self.car.fuel_capacity=-1

    def test_fuel_amount_belowzero_exeption(self):
        with self.assertRaises ( Exception ):
            self.car.fuel_amount=-1

    def test_refuel_lezero_exeption(self):
        with self.assertRaises ( Exception ):
            self.car.refuel(-1)

    def test_refuel_more_capacity(self):
        self.car.refuel(50)
        self.assertEqual ( self.car.fuel_amount, self.car.fuel_capacity )

    def test_refuel(self):
        amount = self.car.fuel_amount
        self.car.refuel(1)
        self.assertEqual ( amount+1, self.car.fuel_amount )

    def test_drive_more_than_fuel(self):
        with self.assertRaises ( Exception ) as exp:
            self.car.drive ( 1000 )
        self.assertEqual ( str(exp.exception), 'You don\'t have enough fuel to drive!' )

    def test_fuel_amount_after_drive(self):
        self.car.fuel_amount=1
        self.car.drive ( 100 )
        self.assertEqual ( self.car.fuel_amount, 0 )

if __name__ == "__main__":
    unittest.main()