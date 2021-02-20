from django.utils import timezone as djangotime

from alerts.models import Alert
from tacticalrmm.celery import app


@app.task
def unsnooze_alerts() -> str:

    Alert.objects.filter(snoozed=True, snooze_until__lte=djangotime.now()).update(
        snoozed=False, snooze_until=None
    )

    return "ok"
