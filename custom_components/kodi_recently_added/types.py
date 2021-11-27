from typing import Optional, TypedDict


class KodiConfig(TypedDict):
    host: str
    name: Optional[str]
    password: str
    port: int
    ssl: bool
    timeout: int
    username: str
    ws_port: int
