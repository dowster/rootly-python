from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3_shift_length_unit import (
    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3")


@_attrs_define
class UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3:
    """
    Attributes:
        shift_length (int): Shift length for custom rotation
        handoff_time (str): Hand off time for custom rotation
        shift_length_unit (Union[Unset,
            UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit]): Shift length unit for
            custom rotation
    """

    shift_length: int
    handoff_time: str
    shift_length_unit: Union[
        Unset, UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        shift_length = self.shift_length

        handoff_time = self.handoff_time

        shift_length_unit: Union[Unset, str] = UNSET
        if not isinstance(self.shift_length_unit, Unset):
            shift_length_unit = self.shift_length_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "shift_length": shift_length,
                "handoff_time": handoff_time,
            }
        )
        if shift_length_unit is not UNSET:
            field_dict["shift_length_unit"] = shift_length_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        shift_length = d.pop("shift_length")

        handoff_time = d.pop("handoff_time")

        _shift_length_unit = d.pop("shift_length_unit", UNSET)
        shift_length_unit: Union[
            Unset, UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit
        ]
        if isinstance(_shift_length_unit, Unset):
            shift_length_unit = UNSET
        else:
            shift_length_unit = UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType3ShiftLengthUnit(
                _shift_length_unit
            )

        update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3 = cls(
            shift_length=shift_length,
            handoff_time=handoff_time,
            shift_length_unit=shift_length_unit,
        )

        return update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_3
