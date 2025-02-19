import os
import sys
import unittest
import tempfile
import shutil
from PIL import Image

# Add the project root directory to the path to import 'converter'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from converter import convert_images_to_pdf

class TestImageToPDFConverter(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for the test files
        self.test_dir = tempfile.mkdtemp()

        # Create a temporary image using Pillow
        self.image_path = os.path.join(self.test_dir, "test_image.jpg")
        image = Image.new("RGB", (100, 100), (255, 0, 0))  # Red 100x100 image
        image.save(self.image_path)

        # Output path for the generated PDF
        self.output_pdf = os.path.join(self.test_dir, "output.pdf")

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_conversion_success(self):
        """
        Verifies that converting an existing image to PDF works correctly.
        """
        convert_images_to_pdf([self.image_path], self.output_pdf)
        # The PDF file should exist
        self.assertTrue(os.path.exists(self.output_pdf))
        # And its content should not be empty
        self.assertGreater(os.path.getsize(self.output_pdf), 0)

    def test_nonexistent_image(self):
        """
        Verifies that conversion raises an exception when the image does not exist.
        """
        non_existent_path = os.path.join(self.test_dir, "nonexistent.jpg")
        with self.assertRaises(ValueError):
            convert_images_to_pdf([non_existent_path], self.output_pdf)

if __name__ == '__main__':
    unittest.main()
