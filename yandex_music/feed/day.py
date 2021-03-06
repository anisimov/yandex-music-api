from typing import TYPE_CHECKING, Optional, List

from yandex_music import YandexMusicObject

if TYPE_CHECKING:
    from yandex_music import Client, Event, Track, TrackWithAds


class Day(YandexMusicObject):
    """Класс, представляющий .

    Attributes:
        client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

    Args:
        client (:obj:`yandex_music.Client`, optional): Объект класса :class:`yandex_music.Client`, представляющий клиент
            Yandex Music.
        **kwargs: Произвольные ключевые аргументы полученные от API.
    """

    def __init__(self,
                 day: str,
                 events: List['Event'],
                 tracks_to_play_with_ads: List['TrackWithAds'],
                 tracks_to_play: List['Track'],
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.day = day
        self.events = events
        self.tracks_to_play_with_ads = tracks_to_play_with_ads
        self.tracks_to_play = tracks_to_play

        self.client = client
        self._id_attrs = (self.day, self.events, self.tracks_to_play_with_ads, self.tracks_to_play)

    @classmethod
    def de_json(cls, data: dict, client: 'Client') -> Optional['Day']:
        """Десериализация объекта.

        Args:
            data (:obj:`dict`): Поля и значения десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`yandex_music.Day`: Объект класса :class:`yandex_music.Day`.
        """
        if not data:
            return None

        data = super(Day, cls).de_json(data, client)
        from yandex_music import Event, Track, TrackWithAds
        data['events'] = Event.de_list(data.get('events'), client)
        data['tracks_to_play_with_ads'] = TrackWithAds.de_list(data.get('tracks_to_play_with_ads'), client)
        data['tracks_to_play'] = Track.de_list(data.get('tracks_to_play'), client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client') -> List['Day']:
        """Десериализация списка объектов.

        Args:
            data (:obj:`list`): Список словарей с полями и значениями десериализуемого объекта.
            client (:obj:`yandex_music.Client`): Объект класса :class:`yandex_music.Client`, представляющий клиент
                Yandex Music.

        Returns:
            :obj:`list` из :obj:`yandex_music.Day`: Список объектов класса :class:`yandex_music.Day`.
        """
        if not data:
            return []

        days = list()
        for day in data:
            days.append(cls.de_json(day, client))

        return days
