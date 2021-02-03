import unittest
from city_functions import get_city_country


class CityTestCases(unittest.TestCase):
    """Testing the city_country function"""

    def test_city_country(self):
        """Testing the function with only the city and country variable"""
        city_country = get_city_country("hamburg", "germany")
        self.assertEqual(city_country, "Hamburg, Germany")

    def test_city_country_population(self):
        """Testing the function, including the population variable"""
        city_country_population = get_city_country(
            "hamburg", "germany", population="1.850.000"
        )
        self.assertEqual(
            city_country_population, "Hamburg, Germany - population 1.850.000"
        )


if __name__ == "__main__":
    unittest.main()