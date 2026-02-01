"""
Файл описывает базовые сущности для работы с медиа файлами
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import datetime
from typing import Any, Dict, Optional
from uuid import uuid4


@dataclass
class FileInfo:
    #общие данные о любом файла
    name: str
    size_bytes : int
    created_at: datetime
    owner: str
    mime_type: Optional[str] = None

@dataclass
class MediaId:
    #идентификатор медиа в системе
    value: str =  field(default_factory=lambda: str(uuid4()))

class MediaFile(ABC):
    
    def __init__(self, info: FileInfo, media_id: Optional[MediaId] = None) -> None:
        self.id : MediaId = media_id or MediaId()
        self.info : FileInfo = info
        self.deleted : bool = False

    @property
    @abstractmethod
    def kind(self) ->str:
        #тип медиа
        raise NotImplementedError
    
    @abstractmethod
    def metadata(self) -> Dict[str,Any]:
        #метаданные файла
        raise NotImplementedError
    
    def rename(self, new_name: str) -> None:
        self._ensure_not_deleted()
        self.info.name = new_name

    def mark_deleted(self) -> None:
        #метка о том, что файл удален. Физически ничего не происходит
        self.deleted = True

    def _ensure_not_deleted(self) -> None:
        if self.deleted:
            raise RuntimeError(f"Mdeia file {self.id.value} is deleted")
        
