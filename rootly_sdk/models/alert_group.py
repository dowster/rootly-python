from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_group_attributes_item import AlertGroupAttributesItem
    from ..models.alert_group_targets_item import AlertGroupTargetsItem


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
        targets (Union[Unset, list['AlertGroupTargetsItem']]):
        attributes (Union[Unset, list['AlertGroupAttributesItem']]):
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
    targets: Union[Unset, list["AlertGroupTargetsItem"]] = UNSET
    attributes: Union[Unset, list["AlertGroupAttributesItem"]] = UNSET
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

        targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

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
        if targets is not UNSET:
            field_dict["targets"] = targets
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert_group_attributes_item import AlertGroupAttributesItem
        from ..models.alert_group_targets_item import AlertGroupTargetsItem

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

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = AlertGroupTargetsItem.from_dict(targets_item_data)

            targets.append(targets_item)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = AlertGroupAttributesItem.from_dict(attributes_item_data)

            attributes.append(attributes_item)

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
            targets=targets,
            attributes=attributes,
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
