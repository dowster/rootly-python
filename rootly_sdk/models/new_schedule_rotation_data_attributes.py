from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_schedule_rotation_data_attributes_active_days_item import (
    NewScheduleRotationDataAttributesActiveDaysItem,
)
from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_type import (
    NewScheduleRotationDataAttributesScheduleRotationableType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_data_attributes_active_time_attributes_item import (
        NewScheduleRotationDataAttributesActiveTimeAttributesItem,
    )
    from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0 import (
        NewScheduleRotationDataAttributesScheduleRotationableAttributesType0,
    )
    from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 import (
        NewScheduleRotationDataAttributesScheduleRotationableAttributesType1,
    )
    from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_2 import (
        NewScheduleRotationDataAttributesScheduleRotationableAttributesType2,
    )
    from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3 import (
        NewScheduleRotationDataAttributesScheduleRotationableAttributesType3,
    )


T = TypeVar("T", bound="NewScheduleRotationDataAttributes")


@_attrs_define
class NewScheduleRotationDataAttributes:
    """
    Attributes:
        name (str): The name of the schedule rotation
        schedule_rotationable_type (NewScheduleRotationDataAttributesScheduleRotationableType): Schedule rotation type
        schedule_rotationable_attributes (Union['NewScheduleRotationDataAttributesScheduleRotationableAttributesType0',
            'NewScheduleRotationDataAttributesScheduleRotationableAttributesType1',
            'NewScheduleRotationDataAttributesScheduleRotationableAttributesType2',
            'NewScheduleRotationDataAttributesScheduleRotationableAttributesType3']):
        position (Union[Unset, int]): Position of the schedule rotation
        active_all_week (Union[Unset, bool]): Schedule rotation active all week? Default: True.
        active_days (Union[Unset, list[NewScheduleRotationDataAttributesActiveDaysItem]]):
        active_time_type (Union[Unset, str]):
        active_time_attributes (Union[Unset, list['NewScheduleRotationDataAttributesActiveTimeAttributesItem']]):
            Schedule rotation's active times
        time_zone (Union[Unset, str]): A valid IANA time zone name. Default: 'Etc/UTC'.
    """

    name: str
    schedule_rotationable_type: NewScheduleRotationDataAttributesScheduleRotationableType
    schedule_rotationable_attributes: Union[
        "NewScheduleRotationDataAttributesScheduleRotationableAttributesType0",
        "NewScheduleRotationDataAttributesScheduleRotationableAttributesType1",
        "NewScheduleRotationDataAttributesScheduleRotationableAttributesType2",
        "NewScheduleRotationDataAttributesScheduleRotationableAttributesType3",
    ]
    position: Union[Unset, int] = UNSET
    active_all_week: Union[Unset, bool] = True
    active_days: Union[Unset, list[NewScheduleRotationDataAttributesActiveDaysItem]] = UNSET
    active_time_type: Union[Unset, str] = UNSET
    active_time_attributes: Union[Unset, list["NewScheduleRotationDataAttributesActiveTimeAttributesItem"]] = UNSET
    time_zone: Union[Unset, str] = "Etc/UTC"

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0 import (
            NewScheduleRotationDataAttributesScheduleRotationableAttributesType0,
        )
        from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 import (
            NewScheduleRotationDataAttributesScheduleRotationableAttributesType1,
        )
        from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_2 import (
            NewScheduleRotationDataAttributesScheduleRotationableAttributesType2,
        )

        name = self.name

        schedule_rotationable_type = self.schedule_rotationable_type.value

        schedule_rotationable_attributes: dict[str, Any]
        if isinstance(
            self.schedule_rotationable_attributes, NewScheduleRotationDataAttributesScheduleRotationableAttributesType0
        ):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        elif isinstance(
            self.schedule_rotationable_attributes, NewScheduleRotationDataAttributesScheduleRotationableAttributesType1
        ):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        elif isinstance(
            self.schedule_rotationable_attributes, NewScheduleRotationDataAttributesScheduleRotationableAttributesType2
        ):
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()
        else:
            schedule_rotationable_attributes = self.schedule_rotationable_attributes.to_dict()

        position = self.position

        active_all_week = self.active_all_week

        active_days: Union[Unset, list[str]] = UNSET
        if not isinstance(self.active_days, Unset):
            active_days = []
            for active_days_item_data in self.active_days:
                active_days_item = active_days_item_data.value
                active_days.append(active_days_item)

        active_time_type = self.active_time_type

        active_time_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.active_time_attributes, Unset):
            active_time_attributes = []
            for active_time_attributes_item_data in self.active_time_attributes:
                active_time_attributes_item = active_time_attributes_item_data.to_dict()
                active_time_attributes.append(active_time_attributes_item)

        time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "schedule_rotationable_type": schedule_rotationable_type,
                "schedule_rotationable_attributes": schedule_rotationable_attributes,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if active_all_week is not UNSET:
            field_dict["active_all_week"] = active_all_week
        if active_days is not UNSET:
            field_dict["active_days"] = active_days
        if active_time_type is not UNSET:
            field_dict["active_time_type"] = active_time_type
        if active_time_attributes is not UNSET:
            field_dict["active_time_attributes"] = active_time_attributes
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.new_schedule_rotation_data_attributes_active_time_attributes_item import (
            NewScheduleRotationDataAttributesActiveTimeAttributesItem,
        )
        from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0 import (
            NewScheduleRotationDataAttributesScheduleRotationableAttributesType0,
        )
        from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 import (
            NewScheduleRotationDataAttributesScheduleRotationableAttributesType1,
        )
        from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_2 import (
            NewScheduleRotationDataAttributesScheduleRotationableAttributesType2,
        )
        from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3 import (
            NewScheduleRotationDataAttributesScheduleRotationableAttributesType3,
        )

        d = src_dict.copy()
        name = d.pop("name")

        schedule_rotationable_type = NewScheduleRotationDataAttributesScheduleRotationableType(
            d.pop("schedule_rotationable_type")
        )

        def _parse_schedule_rotationable_attributes(
            data: object,
        ) -> Union[
            "NewScheduleRotationDataAttributesScheduleRotationableAttributesType0",
            "NewScheduleRotationDataAttributesScheduleRotationableAttributesType1",
            "NewScheduleRotationDataAttributesScheduleRotationableAttributesType2",
            "NewScheduleRotationDataAttributesScheduleRotationableAttributesType3",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_0 = (
                    NewScheduleRotationDataAttributesScheduleRotationableAttributesType0.from_dict(data)
                )

                return schedule_rotationable_attributes_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_1 = (
                    NewScheduleRotationDataAttributesScheduleRotationableAttributesType1.from_dict(data)
                )

                return schedule_rotationable_attributes_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_rotationable_attributes_type_2 = (
                    NewScheduleRotationDataAttributesScheduleRotationableAttributesType2.from_dict(data)
                )

                return schedule_rotationable_attributes_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            schedule_rotationable_attributes_type_3 = (
                NewScheduleRotationDataAttributesScheduleRotationableAttributesType3.from_dict(data)
            )

            return schedule_rotationable_attributes_type_3

        schedule_rotationable_attributes = _parse_schedule_rotationable_attributes(
            d.pop("schedule_rotationable_attributes")
        )

        position = d.pop("position", UNSET)

        active_all_week = d.pop("active_all_week", UNSET)

        active_days = []
        _active_days = d.pop("active_days", UNSET)
        for active_days_item_data in _active_days or []:
            active_days_item = NewScheduleRotationDataAttributesActiveDaysItem(active_days_item_data)

            active_days.append(active_days_item)

        active_time_type = d.pop("active_time_type", UNSET)

        active_time_attributes = []
        _active_time_attributes = d.pop("active_time_attributes", UNSET)
        for active_time_attributes_item_data in _active_time_attributes or []:
            active_time_attributes_item = NewScheduleRotationDataAttributesActiveTimeAttributesItem.from_dict(
                active_time_attributes_item_data
            )

            active_time_attributes.append(active_time_attributes_item)

        time_zone = d.pop("time_zone", UNSET)

        new_schedule_rotation_data_attributes = cls(
            name=name,
            schedule_rotationable_type=schedule_rotationable_type,
            schedule_rotationable_attributes=schedule_rotationable_attributes,
            position=position,
            active_all_week=active_all_week,
            active_days=active_days,
            active_time_type=active_time_type,
            active_time_attributes=active_time_attributes,
            time_zone=time_zone,
        )

        return new_schedule_rotation_data_attributes
