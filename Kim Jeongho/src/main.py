import argparse
from pathlib import Path

import cv2
from filter import apply_cartoon_filter, apply_sketch_filter


VALID_MODES = ("cartoon", "sketch")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Cartoon & Sketch image filter tool using OpenCV"
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="input image path",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="output image path",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=VALID_MODES,
        required=True,
        help="filter mode: 'cartoon' or 'sketch'",
    )

    return parser.parse_args()


def validate_paths(input_path_str: str, output_path_str: str) -> tuple[Path, Path]:
    """Validate input/output paths and create output directory if needed."""
    input_path = Path(input_path_str)
    output_path = Path(output_path_str)

    if not input_path.is_file():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    # Create parent directory for output file if it does not exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    return input_path, output_path


def main() -> None:
    args = parse_args()

    input_path, output_path = validate_paths(args.input, args.output)

    img = cv2.imread(str(input_path))
    if img is None:
        raise RuntimeError(f"Failed to read image: {input_path}")

    if args.mode == "cartoon":
        result = apply_cartoon_filter(img)
    elif args.mode == "sketch":
        result = apply_sketch_filter(img)
    else:
        # This should not happen because argparse restricts choices,
        # but we keep it for safety.
        raise ValueError(f"Unsupported mode: {args.mode}. Use {VALID_MODES}.")

    success = cv2.imwrite(str(output_path), result)
    if not success:
        raise RuntimeError(f"Failed to write output image: {output_path}")


if __name__ == "__main__":
    main()
