from vehicle.project.vehicle import Vehicle
import unittest


class VehicleTests(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10.0, 100.0)

    def test_vehicle_initialized(self):
        self.assertEqual ( self.vehicle.fuel, 10.0 )
        self.assertEqual ( self.vehicle.capacity, 10.0 )
        self.assertEqual ( self.vehicle.horse_power, 100.0 )

    def test_drive(self):
        self.vehicle.drive ( 1 )
        self.assertEqual ( self.vehicle.fuel , 8.75)

    def test_drive_raise_exeption(self):
        with self.assertRaises ( Exception ) as exp:
            self.vehicle.drive(500)
        self.assertEqual ( exp.exception.args[0], "Not enough fuel" )
        # self.assertRaises ( Exception, self.vehicle.drive, 50 )

    def test_refuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel ( 1 )
        self.assertEqual ( self.vehicle.fuel , 1)

    def test_refuel_raise_exeption(self):
        with self.assertRaises ( Exception ) as exp:
            self.vehicle.refuel(50)
        self.assertEqual ( exp.exception.args[0], "Too much fuel" )
        # self.assertRaises ( Exception, self.vehicle.refuel, 500 )

    def test_str_vehicle(self):
        self.assertEqual ( self.vehicle.__str__(), "The vehicle has 100.0 horse power with 10.0 fuel left and 1.25 fuel consumption" )


if __name__ == "__main__":
    unittest.main()