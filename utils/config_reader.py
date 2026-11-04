import configparser
from functools import lru_cache
from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"

@lru_cache
def _load(file_name: str) -> configparser.ConfigParser:
    parser = configparser.ConfigParser()
    parser.read(CONFIG_DIR / file_name, encoding="utf-8")
    return parser

def get_property(key: str, file_name: str = "base.ini", section: str="base") -> str:
    return _load(file_name).get(section, key)