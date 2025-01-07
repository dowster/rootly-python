from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alerts_source_sourceable_attributes import AlertsSourceSourceableAttributes


T = TypeVar("T", bound="AlertsSource")


@_attrs_define
class AlertsSource:
    """
    Attributes:
        name (str): The name of the alert source
        status (str): The current status of the alert source
        secret (str): A secret key used to authenticate incoming requests to this alerts source
        webhook_endpoint (str): The URL endpoint of the alert source
        created_at (str): Date of creation
        updated_at (str): Date of last update
        source_type (Union[Unset, str]): The alert source type
        sourceable_attributes (Union[Unset, AlertsSourceSourceableAttributes]): Additional attributes specific to
            certain alert sources (e.g., generic_webhook), encapsulating source-specific configurations or details
    """

    name: str
    status: str
    secret: str
    webhook_endpoint: str
    created_at: str
    updated_at: str
    source_type: Union[Unset, str] = UNSET
    sourceable_attributes: Union[Unset, "AlertsSourceSourceableAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        secret = self.secret

        webhook_endpoint = self.webhook_endpoint

        created_at = self.created_at

        updated_at = self.updated_at

        source_type = self.source_type

        sourceable_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sourceable_attributes, Unset):
            sourceable_attributes = self.sourceable_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "secret": secret,
                "webhook_endpoint": webhook_endpoint,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if sourceable_attributes is not UNSET:
            field_dict["sourceable_attributes"] = sourceable_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alerts_source_sourceable_attributes import AlertsSourceSourceableAttributes

        d = src_dict.copy()
        name = d.pop("name")

        status = d.pop("status")

        secret = d.pop("secret")

        webhook_endpoint = d.pop("webhook_endpoint")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        source_type = d.pop("source_type", UNSET)

        _sourceable_attributes = d.pop("sourceable_attributes", UNSET)
        sourceable_attributes: Union[Unset, AlertsSourceSourceableAttributes]
        if isinstance(_sourceable_attributes, Unset):
            sourceable_attributes = UNSET
        else:
            sourceable_attributes = AlertsSourceSourceableAttributes.from_dict(_sourceable_attributes)

        alerts_source = cls(
            name=name,
            status=status,
            secret=secret,
            webhook_endpoint=webhook_endpoint,
            created_at=created_at,
            updated_at=updated_at,
            source_type=source_type,
            sourceable_attributes=sourceable_attributes,
        )

        alerts_source.additional_properties = d
        return alerts_source

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
