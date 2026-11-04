from dataclasses import dataclass
from typing import Optional

@dataclass
class Contact:
    name: str
    lastName: str
    email: str
    phone: str
    address: str
    description: str
    id:Optional[str]=None