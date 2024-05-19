FUNCTION monitorSystem()
    WHILE true
        CHECK systemHealth
        IF systemHealth IS NOT optimal
            NOTIFY admins
        END IF
        WAIT 5 minutes
    END WHILE
END FUNCTION

FUNCTION CHECK systemHealth()
    DEFINE components = [dataAggregation, alertGeneration, userManagement, notificationDispatch]

    FOR each component IN components
        status = component.STATUS()
        IF status IS NOT "OK"
            RETURN "NOT OK"
        END IF
    END FOR

    RETURN "OK"
END FUNCTION
