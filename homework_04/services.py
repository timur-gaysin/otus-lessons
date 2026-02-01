from dataclasses import dataclass
from typing import Any, Dict

from homework_04.media_base import MediaFile
from homework_04.storages import Storage, StorageRef


@dataclass
class MediaRecord:
    media : MediaFile
    storage_ref : StorageRef
    storage_name : str

class MediaRepository:
    #упрощенный репозиторий
    def __init__(self) -> None:
        self._items : Dict[str,MediaRecord] = {}

    def add(self,record: MediaRecord) -> None:
        self._items[record.media.id.value] = record

    def get(self, media_id: str) -> MediaRecord:
        return self._items[media_id]
    
    def delete(self, media_id : str) -> None:
        self._items[media_id]

class MediaService:
    #создание, обновление, удаление + действия convert/extract_features
    def __init__(self, repo: MediaRepository, storage: Dict[str, Storage]) -> None:
        self.repo = repo
        self.storages = storage

    def create(self, media : MediaFile, storage_name: str, content: bytes) -> str:
        storage = self.storages[storage_name]
        ref = storage.save(media,content)

        self.repo.add(MediaRecord(media = media, storage_ref = ref, storage_name=storage_name))
        return media.id.value
    
    def rename(self, media_id: str, new_name: str) -> None:
        record = self.repo.get(media_id)
        record.media.rename(new_name)

    def delete(self, media_id: str) -> None:
        record = self.repo.get(media_id)
        storage = self.storages[record.storage_name]

        record.media.mark_deleted()
        storage.delete(record.storage_ref)
        self.repo.delete(media_id)

    def convert(self, media_id: str, target_format: str) -> None:
        raise NotImplemented
    
    def extract_features(self, media_id: str) -> Dict[str, Any]:
        record = self.repo.get(media_id)
        return {
            "media_id": record.media.id.value,
            "kind" : record.media.kind,
            "meta": record.media.metadata(),
            "features": {"stub": True},
        }
    
    