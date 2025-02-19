import img2pdf
import os

def convert_images_to_pdf(image_paths, output_path):
    """
    Converts a list of images into a PDF file.
    
    :param image_paths: List of image file paths.
    :param output_path: Full path of the output PDF file.
    """

    valid_images = []
    for img in image_paths:
        if os.path.exists(img):
            valid_images.append(img)
        else:
            print(f"[WARNING] The file {img} does not exist and will be ignored.")
    
    if not valid_images:
        raise ValueError("No valid images provided for conversion.")
    
    try:
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(valid_images))
        print(f"[INFO] PDF successfully generated: {output_path}")
    except Exception as e:
        print(f"[ERROR] An error occurred during conversion: {e}")
