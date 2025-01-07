from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_source import AlertSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_data_type_0 import AlertDataType0
    from ..models.alert_labels_item_type_0 import AlertLabelsItemType0
    from ..models.environment import Environment
    from ..models.service import Service
    from ..models.team import Team


T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """
    Attributes:
        source (AlertSource): The source of the alert
        summary (str): The summary of the alert
        created_at (str): Date of creation
        updated_at (str): Date of last update
        description (Union[None, Unset, str]): The description of the alert
        services (Union[Unset, list['Service']]): Services attached to the alert
        groups (Union[Unset, list['Team']]): Groups attached to the alert
        environments (Union[Unset, list['Environment']]): Environments attached to the alert
        external_id (Union[None, Unset, str]): External ID
        external_url (Union[None, Unset, str]): External Url
        alert_urgency_id (Union[None, Unset, str]): The ID of the alert urgency
        labels (Union[Unset, list[Union['AlertLabelsItemType0', None]]]):
        data (Union['AlertDataType0', None, Unset]): Additional data
    """

    source: AlertSource
    summary: str
    created_at: str
    updated_at: str
    description: Union[None, Unset, str] = UNSET
    services: Union[Unset, list["Service"]] = UNSET
    groups: Union[Unset, list["Team"]] = UNSET
    environments: Union[Unset, list["Environment"]] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    alert_urgency_id: Union[None, Unset, str] = UNSET
    labels: Union[Unset, list[Union["AlertLabelsItemType0", None]]] = UNSET
    data: Union["AlertDataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_data_type_0 import AlertDataType0
        from ..models.alert_labels_item_type_0 import AlertLabelsItemType0

        source = self.source.value

        summary = self.summary

        created_at = self.created_at

        updated_at = self.updated_at

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        environments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for environments_item_data in self.environments:
                environments_item = environments_item_data.to_dict()
                environments.append(environments_item)

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        alert_urgency_id: Union[None, Unset, str]
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        labels: Union[Unset, list[Union[None, dict[str, Any]]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: Union[None, dict[str, Any]]
                if isinstance(labels_item_data, AlertLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, AlertDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "summary": summary,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if services is not UNSET:
            field_dict["services"] = services
        if groups is not UNSET:
            field_dict["groups"] = groups
        if environments is not UNSET:
            field_dict["environments"] = environments
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.alert_data_type_0 import AlertDataType0
        from ..models.alert_labels_item_type_0 import AlertLabelsItemType0
        from ..models.environment import Environment
        from ..models.service import Service
        from ..models.team import Team

        d = src_dict.copy()
        source = AlertSource(d.pop("source"))

        summary = d.pop("summary")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = Service.from_dict(services_item_data)

            services.append(services_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = Team.from_dict(groups_item_data)

            groups.append(groups_item)

        environments = []
        _environments = d.pop("environments", UNSET)
        for environments_item_data in _environments or []:
            environments_item = Environment.from_dict(environments_item_data)

            environments.append(environments_item)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_alert_urgency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:

            def _parse_labels_item(data: object) -> Union["AlertLabelsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    labels_item_type_0 = AlertLabelsItemType0.from_dict(data)

                    return labels_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["AlertLabelsItemType0", None], data)

            labels_item = _parse_labels_item(labels_item_data)

            labels.append(labels_item)

        def _parse_data(data: object) -> Union["AlertDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = AlertDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        alert = cls(
            source=source,
            summary=summary,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            services=services,
            groups=groups,
            environments=environments,
            external_id=external_id,
            external_url=external_url,
            alert_urgency_id=alert_urgency_id,
            labels=labels,
            data=data,
        )

        alert.additional_properties = d
        return alert

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
