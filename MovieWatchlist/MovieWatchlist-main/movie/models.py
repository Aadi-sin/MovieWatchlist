from ctypes import cast
from dataclasses import dataclass, field
from datetime import datetime
from turtle import title

@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: list[str] = field(default_factory=list)
    series: list[str] = field(default_factory=list)
    last_watched: datetime = None
    video_link: str = None
    rating: int = 0
