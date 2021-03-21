from worker_01_lab import Worker
# from parameterized import parameterized
import unittest

class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Olga", 5000, 5)

    def test_worker_initialized(self):
        self.assertEqual ( self.worker.name, "Olga" )
        self.assertEqual ( self.worker.salary, 5000 )
        self.assertEqual ( self.worker.energy, 5 )

    def test_energy_incremented(self):
        result = self.worker.energy
        self.worker.rest()
        expected_result = self.worker.energy
        self.assertEqual(result+1, expected_result)

    def test_energy_raised_below_zerro(self):
        self.worker.energy =0
        with self.assertRaises ( Exception ):
            self.worker.work()

    def test_money_increased(self):
        result = self.worker.money
        salary = self.worker.salary
        self.worker.work()
        expected_result = self.worker.money
        self.assertEqual ( result + salary, expected_result )

    def test_energy_decreased(self):
        result = self.worker.energy
        self.worker.work()
        expected_result = self.worker.energy
        self.assertEqual(result-1, expected_result)

    def test_get_info(self):
        result = self.worker.get_info ()
        expected_result = "Olga has saved 0 money."
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

