import csv


def load_samples_from_csv(file_path: str) -> list[dict]:
    """
    Load samples from a CSV file.

    Required columns:
    - sample_id
    - i7_index
    """

    samples = []

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        required_columns = {"sample_id", "i7_index"}

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty.")

        if not required_columns.issubset(reader.fieldnames):
            raise ValueError("CSV must contain 'sample_id' and 'i7_index' columns.")

        for row in reader:
            sample_id = row["sample_id"].strip()
            i7_index = row["i7_index"].strip()

            if not sample_id:
                raise ValueError("Sample ID cannot be empty.")

            samples.append(
                {
                    "sample_id": sample_id,
                    "i7_index": i7_index,
                }
            )

    return samples