#!/usr/bin/python3
"""Unit testing rectangle"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import pep8


class TestRectanglepep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        rectangle = "models/rectangle.py"
        test_rectangle = "tests/test_models/test_rectangle.py"
        result = style.check_files([rectangle, test_rectangle])
        self.assertEqual(result.total_errors, 0)


class TestDocs(unittest.TestCase):
    """test docstrings for rectangle and test_rectangle files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)


class TestRectangle(unittest.TestCase):
    """This class is for testing the Square class"""

    @classmethod
    def setUpClass(cls):
        """set up instances for all tests"""

        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(5, 5, 5)
        cls.r3 = Rectangle(1, 2, 3, 4)
        cls.r4 = Rectangle(5, 6, 7, 8, 9)

    def test_id(self):
        """Test to check id's"""

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 9)

    def test_validate_attr(self):
        """Tests to validate error messages of attr"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("one", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(1.1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({1: 2}, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((1, 2), 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([1, 2], 3)

    def test_height_errors(self):
        """test height type and value errors"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "two")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, 2.2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, {2: 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (2, 3))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [2, 3])

    def test_x_errors(self):
        """test x type and value errors"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, "three", 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, 3.3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, {3: 4}, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, (3, 4), 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, [3, 4], 5)

    def test_height(self):
        """test height attribute"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r4.height, 6)

    def test_x(self):
        """test x attribute"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 5)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r4.x, 7)

    def test_y(self):
        """test y attribute"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 4)
        self.assertEqual(self.r4.y, 8)

    def test_area(self):
        """test area method"""
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 25)
        self.assertEqual(self.r3.area(), 2)
        self.assertEqual(self.r4.area(), 30)

    def test_display(self):
        """Test display method"""

        r1 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
        r1 = Rectangle(1, 1)
        expected_output = "#\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
        r1 = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test str method"""

        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 5/0 - 5/5")
        self.assertEqual(str(self.r3), "[Rectangle] (3) 3/4 - 1/2")
        self.assertEqual(str(self.r4), "[Rectangle] (9) 7/8 - 5/6")

    def test_update(self):
        """Test update method"""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        r1.update(id=1)
        self.assertEqual(r1.id, 1)

        r1.update(width=2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)

        r1.update(height=3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(x=5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)

        r1.update(y=7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)

        r1.update(2, 4, 6, 8, 10, id=3, width=5, height=7, x=9, y=11)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 11)

    def test_to_dictionary(self):
        """Test to_dictionary method"""

        d1 = self.r1.to_dictionary()
        self.assertDictEqual(d1, {"height": 10, "x": 0, "id": 1, "y": 0, "width": 10})
        d2 = self.r2.to_dictionary()
        self.assertDictEqual(d2, {"width": 5, "x": 5, "y": 0, "id": 2, "height": 5})
        d3 = self.r3.to_dictionary()
        self.assertDictEqual(d3, {"width": 1, "x": 3, "height": 2, "id": 3, "y": 4})
        d4 = self.r4.to_dictionary()
        self.assertDictEqual(d4, {"id": 9, "x": 7, "y": 8, "height": 6, "width": 5})


if __name__ == "__main__":
    unittest.main()
