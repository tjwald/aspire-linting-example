from app.forecast_generator import generate_forecast, SUMMARIES


def test_generate_forecast():
    forecast = generate_forecast()
    
    assert isinstance(forecast, list)
    for item in forecast:
        assert isinstance(item, dict)
        assert "date" in item
        assert "temperatureC" in item
        assert "temperatureF" in item
        assert "summary" in item
        assert item["summary"] in SUMMARIES
        assert -20 <= item["temperatureC"] <= 55