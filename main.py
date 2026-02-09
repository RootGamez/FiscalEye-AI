from __future__ import annotations

import os

import pandas as pd

from src.anomaly_detector import FinancialAnomalyDetector
from src.anonymizer import anonymize_data
from src.data_loader import load_homebank_data
from src.visualizer import plot_audit_results


def main() -> None:
    raw_path = os.path.join("data", "raw", "homebank_export.csv")
    df = load_homebank_data(raw_path)
    anonymized_df = anonymize_data(df)

    detector = FinancialAnomalyDetector(contamination=0.05)
    detector.train(anonymized_df)
    labeled_df = detector.predict(anonymized_df)

    anomalies = detector.get_anomalies(anonymized_df)
    top_anomalies = anomalies.sort_values(by="Importe", ascending=False).head(5)
    print("Top 5 anomalies by amount:")
    print(top_anomalies)

    plot_path = plot_audit_results(labeled_df, output_dir="outputs")
    print(f"Saved plot to {plot_path}")


if __name__ == "__main__":
    main()
