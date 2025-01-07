from enum import Enum


class CreateShortcutStoryTaskParamsTaskType(str, Enum):
    CREATE_SHORTCUT_STORY = "create_shortcut_story"

    def __str__(self) -> str:
        return str(self.value)
