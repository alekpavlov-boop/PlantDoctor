"""Validation for image files and image objects supplied as model input."""

from pathlib import Path

from PIL import Image, UnidentifiedImageError


class InvalidImageError(ValueError):
    """Raised when an uploaded or supplied image cannot be safely used."""


def load_image(path: str | Path, *, max_bytes: int = 10 * 1024 * 1024) -> Image.Image:
    """Open an image file after checking its size and decoding its contents."""
    file_path = Path(path)
    try:
        size = file_path.stat().st_size
    except OSError as exc:
        raise InvalidImageError("image file cannot be read") from exc
    if size <= 0 or size > max_bytes:
        raise InvalidImageError(f"image file must be between 1 and {max_bytes} bytes")
    try:
        with Image.open(file_path) as image:
            if max(image.size) > 8192:
                raise InvalidImageError("image dimensions must not exceed 8192 pixels")
            image.verify()
        with Image.open(file_path) as image:
            image.load()
            return validate_image(image)
    except InvalidImageError:
        raise
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as exc:
        raise InvalidImageError("file is not a supported, readable image") from exc


def validate_image(image: Image.Image, *, max_dimension: int = 8192) -> Image.Image:
    """Validate a decoded image and return an RGB copy suitable for inference."""
    if not isinstance(image, Image.Image):
        raise InvalidImageError("input must be a decoded image")
    width, height = image.size
    if width <= 0 or height <= 0 or max(width, height) > max_dimension:
        raise InvalidImageError(f"image dimensions must be between 1 and {max_dimension} pixels")
    return image.convert("RGB")
