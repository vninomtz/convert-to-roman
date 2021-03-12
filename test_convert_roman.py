import unittest
from convert_roman import Roman


class TestRomanConverter(unittest.TestCase):
    def test_number_entries(self):
        self.assertRaises(ValueError, Roman.convert_from_int, "")
        self.assertRaises(ValueError, Roman.convert_from_int, "xxcdc")
        self.assertRaises(ValueError, Roman.convert_from_int, 0)
        self.assertRaises(ValueError, Roman.convert_from_int, -1)
        self.assertRaises(ValueError, Roman.convert_from_int, 3001)
        self.assertRaises(ValueError, Roman.convert_from_int, 5000)

    def test_convert_from_int(self):
        self.assertEqual(Roman.convert_from_int(3), "III")  # III
        self.assertEqual(Roman.convert_from_int(345), "CCCXLV")  # CCCXLV
        self.assertEqual(Roman.convert_from_int(927), "CMXXVII")  # CMXXVII
        self.assertEqual(Roman.convert_from_int(2999), "MMCMXCIX")  # MMCMXCIX
        self.assertEqual(Roman.convert_from_int(16), "XVI")  # XVI
        self.assertEqual(Roman.convert_from_int(45), "XLV")  # XLV
        self.assertEqual(Roman.convert_from_int(39), "XXXIX")  # XXXIX
        self.assertEqual(Roman.convert_from_int(410), "CDX")  # CDX


if __name__ == "__main__":
    unittest.main()
