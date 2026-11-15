"""Prediction interface for a future plant classifier."""

import math
from collections.abc import Callable, Sequence
from dataclasses import dataclass

from PIL import Image

from .validation import validate_image


@dataclass(frozen=True)
class Prediction:
    label: str
    confidence: float


def predict_image(
    model: Callable[[Image.Image], Sequence[float]],
    image: Image.Image,
    class_names: Sequence[str],
) -> Prediction:
    """Run a classifier returning class probabilities and select the top class.

    The model must accept an RGB PIL image and return one probability per class.
    This interface does not include or load an actual trained model.
    """
    if not callable(model):
        raise TypeError("model must be callable")
    if not class_names or any(not isinstance(name, str) or not name.strip() for name in class_names):
        raise ValueError("class_names must contain non-empty strings")
    prepared_image = validate_image(image)
    probabilities = list(model(prepared_image))
    if len(probabilities) != len(class_names):
        raise ValueError("model output count must match class_names")
    try:
        values = [float(value) for value in probabilities]
    except (TypeError, ValueError) as exc:
        raise ValueError("model outputs must be numeric probabilities") from exc
    if any(not math.isfinite(value) or value < 0 or value > 1 for value in values):
        raise ValueError("model outputs must be finite probabilities between 0 and 1")
    if not math.isclose(sum(values), 1.0, rel_tol=1e-4, abs_tol=1e-4):
        raise ValueError("model probabilities must sum to 1")
    index = max(range(len(values)), key=values.__getitem__)
    return Prediction(label=class_names[index], confidence=values[index])
