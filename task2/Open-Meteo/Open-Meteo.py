import requests
import csv

params = {
    "latitude": 26.05942,
    "longitude": 119.198,
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "hourly": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,cloud_cover_total,wind_speed_10m,wind_direction_10m,shortwave_radiation_instant,is_day",
    "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min,precipitation_sum,sunshine_duration",
    "timezone":"Asia/Shanghai"
}

resp=requests.get("https://archive-api.open-meteo.com/v1/archive", params=params, timeout=30)
resp.raise_for_status()
data=resp.json()

hourly_data=data.get("hourly", {})
hourly_time=hourly_data.get("time", [])
hourly_columns=["time"] + hourly_weather_variables
with open("fuzhou_hourly_2024.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(hourly_columns)
    for i, t in enumerate(hourly_time):
        row = [t] + [hourly_data[var][i] for var in hourly_weather_variables]
        writer.writerow(row)

daily_data = data.get("daily", {})
daily_time = daily_data.get("time", [])
daily_columns = ["time"] + daily_weather_variables
with open("fuzhou_daily_2024.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(daily_columns)
    for i, t in enumerate(daily_time):
        row = [t] + [daily_data[var][i] for var in daily_weather_variables]
        writer.writerow(row)

print(f"数据已成功保存,共 {len(daily_time)} 条记录。")
