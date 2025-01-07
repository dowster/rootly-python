from enum import Enum


class ListUsersInclude(str, Enum):
    DEVICES = "devices"
    EMAIL_ADDRESSES = "email_addresses"
    PHONE_NUMBERS = "phone_numbers"

    def __str__(self) -> str:
        return str(self.value)
