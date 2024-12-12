import pandas as pd

class Load:
    """
    Load Excel workbook to return datasets.
    """
    def __init__(self, file_name):
        """
        Initializes a new Load object.
        :param file_name: Excel file name.
        """
        self.file = file_name
    def get_startkm(self):
        """
        Reads data from column 'J' in the 'Rutting' sheet.
        :return:
        """
        data_start = pd.read_excel(self.file, sheet_name="Rutting", usecols="J", skiprows=23, nrows=6407 - 25 + 1)
        return data_start.iloc[:, 0].tolist()

    def get_endkm(self):
        """
        Reads data from column 'N' in the 'Rutting' sheet.
        :return:
        """
        data_end = pd.read_excel(self.file, sheet_name="Rutting", usecols="N", skiprows=23, nrows=6407 - 25 + 1)
        return data_end.iloc[:, 0].tolist()

    def get_right_list(self):
        """
        Reads data from column 'AM' in the 'Rutting' sheet and removes empty rows.
        :return: Cleaned dataset from column 'AM' as a list.
        """
        data_right = pd.read_excel(self.file, sheet_name="Rutting", usecols="AM", skiprows=23, nrows=6407 - 25+1 )
        #data_rc = data_right.dropna()
        return data_right.iloc[:, 0].tolist()

    def get_left_list(self):
        """
        Reads data from column 'AL' in the 'Rutting' sheet and removes empty rows.
        :return: Cleaned dataset from column 'AL' as a list.
        """
        data_left = pd.read_excel(self.file, sheet_name="Rutting", usecols="AL", skiprows=23, nrows=6407 - 25+1)
        #data_lc = data_left.dropna()
        return data_left.iloc[:, 0].tolist()
