#!/usr/bin/python3
"""Unittest for Square class"""

import json
from os import path
from io import StringIO
import sys
import pep8
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquarepep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        square = "models/square.py"
        test_square = "tests/test_models/test_square.py"
        result = style.check_files([square, test_square])
        self.assertEqual(result.total_errors, 0)


class TestDocs(unittest.TestCase):
    """test docstrings for square and test_square files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(Square.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Square.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Square):
            self.assertTrue(len(func.__doc__) > 0)


class TestSquareClass(unittest.TestCase):
    """This class is for testing the Square class"""

    @classmethod
    def setUpClass(cls):
        """Set up instances for all tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(4)
        cls.s2 = Square(8, 2)
        cls.s3 = Square(16, 2, 3)
        cls.s4 = Square(32, 2, 4, 10)
        cls.s5 = Square(64, 2, 5, None)

    def test_id_validation(self):
        """Test to check id's"""

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)
        self.assertEqual(self.s5.id, 4)

    def test_y_getter(self):
        """Test to check getter function of y"""

        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.y, 4)
        self.assertEqual(self.s5.y, 5)

    def test_x_getter(self):
        """"Test to check getter function of x"""

        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s5.x, 2)

    def test_size_getter(self):
        """"Test to check getter function of size"""

        self.assertEqual(self.s1.size, 4)
        self.assertEqual(self.s2.size, 8)
        self.assertEqual(self.s3.size, 16)
        self.assertEqual(self.s4.size, 32)
        self.assertEqual(self.s5.size, 64)

    def test_area(self):
        """Test to check area function"""

        self.assertEqual(self.s1.area(), 16)
        self.assertEqual(self.s2.area(), 64)
        self.assertEqual(self.s3.area(), 256)
        self.assertEqual(self.s4.area(), 1024)
        self.assertEqual(self.s5.area(), 4096)

    def test_str(self):
        """Test to check area function"""

        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 4")
        self.assertEqual(str(self.s2), "[Square] (2) 2/0 - 8")
        self.assertEqual(str(self.s3), "[Square] (3) 2/3 - 16")
        self.assertEqual(str(self.s4), "[Square] (10) 2/4 - 32")
        self.assertEqual(str(self.s5), "[Square] (4) 2/5 - 64")

    def test_update(self):
        """Test to check update function"""

        s6 = Square(4, 0, 0, 27)
        s7 = Square(32, 2, 4, 10)

        self.assertEqual(str(s6), "[Square] (27) 0/0 - 4")
        s6.update(1, 2, 3, 6)
        self.assertEqual(str(s6), "[Square] (1) 3/6 - 2")

        self.assertEqual(str(s7), "[Square] (10) 2/4 - 32")
        s7.update(size=7, id=89, y=1)
        self.assertEqual(str(s7), "[Square] (89) 2/1 - 7")

    def test_dictionary(self):
        """Test Test to check to_dictionary function"""
        d1 = self.s1.to_dictionary()
        self.assertEqual(d1, {'id': 1, 'x': 0, 'y': 0, 'size': 4})
        d2 = self.s2.to_dictionary()
        self.assertEqual(d2, {'id': 2, 'x': 2, 'y': 0, 'size': 8})
        d3 = self.s3.to_dictionary()
        self.assertEqual(d3, {'id': 3, 'x': 2, 'y': 3, 'size': 16})
        d4 = self.s4.to_dictionary()
        self.assertEqual(d4, {'id': 10, 'x': 2, 'y': 4, 'size': 32})
        d5 = self.s5.to_dictionary()
        self.assertEqual(d5, {'id': 4, 'x': 2, 'y': 5, 'size': 64})

    def test_error_msgs_size(self):
        """Tests to validate error messages of size"""

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s8 = Square(0)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s8 = Square(-98)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s8 = Square("melkin")
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s8 = Square(5.43)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s8 = Square([{3: 11}])
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s8 = Square({9, 8})
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s8 = Square(("melkin", 2))
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s8 = Square(None)

    def test_error_msgs_x(self):
        """Tests to validate error messages for x"""

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s8 = Square(1, -1)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s8 = Square(1, "melkin")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s8 = Square(1, 5.43)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s8 = Square(1, [{3: 11}])
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s8 = Square(1, {9, 8})
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s8 = Square(1, ("melkin", 2))
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s8 = Square(1, None)

    def test_error_msgs_y(self):
        """Tests to validate error messages for y"""

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s8 = Square(1, 0, -1)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s8 = Square(1, 0, "melkin")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s8 = Square(1, 0, 5.43)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s8 = Square(1, 0, [{3: 11}])
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s8 = Square(1, 0, {9, 8})
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s8 = Square(1, 0, ("melkin", 2))
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s8 = Square(1, 0, None)

    def test_display(self):
        """Test display method"""

        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.s1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

        s9 = Square(2, 2, 1)

        et = "\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s9.display()
            self.assertEqual(fake_out.getvalue(), et)

    def test_if_the_flies(self):
        """Test cases creting or calling functions"""

        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            self.s1.display(1)
        with self.assertRaises(TypeError):
            self.s1.to_dictionary(1)
        with self.assertRaises(TypeError):
            self.s1.area(1)

    @classmethod
    def tearDownClass(cls):
        """class method called after tests have run"""

        pass


if __name__ == "__main__":
    unittest.main()
