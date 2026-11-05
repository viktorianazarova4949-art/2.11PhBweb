import csv
from pathlib import Path
from models.user import User

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def _read_rows(file_name: str) -> list[list[str]]:
    rows = []
    with open(DATA_DIR / file_name, encoding="utf-8") as file:
        for line in csv.reader(file):
            if line:
                rows.append(line)
    return rows

def wrong_email_password_users() -> list[User]:
    return [User(username=r[0], password=r[1]) for r in _read_rows("wrong_email_password.csv")]
