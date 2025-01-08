from enum import IntEnum


class UpdateStatusPageDataAttributesShowUptimeLastDays(IntEnum):
    VALUE_30 = 30
    VALUE_60 = 60
    VALUE_90 = 90
    VALUE_180 = 180
    VALUE_360 = 360

    def __str__(self) -> str:
        return str(self.value)
