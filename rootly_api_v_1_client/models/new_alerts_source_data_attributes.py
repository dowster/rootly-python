from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_alerts_source_data_attributes_source_type import NewAlertsSourceDataAttributesSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item import (
        NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem,
    )
    from ..models.new_alerts_source_data_attributes_sourceable_attributes import (
        NewAlertsSourceDataAttributesSourceableAttributes,
    )


T = TypeVar("T", bound="NewAlertsSourceDataAttributes")


@_attrs_define
class NewAlertsSourceDataAttributes:
    """
    Attributes:
        name (str): The name of the alert source
        source_type (Union[Unset, NewAlertsSourceDataAttributesSourceType]): The alert source type
        alert_urgency_id (Union[Unset, str]): ID for the default alert urgency assigned to this alert source
        alert_source_urgency_rules_attributes (Union[Unset,
            list['NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem']]): List of rules that define the
            conditions under which the alert urgency will be set automatically based on the alert payload
        sourceable_attributes (Union[Unset, NewAlertsSourceDataAttributesSourceableAttributes]): Provide additional
            attributes for generic_webhook alerts source
    """

    name: str
    source_type: Union[Unset, NewAlertsSourceDataAttributesSourceType] = UNSET
    alert_urgency_id: Union[Unset, str] = UNSET
    alert_source_urgency_rules_attributes: Union[
        Unset, list["NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem"]
    ] = UNSET
    sourceable_attributes: Union[Unset, "NewAlertsSourceDataAttributesSourceableAttributes"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        alert_urgency_id = self.alert_urgency_id

        alert_source_urgency_rules_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.alert_source_urgency_rules_attributes, Unset):
            alert_source_urgency_rules_attributes = []
            for alert_source_urgency_rules_attributes_item_data in self.alert_source_urgency_rules_attributes:
                alert_source_urgency_rules_attributes_item = alert_source_urgency_rules_attributes_item_data.to_dict()
                alert_source_urgency_rules_attributes.append(alert_source_urgency_rules_attributes_item)

        sourceable_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sourceable_attributes, Unset):
            sourceable_attributes = self.sourceable_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if alert_source_urgency_rules_attributes is not UNSET:
            field_dict["alert_source_urgency_rules_attributes"] = alert_source_urgency_rules_attributes
        if sourceable_attributes is not UNSET:
            field_dict["sourceable_attributes"] = sourceable_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.new_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item import (
            NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem,
        )
        from ..models.new_alerts_source_data_attributes_sourceable_attributes import (
            NewAlertsSourceDataAttributesSourceableAttributes,
        )

        d = src_dict.copy()
        name = d.pop("name")

        _source_type = d.pop("source_type", UNSET)
        source_type: Union[Unset, NewAlertsSourceDataAttributesSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = NewAlertsSourceDataAttributesSourceType(_source_type)

        alert_urgency_id = d.pop("alert_urgency_id", UNSET)

        alert_source_urgency_rules_attributes = []
        _alert_source_urgency_rules_attributes = d.pop("alert_source_urgency_rules_attributes", UNSET)
        for alert_source_urgency_rules_attributes_item_data in _alert_source_urgency_rules_attributes or []:
            alert_source_urgency_rules_attributes_item = (
                NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem.from_dict(
                    alert_source_urgency_rules_attributes_item_data
                )
            )

            alert_source_urgency_rules_attributes.append(alert_source_urgency_rules_attributes_item)

        _sourceable_attributes = d.pop("sourceable_attributes", UNSET)
        sourceable_attributes: Union[Unset, NewAlertsSourceDataAttributesSourceableAttributes]
        if isinstance(_sourceable_attributes, Unset):
            sourceable_attributes = UNSET
        else:
            sourceable_attributes = NewAlertsSourceDataAttributesSourceableAttributes.from_dict(_sourceable_attributes)

        new_alerts_source_data_attributes = cls(
            name=name,
            source_type=source_type,
            alert_urgency_id=alert_urgency_id,
            alert_source_urgency_rules_attributes=alert_source_urgency_rules_attributes,
            sourceable_attributes=sourceable_attributes,
        )

        return new_alerts_source_data_attributes
