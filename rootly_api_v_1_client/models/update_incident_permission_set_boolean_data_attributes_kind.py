from enum import Enum


class UpdateIncidentPermissionSetBooleanDataAttributesKind(str, Enum):
    ASSIGN_INCIDENT_ROLES = "assign_incident_roles"
    INVITE_SUBSCRIBERS = "invite_subscribers"
    MODIFY_CUSTOM_FIELDS = "modify_custom_fields"
    PUBLISH_TO_STATUS_PAGE = "publish_to_status_page"
    TRIGGER_WORKFLOWS = "trigger_workflows"
    UPDATE_SUMMARY = "update_summary"
    UPDATE_TIMELINE = "update_timeline"

    def __str__(self) -> str:
        return str(self.value)
