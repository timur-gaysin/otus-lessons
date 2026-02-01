from datetime import datetime
from homework_04.media_base import FileInfo
from homework_04.media_types import AudioFile, AudioMeta, PhotoFile, PhotoMeta
from homework_04.services import MediaRepository, MediaService
from homework_04.storages import LocalDiskStorage, RemoteServerStorage, S3Storage


def main():
    #пример хранилища - локальный, удаленный и S3
    storages = {
        "local":LocalDiskStorage(root_dir="C:/workspace/otus/homework_04/storage"),
        "remote":RemoteServerStorage(host="it-notepad.com", path = "data/media"),
        "s3":S3Storage(bucket="own_backet", prefix="otus")
    }

    repo = MediaRepository()
    service = MediaService(repo = repo, storage = storages)
    
    #Создание файла
    audio_info = FileInfo (
        name = "song.mp3",
        size_bytes=123_456,
        created_at=datetime.utcnow(),
        owner="ivanov",
        mime_type="audio/mpeg",
    )

    audio= AudioFile(audio_info,AudioMeta(duration_sec=210,sample_rate_hz=44100,channels=2,codec="wav"))

    audio_id = service.create(audio,storage_name="local", content=b" ... wav bytes...")
    print("created audio : ",audio_id)    

    #переименовывание
    service.rename(audio_id,"new_name.wav")

    #извлечение фич
    feats = service.extract_features(audio_id)
    print("Features: ",feats)

    #создание фото в S3 хранилище
    photo_info = FileInfo(
        name = "pic.jpg",
        size_bytes=10_000,
        created_at=datetime.utcnow(),
        owner = "petrov",
        mime_type="image/jpeg"
    )

    photo = PhotoFile(photo_info, PhotoMeta(width = 1920,height=1080,camera_model="Canon", iso = 100))
    photo_id = service.create(photo,storage_name="s3", content = b"...jpg bytes")

    print("Created photo: ", photo_id)

    #удаление
    service.delete(audio_id)


if __name__ == "__main__":
    main()
    