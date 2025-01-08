from enum import Enum


class AlertTriggerParamsTriggersItem(str, Enum):
    ALERT_CREATED = "alert_created"

    def __str__(self) -> str:
        return str(self.value)
