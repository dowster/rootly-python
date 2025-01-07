from enum import Enum


class NewAlertsSourceDataAttributesSourceType(str, Enum):
    ALERTMANAGER = "alertmanager"
    AZURE = "azure"
    CHECKLY = "checkly"
    CLOUD_WATCH = "cloud_watch"
    DATADOG = "datadog"
    GENERIC_WEBHOOK = "generic_webhook"
    GOOGLE_CLOUD = "google_cloud"
    GRAFANA = "grafana"
    NEW_RELIC = "new_relic"
    SENTRY = "sentry"
    SPLUNK = "splunk"

    def __str__(self) -> str:
        return str(self.value)
