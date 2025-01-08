from enum import Enum


class LiveCallRouterCountryCode(str, Enum):
    AU = "AU"
    CA = "CA"
    GB = "GB"
    NZ = "NZ"
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
