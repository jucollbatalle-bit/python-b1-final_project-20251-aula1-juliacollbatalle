import pandas as pd

class CSVFileManager:
  def read(self, path) -> pd.DataFrame:
    return pd.read_csv(path)
  