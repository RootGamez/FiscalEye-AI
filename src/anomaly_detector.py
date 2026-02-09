from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


@dataclass
class FinancialAnomalyDetector:
    """Isolation Forest-based anomaly detector for pizzeria transactions."""

    contamination: float = 0.05
    random_state: int = 42
    model: Optional[IsolationForest] = None

    def __post_init__(self) -> None:
        self.model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
            n_estimators=200,
        )

    def _build_features(self, df: pd.DataFrame) -> pd.DataFrame:
        if "Monto_Abs" not in df.columns:
            raise ValueError("Input DataFrame must include a 'Monto_Abs' column.")

        features = pd.DataFrame()
        features["Monto_Abs"] = pd.to_numeric(df["Monto_Abs"], errors="coerce").fillna(0.0)

        if "Fecha" in df.columns:
            date_series = pd.to_datetime(df["Fecha"], errors="coerce")
            features["Dia_Semana"] = date_series.dt.dayofweek.fillna(0).astype(int)

        return features

    def train(self, df: pd.DataFrame) -> None:
        features = self._build_features(df)
        self.model.fit(features)

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        features = self._build_features(df)
        predictions = self.model.predict(features)
        result = df.copy()
        result["anomaly"] = predictions
        return result

    def get_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        labeled = self.predict(df)
        return labeled[labeled["anomaly"] == -1]
