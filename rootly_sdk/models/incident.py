from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_retrospective_progress_status import IncidentRetrospectiveProgressStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_response import EnvironmentResponse
    from ..models.functionality_response import FunctionalityResponse
    from ..models.incident_labels_type_0 import IncidentLabelsType0
    from ..models.incident_type_response import IncidentTypeResponse
    from ..models.service_response import ServiceResponse
    from ..models.severity_response import SeverityResponse
    from ..models.team_response import TeamResponse


T = TypeVar("T", bound="Incident")


@_attrs_define
class Incident:
    """
    Attributes:
        title (str): The title of the incident
        slug (str): The slug of the incident
        created_at (str): Date of creation
        updated_at (str): Date of last update
        kind (Union[Unset, str]): The kind of the incident
        parent_incident_id (Union[None, Unset, str]): ID of parent incident
        duplicate_incident_id (Union[None, Unset, str]): ID of duplicated incident
        summary (Union[None, Unset, str]): The summary of the incident
        private (Union[None, Unset, bool]): Create an incident as private Default: False.
        severity (Union[Unset, SeverityResponse]):
        environments (Union[None, Unset, list['EnvironmentResponse']]): The Environments of the incident
        incident_types (Union[None, Unset, list['IncidentTypeResponse']]): The Incident Types of the incident
        services (Union[None, Unset, list['ServiceResponse']]): The Services of the incident
        functionalities (Union[None, Unset, list['FunctionalityResponse']]): The Functionalities of the incident
        groups (Union[None, Unset, list['TeamResponse']]): The Teams of to the incident
        labels (Union['IncidentLabelsType0', None, Unset]): Labels to attach to the incidents. eg: {"platform":"osx",
            "version": "1.29"}
        slack_channel_id (Union[None, Unset, str]): Slack channel id
        slack_channel_name (Union[None, Unset, str]): Slack channel name
        slack_channel_url (Union[None, Unset, str]): Slack channel url
        mitigation_message (Union[None, Unset, str]): How was the incident mitigated?
        resolution_message (Union[None, Unset, str]): How was the incident resolved?
        cancellation_message (Union[None, Unset, str]): Why was the incident cancelled?
        scheduled_for (Union[None, Unset, str]): Date of when the maintenance begins
        scheduled_until (Union[None, Unset, str]): Date of when the maintenance ends
        retrospective_progress_status (Union[Unset, IncidentRetrospectiveProgressStatus]): The status of the
            retrospective progress
        in_triage_at (Union[None, Unset, str]): Date of triage
        started_at (Union[None, Unset, str]): Date of start
        detected_at (Union[None, Unset, str]): Date of detection
        acknowledged_at (Union[None, Unset, str]): Date of acknowledgment
        mitigated_at (Union[None, Unset, str]): Date of mitigation
        resolved_at (Union[None, Unset, str]): Date of resolution
        cancelled_at (Union[None, Unset, str]): Date of cancellation
    """

    title: str
    slug: str
    created_at: str
    updated_at: str
    kind: Union[Unset, str] = UNSET
    parent_incident_id: Union[None, Unset, str] = UNSET
    duplicate_incident_id: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    private: Union[None, Unset, bool] = False
    severity: Union[Unset, "SeverityResponse"] = UNSET
    environments: Union[None, Unset, list["EnvironmentResponse"]] = UNSET
    incident_types: Union[None, Unset, list["IncidentTypeResponse"]] = UNSET
    services: Union[None, Unset, list["ServiceResponse"]] = UNSET
    functionalities: Union[None, Unset, list["FunctionalityResponse"]] = UNSET
    groups: Union[None, Unset, list["TeamResponse"]] = UNSET
    labels: Union["IncidentLabelsType0", None, Unset] = UNSET
    slack_channel_id: Union[None, Unset, str] = UNSET
    slack_channel_name: Union[None, Unset, str] = UNSET
    slack_channel_url: Union[None, Unset, str] = UNSET
    mitigation_message: Union[None, Unset, str] = UNSET
    resolution_message: Union[None, Unset, str] = UNSET
    cancellation_message: Union[None, Unset, str] = UNSET
    scheduled_for: Union[None, Unset, str] = UNSET
    scheduled_until: Union[None, Unset, str] = UNSET
    retrospective_progress_status: Union[Unset, IncidentRetrospectiveProgressStatus] = UNSET
    in_triage_at: Union[None, Unset, str] = UNSET
    started_at: Union[None, Unset, str] = UNSET
    detected_at: Union[None, Unset, str] = UNSET
    acknowledged_at: Union[None, Unset, str] = UNSET
    mitigated_at: Union[None, Unset, str] = UNSET
    resolved_at: Union[None, Unset, str] = UNSET
    cancelled_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.incident_labels_type_0 import IncidentLabelsType0

        title = self.title

        slug = self.slug

        created_at = self.created_at

        updated_at = self.updated_at

        kind = self.kind

        parent_incident_id: Union[None, Unset, str]
        if isinstance(self.parent_incident_id, Unset):
            parent_incident_id = UNSET
        else:
            parent_incident_id = self.parent_incident_id

        duplicate_incident_id: Union[None, Unset, str]
        if isinstance(self.duplicate_incident_id, Unset):
            duplicate_incident_id = UNSET
        else:
            duplicate_incident_id = self.duplicate_incident_id

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        private: Union[None, Unset, bool]
        if isinstance(self.private, Unset):
            private = UNSET
        else:
            private = self.private

        severity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        environments: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.environments, Unset):
            environments = UNSET
        elif isinstance(self.environments, list):
            environments = []
            for environments_type_0_item_data in self.environments:
                environments_type_0_item = environments_type_0_item_data.to_dict()
                environments.append(environments_type_0_item)

        else:
            environments = self.environments

        incident_types: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.incident_types, Unset):
            incident_types = UNSET
        elif isinstance(self.incident_types, list):
            incident_types = []
            for incident_types_type_0_item_data in self.incident_types:
                incident_types_type_0_item = incident_types_type_0_item_data.to_dict()
                incident_types.append(incident_types_type_0_item)

        else:
            incident_types = self.incident_types

        services: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.services, Unset):
            services = UNSET
        elif isinstance(self.services, list):
            services = []
            for services_type_0_item_data in self.services:
                services_type_0_item = services_type_0_item_data.to_dict()
                services.append(services_type_0_item)

        else:
            services = self.services

        functionalities: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.functionalities, Unset):
            functionalities = UNSET
        elif isinstance(self.functionalities, list):
            functionalities = []
            for functionalities_type_0_item_data in self.functionalities:
                functionalities_type_0_item = functionalities_type_0_item_data.to_dict()
                functionalities.append(functionalities_type_0_item)

        else:
            functionalities = self.functionalities

        groups: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        labels: Union[None, Unset, dict[str, Any]]
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, IncidentLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        slack_channel_id: Union[None, Unset, str]
        if isinstance(self.slack_channel_id, Unset):
            slack_channel_id = UNSET
        else:
            slack_channel_id = self.slack_channel_id

        slack_channel_name: Union[None, Unset, str]
        if isinstance(self.slack_channel_name, Unset):
            slack_channel_name = UNSET
        else:
            slack_channel_name = self.slack_channel_name

        slack_channel_url: Union[None, Unset, str]
        if isinstance(self.slack_channel_url, Unset):
            slack_channel_url = UNSET
        else:
            slack_channel_url = self.slack_channel_url

        mitigation_message: Union[None, Unset, str]
        if isinstance(self.mitigation_message, Unset):
            mitigation_message = UNSET
        else:
            mitigation_message = self.mitigation_message

        resolution_message: Union[None, Unset, str]
        if isinstance(self.resolution_message, Unset):
            resolution_message = UNSET
        else:
            resolution_message = self.resolution_message

        cancellation_message: Union[None, Unset, str]
        if isinstance(self.cancellation_message, Unset):
            cancellation_message = UNSET
        else:
            cancellation_message = self.cancellation_message

        scheduled_for: Union[None, Unset, str]
        if isinstance(self.scheduled_for, Unset):
            scheduled_for = UNSET
        else:
            scheduled_for = self.scheduled_for

        scheduled_until: Union[None, Unset, str]
        if isinstance(self.scheduled_until, Unset):
            scheduled_until = UNSET
        else:
            scheduled_until = self.scheduled_until

        retrospective_progress_status: Union[Unset, str] = UNSET
        if not isinstance(self.retrospective_progress_status, Unset):
            retrospective_progress_status = self.retrospective_progress_status.value

        in_triage_at: Union[None, Unset, str]
        if isinstance(self.in_triage_at, Unset):
            in_triage_at = UNSET
        else:
            in_triage_at = self.in_triage_at

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        detected_at: Union[None, Unset, str]
        if isinstance(self.detected_at, Unset):
            detected_at = UNSET
        else:
            detected_at = self.detected_at

        acknowledged_at: Union[None, Unset, str]
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        mitigated_at: Union[None, Unset, str]
        if isinstance(self.mitigated_at, Unset):
            mitigated_at = UNSET
        else:
            mitigated_at = self.mitigated_at

        resolved_at: Union[None, Unset, str]
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        cancelled_at: Union[None, Unset, str]
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = self.cancelled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "slug": slug,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if parent_incident_id is not UNSET:
            field_dict["parent_incident_id"] = parent_incident_id
        if duplicate_incident_id is not UNSET:
            field_dict["duplicate_incident_id"] = duplicate_incident_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if private is not UNSET:
            field_dict["private"] = private
        if severity is not UNSET:
            field_dict["severity"] = severity
        if environments is not UNSET:
            field_dict["environments"] = environments
        if incident_types is not UNSET:
            field_dict["incident_types"] = incident_types
        if services is not UNSET:
            field_dict["services"] = services
        if functionalities is not UNSET:
            field_dict["functionalities"] = functionalities
        if groups is not UNSET:
            field_dict["groups"] = groups
        if labels is not UNSET:
            field_dict["labels"] = labels
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
        if slack_channel_url is not UNSET:
            field_dict["slack_channel_url"] = slack_channel_url
        if mitigation_message is not UNSET:
            field_dict["mitigation_message"] = mitigation_message
        if resolution_message is not UNSET:
            field_dict["resolution_message"] = resolution_message
        if cancellation_message is not UNSET:
            field_dict["cancellation_message"] = cancellation_message
        if scheduled_for is not UNSET:
            field_dict["scheduled_for"] = scheduled_for
        if scheduled_until is not UNSET:
            field_dict["scheduled_until"] = scheduled_until
        if retrospective_progress_status is not UNSET:
            field_dict["retrospective_progress_status"] = retrospective_progress_status
        if in_triage_at is not UNSET:
            field_dict["in_triage_at"] = in_triage_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if detected_at is not UNSET:
            field_dict["detected_at"] = detected_at
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if mitigated_at is not UNSET:
            field_dict["mitigated_at"] = mitigated_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.environment_response import EnvironmentResponse
        from ..models.functionality_response import FunctionalityResponse
        from ..models.incident_labels_type_0 import IncidentLabelsType0
        from ..models.incident_type_response import IncidentTypeResponse
        from ..models.service_response import ServiceResponse
        from ..models.severity_response import SeverityResponse
        from ..models.team_response import TeamResponse

        d = src_dict.copy()
        title = d.pop("title")

        slug = d.pop("slug")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        kind = d.pop("kind", UNSET)

        def _parse_parent_incident_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_incident_id = _parse_parent_incident_id(d.pop("parent_incident_id", UNSET))

        def _parse_duplicate_incident_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        duplicate_incident_id = _parse_duplicate_incident_id(d.pop("duplicate_incident_id", UNSET))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_private(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        private = _parse_private(d.pop("private", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, SeverityResponse]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityResponse.from_dict(_severity)

        def _parse_environments(data: object) -> Union[None, Unset, list["EnvironmentResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environments_type_0 = []
                _environments_type_0 = data
                for environments_type_0_item_data in _environments_type_0:
                    environments_type_0_item = EnvironmentResponse.from_dict(environments_type_0_item_data)

                    environments_type_0.append(environments_type_0_item)

                return environments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["EnvironmentResponse"]], data)

        environments = _parse_environments(d.pop("environments", UNSET))

        def _parse_incident_types(data: object) -> Union[None, Unset, list["IncidentTypeResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_types_type_0 = []
                _incident_types_type_0 = data
                for incident_types_type_0_item_data in _incident_types_type_0:
                    incident_types_type_0_item = IncidentTypeResponse.from_dict(incident_types_type_0_item_data)

                    incident_types_type_0.append(incident_types_type_0_item)

                return incident_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IncidentTypeResponse"]], data)

        incident_types = _parse_incident_types(d.pop("incident_types", UNSET))

        def _parse_services(data: object) -> Union[None, Unset, list["ServiceResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                services_type_0 = []
                _services_type_0 = data
                for services_type_0_item_data in _services_type_0:
                    services_type_0_item = ServiceResponse.from_dict(services_type_0_item_data)

                    services_type_0.append(services_type_0_item)

                return services_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ServiceResponse"]], data)

        services = _parse_services(d.pop("services", UNSET))

        def _parse_functionalities(data: object) -> Union[None, Unset, list["FunctionalityResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionalities_type_0 = []
                _functionalities_type_0 = data
                for functionalities_type_0_item_data in _functionalities_type_0:
                    functionalities_type_0_item = FunctionalityResponse.from_dict(functionalities_type_0_item_data)

                    functionalities_type_0.append(functionalities_type_0_item)

                return functionalities_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["FunctionalityResponse"]], data)

        functionalities = _parse_functionalities(d.pop("functionalities", UNSET))

        def _parse_groups(data: object) -> Union[None, Unset, list["TeamResponse"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = TeamResponse.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TeamResponse"]], data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_labels(data: object) -> Union["IncidentLabelsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = IncidentLabelsType0.from_dict(data)

                return labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentLabelsType0", None, Unset], data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_slack_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slack_channel_id = _parse_slack_channel_id(d.pop("slack_channel_id", UNSET))

        def _parse_slack_channel_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slack_channel_name = _parse_slack_channel_name(d.pop("slack_channel_name", UNSET))

        def _parse_slack_channel_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slack_channel_url = _parse_slack_channel_url(d.pop("slack_channel_url", UNSET))

        def _parse_mitigation_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mitigation_message = _parse_mitigation_message(d.pop("mitigation_message", UNSET))

        def _parse_resolution_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolution_message = _parse_resolution_message(d.pop("resolution_message", UNSET))

        def _parse_cancellation_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancellation_message = _parse_cancellation_message(d.pop("cancellation_message", UNSET))

        def _parse_scheduled_for(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scheduled_for = _parse_scheduled_for(d.pop("scheduled_for", UNSET))

        def _parse_scheduled_until(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scheduled_until = _parse_scheduled_until(d.pop("scheduled_until", UNSET))

        _retrospective_progress_status = d.pop("retrospective_progress_status", UNSET)
        retrospective_progress_status: Union[Unset, IncidentRetrospectiveProgressStatus]
        if isinstance(_retrospective_progress_status, Unset):
            retrospective_progress_status = UNSET
        else:
            retrospective_progress_status = IncidentRetrospectiveProgressStatus(_retrospective_progress_status)

        def _parse_in_triage_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        in_triage_at = _parse_in_triage_at(d.pop("in_triage_at", UNSET))

        def _parse_started_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_detected_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detected_at = _parse_detected_at(d.pop("detected_at", UNSET))

        def _parse_acknowledged_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_mitigated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mitigated_at = _parse_mitigated_at(d.pop("mitigated_at", UNSET))

        def _parse_resolved_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        def _parse_cancelled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

        incident = cls(
            title=title,
            slug=slug,
            created_at=created_at,
            updated_at=updated_at,
            kind=kind,
            parent_incident_id=parent_incident_id,
            duplicate_incident_id=duplicate_incident_id,
            summary=summary,
            private=private,
            severity=severity,
            environments=environments,
            incident_types=incident_types,
            services=services,
            functionalities=functionalities,
            groups=groups,
            labels=labels,
            slack_channel_id=slack_channel_id,
            slack_channel_name=slack_channel_name,
            slack_channel_url=slack_channel_url,
            mitigation_message=mitigation_message,
            resolution_message=resolution_message,
            cancellation_message=cancellation_message,
            scheduled_for=scheduled_for,
            scheduled_until=scheduled_until,
            retrospective_progress_status=retrospective_progress_status,
            in_triage_at=in_triage_at,
            started_at=started_at,
            detected_at=detected_at,
            acknowledged_at=acknowledged_at,
            mitigated_at=mitigated_at,
            resolved_at=resolved_at,
            cancelled_at=cancelled_at,
        )

        incident.additional_properties = d
        return incident

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
