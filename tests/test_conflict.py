import pytest
from src.index_checker.conflict import hamming_distance, find_conflicts


def test_hamming_distance_exact_match():
    assert hamming_distance("ATCG", "ATCG") == 0


def test_hamming_distance_one_difference():
    assert hamming_distance("ATCG", "ATCA") == 1


def test_hamming_distance_two_differences():
    assert hamming_distance("ATCG", "AGCA") == 2


def test_hamming_distance_unequal_lengths():
    with pytest.raises(ValueError):
        hamming_distance("ATCG", "ATC")


def test_find_duplicate_conflict():
    samples = [
        {"sample_id": "sample_1", "i7_index": "ATCG"},
        {"sample_id": "sample_2", "i7_index": "ATCG"},
    ]

    conflicts = find_conflicts(samples)

    assert len(conflicts) == 1
    assert conflicts[0]["conflict_type"] == "duplicate"
    assert conflicts[0]["distance"] == 0


def test_find_near_conflict_distance_one():
    samples = [
        {"sample_id": "sample_1", "i7_index": "ATCG"},
        {"sample_id": "sample_2", "i7_index": "ATCA"},
    ]

    conflicts = find_conflicts(samples)

    assert len(conflicts) == 1
    assert conflicts[0]["conflict_type"] == "near_conflict"
    assert conflicts[0]["distance"] == 1


def test_find_near_conflict_distance_two():
    samples = [
        {"sample_id": "sample_1", "i7_index": "ATCG"},
        {"sample_id": "sample_2", "i7_index": "AGCA"},
    ]

    conflicts = find_conflicts(samples)

    assert len(conflicts) == 1
    assert conflicts[0]["conflict_type"] == "near_conflict"
    assert conflicts[0]["distance"] == 2


def test_no_conflict_distance_three():
    samples = [
        {"sample_id": "sample_1", "i7_index": "ATCG"},
        {"sample_id": "sample_2", "i7_index": "GGCA"},
    ]

    conflicts = find_conflicts(samples)

    assert len(conflicts) == 0