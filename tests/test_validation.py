from pathlib import Path

import pytest
from PIL import Image

from plantdoctor.validation import InvalidImageError, load_image, validate_image


def test_validate_image_returns_rgb_copy():
    image = Image.new("L", (12, 8), color=100)
    result = validate_image(image)
    assert result.mode == "RGB"
    assert result.size == (12, 8)


def test_validate_image_rejects_wrong_input():
    with pytest.raises(InvalidImageError):
        validate_image("not an image")


def test_validate_image_rejects_oversized_dimensions():
    with pytest.raises(InvalidImageError):
        validate_image(Image.new("RGB", (20, 10)), max_dimension=15)


def test_load_image_rejects_non_image_file(tmp_path: Path):
    path = tmp_path / "not-image.jpg"
    path.write_text("not image data")
    with pytest.raises(InvalidImageError):
        load_image(path)


def test_load_image_enforces_file_size(tmp_path: Path):
    path = tmp_path / "tiny.png"
    Image.new("RGB", (2, 2)).save(path)
    with pytest.raises(InvalidImageError):
        load_image(path, max_bytes=1)
