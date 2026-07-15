from itertools import combinations
from .validator import validate_index


def hamming_distance(seq1: str, seq2: str) -> int:
    """
    Count how many positions differ between two sequences.
    """

    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length.")

    return sum(base1 != base2 for base1, base2 in zip(seq1, seq2))


def find_conflicts(samples: list[dict], max_distance: int = 2) -> list[dict]:
    """
    Find i7 barcode conflicts.

    Conflict rules:
    - distance 0 = duplicate
    - distance 1 or 2 = near conflict
    """

    if not samples:
        return []

    expected_length = len(samples[0]["i7_index"])
    normalized_samples = []

    for sample in samples:
        sample_id = sample["sample_id"].strip()
        index = validate_index(
            sample["i7_index"],
            expected_length=expected_length,
        )

        normalized_samples.append(
            {
                "sample_id": sample_id,
                "i7_index": index,
            }
        )

    conflicts = []

    for sample1, sample2 in combinations(normalized_samples, 2):
        index1 = sample1["i7_index"]
        index2 = sample2["i7_index"]

        distance = hamming_distance(index1, index2)

        if distance == 0:
            conflict_type = "duplicate"
        elif 1 <= distance <= max_distance:
            conflict_type = "near_conflict"
        else:
            continue

        conflicts.append(
            {
                "sample_1": sample1["sample_id"],
                "sample_2": sample2["sample_id"],
                "index_1": index1,
                "index_2": index2,
                "distance": distance,
                "conflict_type": conflict_type,
            }
        )

    return conflicts