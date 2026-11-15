import pytest
from PIL import Image

from plantdoctor.prediction import Prediction, predict_image


def test_prediction_returns_highest_probability_class():
    result = predict_image(
        lambda image: [0.2, 0.8],
        Image.new("RGB", (4, 4)),
        ["healthy", "diseased"],
    )
    assert result == Prediction(label="diseased", confidence=0.8)


@pytest.mark.parametrize("scores", [[0.2], [0.8, 0.8], [-0.1, 1.1], [float("nan"), 1.0]])
def test_prediction_rejects_invalid_model_outputs(scores):
    with pytest.raises(ValueError):
        predict_image(lambda image: scores, Image.new("RGB", (4, 4)), ["healthy", "diseased"])


def test_prediction_rejects_empty_class_names():
    with pytest.raises(ValueError):
        predict_image(lambda image: [], Image.new("RGB", (4, 4)), [])
