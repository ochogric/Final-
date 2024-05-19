FUNCTION processWeatherData(aggregatedData)
    DEFINE severeWeatherConditions = []

    FOR each dataPoint IN aggregatedData
        IF dataPoint.condition IS severe
            severeWeatherConditions.ADD(dataPoint)
        END IF
    END FOR

    RETURN severeWeatherConditions
END FUNCTION

FUNCTION generateAlerts(severeWeatherConditions)
    DEFINE alerts = []

    FOR each condition IN severeWeatherConditions
        alert = CREATE_ALERT(condition)
        alerts.ADD(alert)
    END FOR

    RETURN alerts
END FUNCTION

FUNCTION CREATE_ALERT(condition)
    alert = NEW Alert()
    alert.type = condition.type
    alert.location = condition.location
    alert.severity = condition.severity
    alert.message = "Severe weather alert: " + condition.description
    RETURN alert
END FUNCTION
