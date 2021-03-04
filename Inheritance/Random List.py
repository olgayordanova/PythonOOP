import random
class RandomList (list):

    def get_random_element(self):
        element = random.choice(self)
        self.pop(self.index(element))
        return element


        #Add additional function that returns and removes a random element from the list.

# import unittest
# from unittest import mock
# import random
#
# class RandomListTests(unittest.TestCase):
#     def test_zero_second(self):
#         mocked_choice = lambda x: 6
#         with mock.patch('random.choice', mocked_choice):
#             li = RandomList()
#             li.append(6)
#             li.append(1.3)
#             li.append(10)
#             li.pop()
#             li.reverse()
#             self.assertEqual(sum(li), 7.3)
#             self.assertEqual(li.get_random_element(),6)
#
#
# if __name__ == '__main__':
#     unittest.main()


## test first zero
# import unittest
# from unittest import mock
# import random
#
# class RandomListTests(unittest.TestCase):
#     def test_zero_first(self):
#         mocked_choice = lambda x: 5
#         with mock.patch('random.choice', mocked_choice):
#             li = RandomList()
#             li.append(4)
#             li.append(3)
#             li.append(5)
#             self.assertEqual(li.get_random_element(), 5)
#
# if __name__ == '__main__':
#     unittest.main()