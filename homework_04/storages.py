"""
Класс описывающий хранилища. Можно добавить другие типы в перспективе
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

from homework_04.media_base import MediaFile


@dataclass
class StorageRef:
    #ссылка на расположение файла Url, Path 
    uri: str

#абстрактный интерфейс хранилища: который должны наследовать все типы хранилищ 
class Storage(ABC):

    @abstractmethod
    def save(self, media: MediaFile, content: bytes) -> StorageRef:
        """
        Сохранить байты в хранилище и врнуть ссылку
        Реализация должна уметь сохранять данные на локальный, удаленный или S3 тип хранилища
        """
        raise NotImplementedError
    
    @abstractmethod
    def load(self, ref: StorageRef) -> bytes:
        #Загрузка файла по ссылке
        raise NotImplementedError
    
    @abstractmethod 
    def delete(self, ref: StorageRef) -> None:
        #физическое удаление файла
        raise NotImplementedError
    

class LocalDiskStorage(Storage):

    def __init__(self, root_dir:str) -> None:
        self.root = Path(root_dir)

    def save(self, media: MediaFile, content: bytes) -> StorageRef:
        folder = self.root / media.kind / media.id.value
        folder.mkdir(parents=True,exist_ok=True)
        file_path = folder / media.info.name
        file_path.write_bytes(content)
        return StorageRef(uri = str(file_path))
    
    def load(self, ref: StorageRef) -> bytes:
        return Path(ref.uri).read_bytes
    
    def delete(self, ref: StorageRef) -> None:
        path = Path(ref.uri)
        if path.exists():
            path.unlink()

class RemoteServerStorage(Storage):
    
    def __init__(self, host:str, path: str) -> None:
        self.host = host
        self.path = path

    def save(self, media: MediaFile, content: bytes) -> StorageRef:
        #сохраняем файл в хранилище и поулчаем ссылку
        raise NotImplementedError
    
    def load(self, ref: StorageRef) -> bytes:
        #загрузка файла по uri
        raise NotImplementedError
    
    def delete(self, ref: StorageRef) -> None:
        #удаление файла на сервере
        raise NotImplementedError

class S3Storage(Storage):

    def __init__(self, bucket:str , prefix: str = "") -> None:
        self.bucket = bucket
        self.prefix = prefix.strip("/")

    def save(self, media: MediaFile, content: bytes) -> StorageRef:
        #сохранение файла в удаленном хранилище
        return StorageRef(f"s3://")
    
    def load(self, ref: StorageRef) -> bytes:
        #получение байтов по ссылку
        raise NotImplementedError
    
    def delete(self, ref: StorageRef) -> None:
        #удаление файла
        raise NotImplementedError