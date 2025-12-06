import argparse
import os
from utils import load_image, save_image
from filter import pencil_sketch

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(description="Pencil Sketch Filter - Auto Path Version (by Kim Seongsoo)")

    project_root = get_project_root()
    default_input = os.path.join(project_root, "images", "input_example.jpg")
    default_output = os.path.join(project_root, "images", "output_sketch.png")

    parser.add_argument("--input", type=str, default=default_input,
                        help="Input image path")
    parser.add_argument("--output", type=str, default=default_output,
                        help="Output image path")
    parser.add_argument("--blur", type=int, default=21,
                        help="Gaussian blur kernel size (odd number recommended)")

    args = parser.parse_args()

    print(f"Auto-detected project root: {project_root}")
    print(f"Loading image: {args.input}")

    img = load_image(args.input)

    print("Applying pencil sketch filter...")
    sketch = pencil_sketch(img, blur_ksize=args.blur)

    print(f"Saving output: {args.output}")
    save_image(args.output, sketch)

    print("Done! Sketch saved successfully.\n"
          f"Output file saved at:\n{args.output}")


if __name__ == "__main__":
    main()
