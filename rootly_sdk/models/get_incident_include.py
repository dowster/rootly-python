from enum import Enum


class GetIncidentInclude(str, Enum):
    ACTION_ITEMS = "action_items"
    CAUSES = "causes"
    ENVIRONMENTS = "environments"
    EVENTS = "events"
    FEEDBACKS = "feedbacks"
    FORM_FIELD_SELECTIONS = "form_field_selections"
    FUNCTIONALITIES = "functionalities"
    GROUPS = "groups"
    INCIDENT_POST_MORTEM = "incident_post_mortem"
    INCIDENT_ROLE_ASSIGNMENTS = "incident_role_assignments"
    INCIDENT_SLACK_MESSAGES = "incident_slack_messages"
    INCIDENT_TYPES = "incident_types"
    SERVICES = "services"
    SUBSCRIBERS = "subscribers"
    SUB_STATUSES = "sub_statuses"

    def __str__(self) -> str:
        return str(self.value)
