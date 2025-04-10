from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_routing_rule_condition_type import AlertRoutingRuleConditionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_routing_rule_conditions_item import AlertRoutingRuleConditionsItem
    from ..models.alert_routing_rule_destination import AlertRoutingRuleDestination


T = TypeVar("T", bound="AlertRoutingRule")


@_attrs_define
class AlertRoutingRule:
    """
    Attributes:
        name (str): The name of the alert routing rule
        enabled (bool): Whether the alert routing rule is enabled
        alerts_source_id (UUID): The ID of the alerts source
        condition_type (AlertRoutingRuleConditionType): The type of condition for the alert routing rule
        destination (AlertRoutingRuleDestination): The destinations for the alert routing rule
        created_at (str): Date of creation
        updated_at (str): Date of last update
        conditions (Union[Unset, list['AlertRoutingRuleConditionsItem']]): The conditions for the alert routing rule
    """

    name: str
    enabled: bool
    alerts_source_id: UUID
    condition_type: AlertRoutingRuleConditionType
    destination: "AlertRoutingRuleDestination"
    created_at: str
    updated_at: str
    conditions: Union[Unset, list["AlertRoutingRuleConditionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        alerts_source_id = str(self.alerts_source_id)

        condition_type = self.condition_type.value

        destination = self.destination.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "enabled": enabled,
                "alerts_source_id": alerts_source_id,
                "condition_type": condition_type,
                "destination": destination,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert_routing_rule_conditions_item import AlertRoutingRuleConditionsItem
        from ..models.alert_routing_rule_destination import AlertRoutingRuleDestination

        d = src_dict.copy()
        name = d.pop("name")

        enabled = d.pop("enabled")

        alerts_source_id = UUID(d.pop("alerts_source_id"))

        condition_type = AlertRoutingRuleConditionType(d.pop("condition_type"))

        destination = AlertRoutingRuleDestination.from_dict(d.pop("destination"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = AlertRoutingRuleConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        alert_routing_rule = cls(
            name=name,
            enabled=enabled,
            alerts_source_id=alerts_source_id,
            condition_type=condition_type,
            destination=destination,
            created_at=created_at,
            updated_at=updated_at,
            conditions=conditions,
        )

        alert_routing_rule.additional_properties = d
        return alert_routing_rule

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
