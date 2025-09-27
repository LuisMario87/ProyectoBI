# ETL preliminar guardado automáticamente
import pandas as pd

def load_data(path="/mnt/data/demoDatos.xlsx"):
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip()
    df["FechaCompra_parsed"] = pd.to_datetime(df.get("FechaCompra"), errors="coerce")
    df["Cantidad"] = pd.to_numeric(df.get("Cantidad"), errors="coerce")
    df["PrecioUnitario"] = pd.to_numeric(df.get("PrecioUnitario"), errors="coerce")
    df["TotalVenta"] = df["Cantidad"] * df["PrecioUnitario"]
    return df

if __name__ == "__main__":
    df = load_data("/mnt/data/demoDatos.xlsx")
    print("Filas cargadas:", len(df))
