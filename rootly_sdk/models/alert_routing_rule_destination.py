from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_routing_rule_destination_target_type import AlertRoutingRuleDestinationTargetType

T = TypeVar("T", bound="AlertRoutingRuleDestination")


@_attrs_define
class AlertRoutingRuleDestination:
    """The destinations for the alert routing rule

    Attributes:
        target_type (AlertRoutingRuleDestinationTargetType): The type of the target
        target_id (UUID): The ID of the target
    """

    target_type: AlertRoutingRuleDestinationTargetType
    target_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        target_id = str(self.target_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_type": target_type,
                "target_id": target_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        target_type = AlertRoutingRuleDestinationTargetType(d.pop("target_type"))

        target_id = UUID(d.pop("target_id"))

        alert_routing_rule_destination = cls(
            target_type=target_type,
            target_id=target_id,
        )

        alert_routing_rule_destination.additional_properties = d
        return alert_routing_rule_destination

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
