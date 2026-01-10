import pandas as pd
import os

class CSVFileManager:
    def read(self, path: str) -> pd.DataFrame:
        # Primer comprovem si el fitxer existeix abans d'intentar llegir-lo
        if not os.path.exists(path):
            # Això t'avisarà a la terminal de quin fitxer falta exactament
            print(f"ERROR CRÍTIC: No s'ha trobat el fitxer a la ruta: {os.path.abspath(path)}")
            # Retornem un DataFrame buit per evitar que el programa peti del tot
            return pd.DataFrame()
        
        try:
            # Línia 5 original millorada amb gestió d'excepcions
            return pd.read_csv(path)
        except Exception as e:
            print(f"Error llegint el CSV {path}: {e}")
            return pd.DataFrame()
  