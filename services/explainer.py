from models import Alert


def generate_explanation(alert: Alert) -> str:
    if alert.metric_value > alert.threshold:
        comparison = "exceeded"
    elif alert.metric_value < alert.threshold:
        comparison = "fell below"
    else:
        comparison = "reached"

    next_steps = {
        "critical": "Investigate immediately and take corrective action.",
        "warning": "Review the affected system and monitor the metric closely.",
        "info": "Review the metric and confirm whether any action is needed.",
    }
    return (
        f'This {alert.severity} alert from {alert.source} is titled "{alert.title}". '
        f"The {alert.metric_name} metric {comparison} its threshold: "
        f"the current value is {alert.metric_value}, "
        f"compared with a threshold of {alert.threshold}. "
        f"Recommended next step: {next_steps[alert.severity]}"
    )