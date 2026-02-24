"""Generate sample data for the Streamlit app."""

from datetime import date, timedelta
from pathlib import Path
import random

import polars as pl


def generate_sample_data(
    n_records: int = 5000,
    output_path: str | Path | None = None,
) -> pl.DataFrame:
    """Generate realistic sample sales data.

    Args:
        n_records: Number of records to generate.
        output_path: Optional path to save the Parquet file.

    Returns:
        Polars DataFrame with sample data.
    """
    random.seed(42)

    categories = ["Electronic", "Clothes", "House", "Sport", "Food", "Beauty"]
    regions = [
        "Victoria",
        "New South Wales",
        "Tasmania",
        "Western Australia",
        "Queensland",
        "South Australia",
        "Northern Territory",
        "Australian Capital Territory",
    ]

    base_date = date(2026, 2, 14)

    records = []
    for i in range(n_records):
        category = random.choice(categories)
        region = random.choice(regions)

        base_value = {
            "Electronic": 500,
            "Clothes": 100,
            "House": 300,
            "Sport": 150,
            "Food": 50,
            "Beauty": 80,
        }[category]

        value = base_value * random.uniform(0.5, 3.0)
        days_offset = random.randint(0, 90)
        record_date = base_date + timedelta(days=days_offset)

        records.append({
            "id": i + 1,
            "date": record_date,
            "category": category,
            "name": f"{category} - Product {random.randint(1, 100)}",
            "region": region,
            "value": round(value, 2),
            "quantity": random.randint(1, 10),
        })

    df = pl.DataFrame(records)
    df = df.sort("date")

    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.write_parquet(output_path)
        print(f"Generated {n_records} records -> {output_path}")

    return df


if __name__ == "__main__":
    output = Path(__file__).parent.parent / "data" / "processed" / "sample_data.parquet"
    df = generate_sample_data(output_path=output)

    print(f"\nSample data summary:")
    print(f"  Records: {len(df)}")
    print(f"  Columns: {df.columns}")
    print(f"  Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"  Total value: {df['value'].sum():,.0f} €")
    print(f"  Categories: {df['category'].unique().to_list()}")
    print(f"  Regions: {df['region'].unique().to_list()}")
