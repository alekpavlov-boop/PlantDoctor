"""Small data-cleaning helpers used by dataset preparation code."""


def clean_label(value: str) -> str:
    """Normalize a class label for consistent comparisons and display."""
    if not isinstance(value, str):
        raise TypeError("label must be a string")
    return " ".join(value.strip().split()).casefold()
