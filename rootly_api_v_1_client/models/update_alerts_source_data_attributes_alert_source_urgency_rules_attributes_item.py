from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item_operator import (
    UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem")


@_attrs_define
class UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItem:
    """
    Attributes:
        json_path (Union[Unset, str]): JSON path expression to extract a specific value from the alert's payload for
            evaluation
        operator (Union[Unset, UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator]):
            Comparison operator used to evaluate the extracted value against the specified condition
        value (Union[Unset, str]): Value that the extracted payload data is compared to using the specified operator to
            determine a match
    """

    json_path: Union[Unset, str] = UNSET
    operator: Union[Unset, UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_path = self.json_path

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if json_path is not UNSET:
            field_dict["json_path"] = json_path
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        json_path = d.pop("json_path", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = UpdateAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributesItemOperator(_operator)

        value = d.pop("value", UNSET)

        update_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item = cls(
            json_path=json_path,
            operator=operator,
            value=value,
        )

        update_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item.additional_properties = d
        return update_alerts_source_data_attributes_alert_source_urgency_rules_attributes_item

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
