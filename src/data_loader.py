from __future__ import annotations

import pandas as pd


def _parse_importe(series: pd.Series) -> pd.Series:
	cleaned = series.astype(str).str.strip()

	def normalize_value(value: str) -> str:
		if "," in value and "." in value:
			value = value.replace(".", "")
		if "," in value:
			value = value.replace(",", ".")
		return value

	normalized = cleaned.map(normalize_value)
	return pd.to_numeric(normalized, errors="coerce")


def load_homebank_data(filepath: str) -> pd.DataFrame:
	df = pd.read_csv(filepath, sep=";")

	if "Fecha" in df.columns:
		df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y-%m-%d", errors="coerce")

	if "Importe" in df.columns:
		df["Importe"] = _parse_importe(df["Importe"]).astype("float64")

	if "Importe" in df.columns:
		df["Tipo"] = df["Importe"].apply(lambda value: "Egreso" if value < 0 else "Ingreso")
		df["Monto_Abs"] = df["Importe"].abs()

	text_columns = ["Beneficiario", "Categoria", "Categoría"]
	for column in text_columns:
		if column in df.columns:
			df[column] = df[column].astype(str).str.strip()

	return df
