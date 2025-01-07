from enum import Enum


class AlertSource(str, Enum):
    ALERTMANAGER = "alertmanager"
    ASANA = "asana"
    AZURE = "azure"
    CLICKUP = "clickup"
    CLOUD_WATCH = "cloud_watch"
    DATADOG = "datadog"
    EMAIL = "email"
    GENERIC_WEBHOOK = "generic_webhook"
    GOOGLE_CLOUD = "google_cloud"
    GRAFANA = "grafana"
    HONEYCOMB = "honeycomb"
    JIRA = "jira"
    LINEAR = "linear"
    LIVE_CALL_ROUTING = "live_call_routing"
    MANUAL = "manual"
    NOBL9 = "nobl9"
    OPSGENIE = "opsgenie"
    PAGERDUTY = "pagerduty"
    PAGERTREE = "pagertree"
    ROLLBAR = "rollbar"
    ROOTLY = "rootly"
    SENTRY = "sentry"
    SERVICE_NOW = "service_now"
    SLACK = "slack"
    SPLUNK = "splunk"
    VICTOROPS = "victorops"
    WEB = "web"
    WORKFLOW = "workflow"
    ZENDESK = "zendesk"

    def __str__(self) -> str:
        return str(self.value)
