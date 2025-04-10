from enum import Enum


class UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers(str, Enum):
    ADMINS = "admins"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
