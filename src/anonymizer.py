from __future__ import annotations

import os

import numpy as np
import pandas as pd


def anonymize_data(df: pd.DataFrame) -> pd.DataFrame:
	anonymized = df.copy()

	if "Importe" in anonymized.columns:
		factors = np.random.uniform(0.9, 1.1, size=len(anonymized))
		anonymized["Importe"] = anonymized["Importe"].astype(float) * factors
		if "Monto_Abs" in anonymized.columns:
			anonymized["Monto_Abs"] = anonymized["Importe"].abs()

	if "Beneficiario" in anonymized.columns:
		benef = anonymized["Beneficiario"].astype(str).str.lower()
		anonymized.loc[benef.str.contains("sabor llanero - compra", na=False), "Beneficiario"] = "Proveedor_Suministros"
		anonymized.loc[benef.str.contains("ventas", na=False), "Beneficiario"] = "Venta_Publico"

	if "Fecha" in anonymized.columns:
		offsets = np.random.randint(1, 4, size=len(anonymized))
		directions = np.random.choice([-1, 1], size=len(anonymized))
		anonymized["Fecha"] = pd.to_datetime(anonymized["Fecha"], errors="coerce") + pd.to_timedelta(
			offsets * directions, unit="D"
		)

	output_path = os.path.join("data", "processed", "demo_audit.csv")
	os.makedirs(os.path.dirname(output_path), exist_ok=True)
	anonymized.to_csv(output_path, index=False)

	return anonymized
