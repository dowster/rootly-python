from enum import Enum


class GeneratePhoneNumberLiveCallRouterPhoneType(str, Enum):
    LOCAL = "local"
    TOLL_FREE = "toll_free"

    def __str__(self) -> str:
        return str(self.value)
