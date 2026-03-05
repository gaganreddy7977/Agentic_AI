import pandas as pd

class FileAgent:

    def load_file(self, file_path):

        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)

        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)

        else:
            raise ValueError("Unsupported file format. Use CSV or XLSX")

        return df