from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertGroup")


@_attrs_define
class AlertGroup:
    """
    Attributes:
        name (str): The name of the alert group
        description (Union[None, str]): The description of the alert group
        slug (str): The slug of the alert group
        condition_type (str): Grouping condition for the alert group
        time_window (int): Time window for the alert grouping
        group_by_alert_title (bool): Whether the alerts are grouped by title or not
        group_by_alert_urgency (bool): Whether the alerts are grouped by urgency or not
        created_at (str): Date of creation
        updated_at (str): Date of last update
        deleted_at (Union[None, str]): Date or deletion
    """

    name: str
    description: Union[None, str]
    slug: str
    condition_type: str
    time_window: int
    group_by_alert_title: bool
    group_by_alert_urgency: bool
    created_at: str
    updated_at: str
    deleted_at: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, str]
        description = self.description

        slug = self.slug

        condition_type = self.condition_type

        time_window = self.time_window

        group_by_alert_title = self.group_by_alert_title

        group_by_alert_urgency = self.group_by_alert_urgency

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "slug": slug,
                "condition_type": condition_type,
                "time_window": time_window,
                "group_by_alert_title": group_by_alert_title,
                "group_by_alert_urgency": group_by_alert_urgency,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        slug = d.pop("slug")

        condition_type = d.pop("condition_type")

        time_window = d.pop("time_window")

        group_by_alert_title = d.pop("group_by_alert_title")

        group_by_alert_urgency = d.pop("group_by_alert_urgency")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        alert_group = cls(
            name=name,
            description=description,
            slug=slug,
            condition_type=condition_type,
            time_window=time_window,
            group_by_alert_title=group_by_alert_title,
            group_by_alert_urgency=group_by_alert_urgency,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        alert_group.additional_properties = d
        return alert_group

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
