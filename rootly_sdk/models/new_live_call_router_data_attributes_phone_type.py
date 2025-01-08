from enum import Enum


class NewLiveCallRouterDataAttributesPhoneType(str, Enum):
    LOCAL = "local"
    TOLL_FREE = "toll_free"

    def __str__(self) -> str:
        return str(self.value)
