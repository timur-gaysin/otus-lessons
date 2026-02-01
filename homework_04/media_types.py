from dataclasses import dataclass
from typing import Any, Dict, Optional

from homework_04.media_base import FileInfo, MediaFile


@dataclass
class AudioMeta:
    duration_sec: int
    sample_rate_hz : int
    channels: int
    codec: Optional[str] = None

class AudioFile(MediaFile):
    def __init__(self, info : FileInfo, meta : AudioMeta) -> None:
        super().__init__(info)
        self._meta = meta

    @property
    def kind(self) -> str:
        return "audio"
    
    def metadata(self) -> Dict[str, Any]:
        return {
            "duration_sec": self._meta.duration_sec,
            "sample_rate_hz": self._meta.sample_rate_hz,
            "channels": self._meta.channels,
            "codec" : self._meta.codec,
        }


@dataclass
class VideoMeta:
    duration_sec : int
    width: int
    height: int
    fps: float
    codec: Optional[str] = None
    
class VideoFile(MediaFile):
    def __init__(self, info: FileInfo, meta : VideoMeta):
        super().__init__(info)
        self._meta = meta

    @property
    def kind(self) -> str:
        return "video"
    
    def metadata(self) -> Dict[str, Any]:
        return  {
            "duration_sec": self._meta.duration_sec,
            "width": self._meta.width,
            "height": self._meta.height,
            "fps": self._meta.fps,
            "codec" : self._meta.codec,
        }
    
@dataclass
class PhotoMeta:
    width: int
    height: int
    camera_model: Optional[str] = None
    iso: Optional[int] = None

class PhotoFile(MediaFile):
    def __init__(self, info : FileInfo,meta: PhotoMeta):
        super().__init__(info)
        self._meta = meta

    @property
    def kind(self) -> str:
        return "photo"
    
    def metadata(self) -> Dict[str, Any]:
        return {
            "width": self._meta.width,
            "height": self._meta.height,
            "camera_model": self._meta.camera_model,
            "iso": self._meta.iso,
        }