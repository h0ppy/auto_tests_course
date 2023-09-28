import unittest
from registrations import registration_page_1, registration_page_2

expected_result = "Congratulations! You have successfully registered!"

class Test_page(unittest.TestCase):
    def test_first_page(self):
        self.assertEqual(registration_page_1(), expected_result, "Registration was unsuccessful")
        
    def test_second_page(self):
        self.assertEqual(registration_page_2(), expected_result, "Registration was unsuccessful")
        
if __name__ == "__main__":
    unittest.main()