from telebot.types import Message, Sticker

from typing import List, Dict


class User:
    users = dict()

    def __init__(self, user_id: int) -> None:
        User.add_user(user_id, self)

        self.user_id: int = user_id

        self.show_photo: bool = False
        self.number_of_photo: int = 0

        self.command: str = ''
        self.location: str = ''
        self.location_id: str = ''
        self.language_code: str = 'en_US'
        self.currency: str = 'USD'
        self.page_size: int = 15
        self.page_number: int = 1
        self.arrival_date: str = ''
        self.departure_date: str = ''
        self.nights_number: int = 0

        self.price_min: str = ''
        self.price_max: str = ''
        self.max_distance: str = ''

        self.message_to_delete: Message | None = None
        self.sticker_to_delete_id: Sticker | None = None
        self.message: Message | None = None

        self.location_id_with_locations_name: Dict = dict()
        self.hotels_list: List = []
        self.sorted_list_by_distance: List = []
        self.hotels_count: int = 0

    @classmethod
    def add_user(cls, user_id: int, user: 'User'):
        cls.users[user_id] = user

    @staticmethod
    def get_user(user_id: int) -> 'User':
        if User.users.get(user_id) is None:
            new_user = User(user_id)
            return new_user
        return User.users.get(user_id)
