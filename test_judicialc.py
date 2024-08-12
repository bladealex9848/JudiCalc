import unittest
from datetime import datetime
from app import calculate_working_days, load_holidays

class TestJudiCalc(unittest.TestCase):
    def setUp(self):
        self.holidays_2023 = load_holidays(2023)

    def test_load_holidays(self):
        self.assertIsInstance(self.holidays_2023, list)
        self.assertTrue(len(self.holidays_2023) > 0)
        self.assertIn("2023-01-01", self.holidays_2023)  # Año Nuevo

    def test_calculate_working_days_normal_week(self):
        start_date = datetime(2023, 8, 14)  # Lunes
        end_date = datetime(2023, 8, 18)  # Viernes
        working_days = calculate_working_days(start_date, end_date, "Individual Penal", self.holidays_2023)
        self.assertEqual(working_days, 5)

    def test_calculate_working_days_with_weekend(self):
        start_date = datetime(2023, 8, 14)  # Lunes
        end_date = datetime(2023, 8, 20)  # Domingo
        working_days = calculate_working_days(start_date, end_date, "Individual Penal", self.holidays_2023)
        self.assertEqual(working_days, 5)

    def test_calculate_working_days_with_holiday(self):
        start_date = datetime(2023, 8, 7)  # Lunes (festivo en Colombia)
        end_date = datetime(2023, 8, 11)  # Viernes
        working_days = calculate_working_days(start_date, end_date, "Individual Penal", self.holidays_2023)
        self.assertEqual(working_days, 4)

    def test_calculate_working_days_colectiva_december(self):
        start_date = datetime(2023, 12, 1)
        end_date = datetime(2023, 12, 31)
        working_days = calculate_working_days(start_date, end_date, "Colectiva", self.holidays_2023)
        # El cálculo exacto dependerá de los días hábiles en diciembre de 2023
        # menos 7 días por la regla especial de Colectiva
        expected_working_days = 19  # Este número puede necesitar ajuste
        self.assertEqual(working_days, expected_working_days)

    def test_calculate_working_days_different_specialties(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)
        working_days_penal = calculate_working_days(start_date, end_date, "Individual Penal", self.holidays_2023)
        working_days_colectiva = calculate_working_days(start_date, end_date, "Colectiva", self.holidays_2023)
        self.assertNotEqual(working_days_penal, working_days_colectiva)
        self.assertGreater(working_days_penal, working_days_colectiva)

    def test_invalid_dates(self):
        start_date = datetime(2023, 12, 31)
        end_date = datetime(2023, 1, 1)
        with self.assertRaises(ValueError):
            calculate_working_days(start_date, end_date, "Individual Penal", self.holidays_2023)

if __name__ == '__main__':
    unittest.main()