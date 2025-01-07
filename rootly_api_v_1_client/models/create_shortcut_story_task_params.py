from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_shortcut_story_task_params_kind import CreateShortcutStoryTaskParamsKind
from ..models.create_shortcut_story_task_params_task_type import CreateShortcutStoryTaskParamsTaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_shortcut_story_task_params_archivation import CreateShortcutStoryTaskParamsArchivation
    from ..models.create_shortcut_story_task_params_project import CreateShortcutStoryTaskParamsProject


T = TypeVar("T", bound="CreateShortcutStoryTaskParams")


@_attrs_define
class CreateShortcutStoryTaskParams:
    """
    Attributes:
        title (str): The incident title
        kind (CreateShortcutStoryTaskParamsKind):
        archivation (CreateShortcutStoryTaskParamsArchivation): The archivation id and display name
        project (CreateShortcutStoryTaskParamsProject): The project id and display name
        task_type (Union[Unset, CreateShortcutStoryTaskParamsTaskType]):
        description (Union[Unset, str]): The incident description
        labels (Union[Unset, str]): The story labels
        due_date (Union[Unset, str]): The due date
    """

    title: str
    kind: CreateShortcutStoryTaskParamsKind
    archivation: "CreateShortcutStoryTaskParamsArchivation"
    project: "CreateShortcutStoryTaskParamsProject"
    task_type: Union[Unset, CreateShortcutStoryTaskParamsTaskType] = UNSET
    description: Union[Unset, str] = UNSET
    labels: Union[Unset, str] = UNSET
    due_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        kind = self.kind.value

        archivation = self.archivation.to_dict()

        project = self.project.to_dict()

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        description = self.description

        labels = self.labels

        due_date = self.due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "kind": kind,
                "archivation": archivation,
                "project": project,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_shortcut_story_task_params_archivation import CreateShortcutStoryTaskParamsArchivation
        from ..models.create_shortcut_story_task_params_project import CreateShortcutStoryTaskParamsProject

        d = src_dict.copy()
        title = d.pop("title")

        kind = CreateShortcutStoryTaskParamsKind(d.pop("kind"))

        archivation = CreateShortcutStoryTaskParamsArchivation.from_dict(d.pop("archivation"))

        project = CreateShortcutStoryTaskParamsProject.from_dict(d.pop("project"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, CreateShortcutStoryTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = CreateShortcutStoryTaskParamsTaskType(_task_type)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        due_date = d.pop("due_date", UNSET)

        create_shortcut_story_task_params = cls(
            title=title,
            kind=kind,
            archivation=archivation,
            project=project,
            task_type=task_type,
            description=description,
            labels=labels,
            due_date=due_date,
        )

        create_shortcut_story_task_params.additional_properties = d
        return create_shortcut_story_task_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
