from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_alert_group_data_attributes_condition_type import NewAlertGroupDataAttributesConditionType
from ..models.new_alert_group_data_attributes_group_by_alert_title import NewAlertGroupDataAttributesGroupByAlertTitle
from ..models.new_alert_group_data_attributes_group_by_alert_urgency import (
    NewAlertGroupDataAttributesGroupByAlertUrgency,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_group_data_attributes_alert_group_targets_attributes import (
        NewAlertGroupDataAttributesAlertGroupTargetsAttributes,
    )


T = TypeVar("T", bound="NewAlertGroupDataAttributes")


@_attrs_define
class NewAlertGroupDataAttributes:
    """
    Attributes:
        name (str): The name of the alert group
        alert_group_targets_attributes (NewAlertGroupDataAttributesAlertGroupTargetsAttributes): Attributes for alert
            group targets
        description (Union[None, Unset, str]): The description of the alert urgency
        time_window (Union[Unset, int]): The length of time an Alert Group should stay open and accept new alerts
        group_by_alert_title (Union[Unset, NewAlertGroupDataAttributesGroupByAlertTitle]): Whether the alerts should be
            grouped by titles.
        group_by_alert_urgency (Union[Unset, NewAlertGroupDataAttributesGroupByAlertUrgency]): Whether the alerts should
            be grouped by urgencies.
        condition_type (Union[Unset, NewAlertGroupDataAttributesConditionType]): Group alerts when ANY or ALL of the
            fields are matching.
    """

    name: str
    alert_group_targets_attributes: "NewAlertGroupDataAttributesAlertGroupTargetsAttributes"
    description: Union[None, Unset, str] = UNSET
    time_window: Union[Unset, int] = UNSET
    group_by_alert_title: Union[Unset, NewAlertGroupDataAttributesGroupByAlertTitle] = UNSET
    group_by_alert_urgency: Union[Unset, NewAlertGroupDataAttributesGroupByAlertUrgency] = UNSET
    condition_type: Union[Unset, NewAlertGroupDataAttributesConditionType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alert_group_targets_attributes = self.alert_group_targets_attributes.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        time_window = self.time_window

        group_by_alert_title: Union[Unset, int] = UNSET
        if not isinstance(self.group_by_alert_title, Unset):
            group_by_alert_title = self.group_by_alert_title.value

        group_by_alert_urgency: Union[Unset, int] = UNSET
        if not isinstance(self.group_by_alert_urgency, Unset):
            group_by_alert_urgency = self.group_by_alert_urgency.value

        condition_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "alert_group_targets_attributes": alert_group_targets_attributes,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if time_window is not UNSET:
            field_dict["time_window"] = time_window
        if group_by_alert_title is not UNSET:
            field_dict["group_by_alert_title"] = group_by_alert_title
        if group_by_alert_urgency is not UNSET:
            field_dict["group_by_alert_urgency"] = group_by_alert_urgency
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.new_alert_group_data_attributes_alert_group_targets_attributes import (
            NewAlertGroupDataAttributesAlertGroupTargetsAttributes,
        )

        d = src_dict.copy()
        name = d.pop("name")

        alert_group_targets_attributes = NewAlertGroupDataAttributesAlertGroupTargetsAttributes.from_dict(
            d.pop("alert_group_targets_attributes")
        )

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        time_window = d.pop("time_window", UNSET)

        _group_by_alert_title = d.pop("group_by_alert_title", UNSET)
        group_by_alert_title: Union[Unset, NewAlertGroupDataAttributesGroupByAlertTitle]
        if isinstance(_group_by_alert_title, Unset):
            group_by_alert_title = UNSET
        else:
            group_by_alert_title = NewAlertGroupDataAttributesGroupByAlertTitle(_group_by_alert_title)

        _group_by_alert_urgency = d.pop("group_by_alert_urgency", UNSET)
        group_by_alert_urgency: Union[Unset, NewAlertGroupDataAttributesGroupByAlertUrgency]
        if isinstance(_group_by_alert_urgency, Unset):
            group_by_alert_urgency = UNSET
        else:
            group_by_alert_urgency = NewAlertGroupDataAttributesGroupByAlertUrgency(_group_by_alert_urgency)

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: Union[Unset, NewAlertGroupDataAttributesConditionType]
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = NewAlertGroupDataAttributesConditionType(_condition_type)

        new_alert_group_data_attributes = cls(
            name=name,
            alert_group_targets_attributes=alert_group_targets_attributes,
            description=description,
            time_window=time_window,
            group_by_alert_title=group_by_alert_title,
            group_by_alert_urgency=group_by_alert_urgency,
            condition_type=condition_type,
        )

        return new_alert_group_data_attributes
