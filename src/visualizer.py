from __future__ import annotations

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_audit_results(df: pd.DataFrame, output_dir: str = "outputs") -> str:
    """Plot audit results highlighting anomalies and save as PNG."""

    os.makedirs(output_dir, exist_ok=True)
    plot_df = df.copy()

    if "Fecha" in plot_df.columns:
        plot_df["Fecha"] = pd.to_datetime(plot_df["Fecha"], errors="coerce")

    if "anomaly" in plot_df.columns:
        plot_df["label"] = plot_df["anomaly"].map({1: "Normal", -1: "Anomalia"}).fillna("Normal")
    else:
        plot_df["label"] = "Normal"

    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=plot_df,
        x="Fecha" if "Fecha" in plot_df.columns else plot_df.index,
        y="Importe",
        hue="label",
        palette={"Normal": "#2ca02c", "Anomalia": "#ff1f1f"},
        alpha=0.8,
        edgecolor=None,
    )

    plt.axhline(0, color="#444444", linewidth=1.2, alpha=0.7)
    plt.title("Auditoría Inteligente - Pizzería Sabor Llanero")
    plt.xlabel("Fecha")
    plt.ylabel("Importe")

    output_path = os.path.join(output_dir, "audit_scatter.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    return output_path
