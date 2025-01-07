from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_to_slack_channel_opsgenie_task_params_task_type import (
    InviteToSlackChannelOpsgenieTaskParamsTaskType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invite_to_slack_channel_opsgenie_task_params_channels_item import (
        InviteToSlackChannelOpsgenieTaskParamsChannelsItem,
    )
    from ..models.invite_to_slack_channel_opsgenie_task_params_schedule import (
        InviteToSlackChannelOpsgenieTaskParamsSchedule,
    )


T = TypeVar("T", bound="InviteToSlackChannelOpsgenieTaskParams")


@_attrs_define
class InviteToSlackChannelOpsgenieTaskParams:
    """
    Attributes:
        schedule (InviteToSlackChannelOpsgenieTaskParamsSchedule):
        task_type (Union[Unset, InviteToSlackChannelOpsgenieTaskParamsTaskType]):
        channels (Union[Unset, list['InviteToSlackChannelOpsgenieTaskParamsChannelsItem']]):
    """

    schedule: "InviteToSlackChannelOpsgenieTaskParamsSchedule"
    task_type: Union[Unset, InviteToSlackChannelOpsgenieTaskParamsTaskType] = UNSET
    channels: Union[Unset, list["InviteToSlackChannelOpsgenieTaskParamsChannelsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule = self.schedule.to_dict()

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.value

        channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule": schedule,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.invite_to_slack_channel_opsgenie_task_params_channels_item import (
            InviteToSlackChannelOpsgenieTaskParamsChannelsItem,
        )
        from ..models.invite_to_slack_channel_opsgenie_task_params_schedule import (
            InviteToSlackChannelOpsgenieTaskParamsSchedule,
        )

        d = src_dict.copy()
        schedule = InviteToSlackChannelOpsgenieTaskParamsSchedule.from_dict(d.pop("schedule"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, InviteToSlackChannelOpsgenieTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = InviteToSlackChannelOpsgenieTaskParamsTaskType(_task_type)

        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = InviteToSlackChannelOpsgenieTaskParamsChannelsItem.from_dict(channels_item_data)

            channels.append(channels_item)

        invite_to_slack_channel_opsgenie_task_params = cls(
            schedule=schedule,
            task_type=task_type,
            channels=channels,
        )

        invite_to_slack_channel_opsgenie_task_params.additional_properties = d
        return invite_to_slack_channel_opsgenie_task_params

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
