from typing import Optional

from typing_extensions import TypedDict


class DeviceStateAttrs(TypedDict):
    data: str


class KodiConfig(TypedDict):
    host: str
    name: Optional[str]
    password: str
    port: int
    ssl: bool
    timeout: int
    username: str
    ws_port: int


class KodiArt(TypedDict):
    thumb: str
    tvshow.banner: str
    tvshow.fanart: str
    tvshow.poster: str


class KodiTVEpisodeResult(TypedDict):
    art: KodiArt
    dateadded: str
    episode: int
    episodeid: int
    fanart: str
    firstaired: str
    label: str
    playcount: int
    rating: float
    runtime: int
    season: int
    showtitle: str
    title: str
