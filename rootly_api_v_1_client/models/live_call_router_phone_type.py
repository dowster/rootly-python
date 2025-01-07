from enum import Enum


class LiveCallRouterPhoneType(str, Enum):
    LOCAL = "local"
    TOLL_FREE = "toll_free"

    def __str__(self) -> str:
        return str(self.value)
