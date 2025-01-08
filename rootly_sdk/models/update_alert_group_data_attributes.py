from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_alert_group_data_attributes_condition_type import UpdateAlertGroupDataAttributesConditionType
from ..models.update_alert_group_data_attributes_group_by_alert_title import (
    UpdateAlertGroupDataAttributesGroupByAlertTitle,
)
from ..models.update_alert_group_data_attributes_group_by_alert_urgency import (
    UpdateAlertGroupDataAttributesGroupByAlertUrgency,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_group_data_attributes_alert_group_targets_attributes import (
        UpdateAlertGroupDataAttributesAlertGroupTargetsAttributes,
    )


T = TypeVar("T", bound="UpdateAlertGroupDataAttributes")


@_attrs_define
class UpdateAlertGroupDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the alert group
        description (Union[None, Unset, str]): The description of the alert group
        time_window (Union[Unset, int]): The length of time an Alert Group should stay open and accept new alerts
        alert_group_targets_attributes (Union[Unset, UpdateAlertGroupDataAttributesAlertGroupTargetsAttributes]):
            Attributes for alert group targets
        group_by_alert_title (Union[Unset, UpdateAlertGroupDataAttributesGroupByAlertTitle]): Whether the alerts should
            be grouped by titles.
        group_by_alert_urgency (Union[Unset, UpdateAlertGroupDataAttributesGroupByAlertUrgency]): Whether the alerts
            should be grouped by urgencies.
        condition_type (Union[Unset, UpdateAlertGroupDataAttributesConditionType]): Group alerts when ANY or ALL of the
            fields are matching.
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    time_window: Union[Unset, int] = UNSET
    alert_group_targets_attributes: Union[Unset, "UpdateAlertGroupDataAttributesAlertGroupTargetsAttributes"] = UNSET
    group_by_alert_title: Union[Unset, UpdateAlertGroupDataAttributesGroupByAlertTitle] = UNSET
    group_by_alert_urgency: Union[Unset, UpdateAlertGroupDataAttributesGroupByAlertUrgency] = UNSET
    condition_type: Union[Unset, UpdateAlertGroupDataAttributesConditionType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        time_window = self.time_window

        alert_group_targets_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.alert_group_targets_attributes, Unset):
            alert_group_targets_attributes = self.alert_group_targets_attributes.to_dict()

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if time_window is not UNSET:
            field_dict["time_window"] = time_window
        if alert_group_targets_attributes is not UNSET:
            field_dict["alert_group_targets_attributes"] = alert_group_targets_attributes
        if group_by_alert_title is not UNSET:
            field_dict["group_by_alert_title"] = group_by_alert_title
        if group_by_alert_urgency is not UNSET:
            field_dict["group_by_alert_urgency"] = group_by_alert_urgency
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_alert_group_data_attributes_alert_group_targets_attributes import (
            UpdateAlertGroupDataAttributesAlertGroupTargetsAttributes,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        time_window = d.pop("time_window", UNSET)

        _alert_group_targets_attributes = d.pop("alert_group_targets_attributes", UNSET)
        alert_group_targets_attributes: Union[Unset, UpdateAlertGroupDataAttributesAlertGroupTargetsAttributes]
        if isinstance(_alert_group_targets_attributes, Unset):
            alert_group_targets_attributes = UNSET
        else:
            alert_group_targets_attributes = UpdateAlertGroupDataAttributesAlertGroupTargetsAttributes.from_dict(
                _alert_group_targets_attributes
            )

        _group_by_alert_title = d.pop("group_by_alert_title", UNSET)
        group_by_alert_title: Union[Unset, UpdateAlertGroupDataAttributesGroupByAlertTitle]
        if isinstance(_group_by_alert_title, Unset):
            group_by_alert_title = UNSET
        else:
            group_by_alert_title = UpdateAlertGroupDataAttributesGroupByAlertTitle(_group_by_alert_title)

        _group_by_alert_urgency = d.pop("group_by_alert_urgency", UNSET)
        group_by_alert_urgency: Union[Unset, UpdateAlertGroupDataAttributesGroupByAlertUrgency]
        if isinstance(_group_by_alert_urgency, Unset):
            group_by_alert_urgency = UNSET
        else:
            group_by_alert_urgency = UpdateAlertGroupDataAttributesGroupByAlertUrgency(_group_by_alert_urgency)

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: Union[Unset, UpdateAlertGroupDataAttributesConditionType]
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = UpdateAlertGroupDataAttributesConditionType(_condition_type)

        update_alert_group_data_attributes = cls(
            name=name,
            description=description,
            time_window=time_window,
            alert_group_targets_attributes=alert_group_targets_attributes,
            group_by_alert_title=group_by_alert_title,
            group_by_alert_urgency=group_by_alert_urgency,
            condition_type=condition_type,
        )

        return update_alert_group_data_attributes
