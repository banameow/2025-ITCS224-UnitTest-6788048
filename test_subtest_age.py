import unittest

def isAdult(age):
    return 18 <= age <= 65

class TestIsAdult(unittest.TestCase):

    def test_adult_age(self):
        print()
        for age in range(18, 66):
            if isAdult(age):
                print(f"{age} is considered as an Adult.")
            self.assertEqual(isAdult(age), 18 <= age <= 65)

if __name__ == "__main__":
    unittest.main(verbosity=2)