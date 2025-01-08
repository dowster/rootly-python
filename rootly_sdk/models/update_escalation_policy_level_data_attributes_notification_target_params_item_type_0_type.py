from enum import Enum


class UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type(str, Enum):
    SCHEDULE = "schedule"
    SLACK_CHANNEL = "slack_channel"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
