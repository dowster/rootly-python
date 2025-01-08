from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
        NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
    )


T = TypeVar("T", bound="NewEscalationPolicyLevelDataAttributes")


@_attrs_define
class NewEscalationPolicyLevelDataAttributes:
    """
    Attributes:
        position (int): Position of the escalation policy level
        notification_target_params
            (list[Union['NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0', None]]): Escalation
            level's notification targets
        delay (Union[Unset, int]): Delay before notification targets will be alerted.
        escalation_policy_path_id (Union[None, Unset, str]): The ID of the dynamic escalation policy path the level will
            belong to. If nothing is specified it will add the level to your default path.
    """

    position: int
    notification_target_params: list[
        Union["NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None]
    ]
    delay: Union[Unset, int] = UNSET
    escalation_policy_path_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
            NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
        )

        position = self.position

        notification_target_params = []
        for notification_target_params_item_data in self.notification_target_params:
            notification_target_params_item: Union[None, dict[str, Any]]
            if isinstance(
                notification_target_params_item_data,
                NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
            ):
                notification_target_params_item = notification_target_params_item_data.to_dict()
            else:
                notification_target_params_item = notification_target_params_item_data
            notification_target_params.append(notification_target_params_item)

        delay = self.delay

        escalation_policy_path_id: Union[None, Unset, str]
        if isinstance(self.escalation_policy_path_id, Unset):
            escalation_policy_path_id = UNSET
        else:
            escalation_policy_path_id = self.escalation_policy_path_id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "position": position,
                "notification_target_params": notification_target_params,
            }
        )
        if delay is not UNSET:
            field_dict["delay"] = delay
        if escalation_policy_path_id is not UNSET:
            field_dict["escalation_policy_path_id"] = escalation_policy_path_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.new_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
            NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
        )

        d = src_dict.copy()
        position = d.pop("position")

        notification_target_params = []
        _notification_target_params = d.pop("notification_target_params")
        for notification_target_params_item_data in _notification_target_params:

            def _parse_notification_target_params_item(
                data: object,
            ) -> Union["NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    notification_target_params_item_type_0 = (
                        NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0.from_dict(data)
                    )

                    return notification_target_params_item_type_0
                except:  # noqa: E722
                    pass
                return cast(
                    Union["NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None], data
                )

            notification_target_params_item = _parse_notification_target_params_item(
                notification_target_params_item_data
            )

            notification_target_params.append(notification_target_params_item)

        delay = d.pop("delay", UNSET)

        def _parse_escalation_policy_path_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        escalation_policy_path_id = _parse_escalation_policy_path_id(d.pop("escalation_policy_path_id", UNSET))

        new_escalation_policy_level_data_attributes = cls(
            position=position,
            notification_target_params=notification_target_params,
            delay=delay,
            escalation_policy_path_id=escalation_policy_path_id,
        )

        return new_escalation_policy_level_data_attributes
