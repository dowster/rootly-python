from enum import Enum


class CreateShortcutStoryTaskParamsKind(str, Enum):
    BUG = "bug"
    CHORE = "chore"
    FEATURE = "feature"

    def __str__(self) -> str:
        return str(self.value)
