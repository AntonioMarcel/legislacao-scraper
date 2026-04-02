from dataclasses import asdict
import json
from models import Legislacao

class JsonlWriter:
    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        self._file = open(self.filepath, "w", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._file.close()

    def write(self, leg: Legislacao):
        leg_dict = asdict(leg)
        leg_json = json.dumps(leg_dict, ensure_ascii=False)
        self._file.write(f"{leg_json}\n")
        self._file.flush()