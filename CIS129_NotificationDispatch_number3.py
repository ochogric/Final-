FUNCTION dispatchAlerts(alerts)
    FOR each alert IN alerts
        users = getUsersInLocation(alert.location)
        FOR each user IN users
            preferences = getUserPreferences(user.id)
            SEND_ALERT(user, alert, preferences)
        END FOR
    END FOR
END FUNCTION

FUNCTION getUsersInLocation(location)
    users = DATABASE_QUERY("SELECT * FROM users WHERE location = location")
    RETURN users
END FUNCTION

FUNCTION SEND_ALERT(user, alert, preferences)
    IF preferences.method == "SMS"
        sendSMS(user.phoneNumber, alert.message)
    ELSE IF preferences.method == "Email"
        sendEmail(user.email, "Weather Alert", alert.message)
    ELSE IF preferences.method == "Push"
        sendPushNotification(user.deviceId, alert.message)
    END IF
END FUNCTION

FUNCTION sendSMS(phoneNumber, message)
    SMS_API.send(phoneNumber, message)
END FUNCTION

FUNCTION sendEmail(email, subject, message)
    EMAIL_API.send(email, subject, message)
END FUNCTION

FUNCTION sendPushNotification(deviceId, message)
    PUSH_API.send(deviceId, message)
END FUNCTION
