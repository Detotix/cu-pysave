import gzip
import json

class CU_GameSave:
    """
    Class to load and save savefiles.
    """
    def __init__(self, data):
        if isinstance(data, str):
            self._data = json.loads(data)
        elif isinstance(data, dict):
            self._data = data
        else:
            raise TypeError("Data must be a string or a dict.")
    
    def write_save(self, filename: str):
        """
        Writes the savefile to disk.
        """
        with gzip.open(filename, "wb", compresslevel=9) as f:
            print(self._data)
            f.write(json.dumps(self._data).encode("utf-8"))
    
    def dict(self):
        """
        Returns the savefile as a dict.
        """
        return self._data

def LoadSave(filename: str) -> CU_GameSave:
    """
    Loads a savefile and returns it as CU_GameSave
    """
    with gzip.open(filename, 'rb') as f:
        jsondata = json.loads(f.read())
    return CU_GameSave(jsondata)