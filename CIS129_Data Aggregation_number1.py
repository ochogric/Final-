FUNCTION aggregateWeatherData()
    DEFINE dataSources = [source1, source2, source3, ...]
    DEFINE aggregatedData = []

    FOR each source IN dataSources
        data = fetchWeatherData(source)
        IF data IS valid
            aggregatedData.ADD(data)
        ELSE
            LOG "Invalid data from" source
        END IF
    END FOR

    RETURN aggregatedData
END FUNCTION

FUNCTION fetchWeatherData(source)
    TRY
        response = API_CALL(source)
        data = PARSE response
        RETURN data
    EXCEPT Exception AS e
        LOG "Error fetching data from" source: e
        RETURN NULL
END FUNCTION
