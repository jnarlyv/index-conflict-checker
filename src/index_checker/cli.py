import argparse
from .parser import load_samples_from_csv
from .conflict import find_conflicts


def run_cli() -> None:
    parser = argparse.ArgumentParser(
        description="Check i7 indices for duplicate and near conflicts."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to CSV file with sample_id and i7_index columns.",
    )

    parser.add_argument(
        "--max-distance",
        type=int,
        default=2,
        help="Maximum number of base differences to flag. Default is 2.",
    )

    args = parser.parse_args()

    samples = load_samples_from_csv(args.input)
    conflicts = find_conflicts(samples, max_distance=args.max_distance)

    if not conflicts:
        print("No conflicts found.")
        return

    print("Conflicts found:\n")

    for conflict in conflicts:
        print(
            f"{conflict['sample_1']} ({conflict['index_1']}) vs "
            f"{conflict['sample_2']} ({conflict['index_2']}): "
            f"{conflict['conflict_type']} "
            f"(distance={conflict['distance']})"
        )