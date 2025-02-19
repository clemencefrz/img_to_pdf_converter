import argparse
from converter import convert_images_to_pdf

def main():
    parser = argparse.ArgumentParser(
        description="Image to PDF converter"
    )
    parser.add_argument(
        "images", nargs="+", help="Paths to the images to be converted"
    )
    parser.add_argument(
        "-o", "--output", default="output.pdf", help="Path to the output PDF file (default: output.pdf)"
    )
    
    args = parser.parse_args()
    
    try:
        convert_images_to_pdf(args.images, args.output)
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
