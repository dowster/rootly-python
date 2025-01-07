from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEscalationPolicyDataAttributes")


@_attrs_define
class UpdateEscalationPolicyDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the escalation policy
        description (Union[None, Unset, str]): The description of the escalation policy
        repeat_count (Union[Unset, int]): The number of times this policy will be executed until someone acknowledges
            the alert
        group_ids (Union[Unset, list[str]]): Associated groups (alerting the group will trigger escalation policy)
        service_ids (Union[Unset, list[str]]): Associated services (alerting the service will trigger escalation policy)
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    repeat_count: Union[Unset, int] = UNSET
    group_ids: Union[Unset, list[str]] = UNSET
    service_ids: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        repeat_count = self.repeat_count

        group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        service_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if repeat_count is not UNSET:
            field_dict["repeat_count"] = repeat_count
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        repeat_count = d.pop("repeat_count", UNSET)

        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        update_escalation_policy_data_attributes = cls(
            name=name,
            description=description,
            repeat_count=repeat_count,
            group_ids=group_ids,
            service_ids=service_ids,
        )

        return update_escalation_policy_data_attributes
