def validate_index(index: str, expected_length: int | None = None) -> str:
    """
    Validate and normalize an i7 index.

    Rules:
    - must not be empty
    - must contain only A, C, G, T
    - must match expected length if provided
    """

    if not isinstance(index, str):
        raise ValueError("Index must be a string.")

    index = index.strip().upper()

    if not index:
        raise ValueError("Index cannot be empty.")

    allowed_bases = {"A", "C", "G", "T"}

    if any(base not in allowed_bases for base in index):
        raise ValueError(f"Invalid characters found in index: {index}")

    if expected_length is not None and len(index) != expected_length:
        raise ValueError(
            f"Index {index} has length {len(index)}, expected {expected_length}."
        )

    return index