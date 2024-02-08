"""Provide functions to handle config."""
import json

from const import CONFIG_FILE


class Config:
    """Represent a config object."""

    def __init__(self) -> None:
        self._data = None
        try:
            self.data = self._load()
        except OSError:
            print("Load config failed")
            self.data = {}

    def _load(self):
        """Load a config."""
        print("Loading config")
        with open(CONFIG_FILE, "rb") as config_file:
            try:
                data = json.load(config_file)
            except ValueError:
                print("JSON Load failed")
                data = {}
        return data

    def save(self, data):
        """Save a config."""
        with open(CONFIG_FILE, "w+", encoding="utf-8") as config_file:
            try:
                json.dump(data, config_file)
            except ValueError:
                print("Save config failed")
            else:
                self.data = data

    @property
    def data(self):
        """Returns data dict."""
        return self._data

    @data.setter
    def data(self, obj):
        if isinstance(obj, dict):
            self._data = obj
            for key in obj:
                setattr(self, key, obj[key])
