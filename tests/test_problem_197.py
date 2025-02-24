from sql_problems.problem_197 import rising_temperature
import pandas as pd 

def test_rising_temperature():
  pass


# def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
#     weather.sort_values(by='recordDate', inplace=True)
#     return weather[
#         (weather.temperature.diff() > 0)
#       & (weather.recordDate.diff().dt.days == 1)
#     ][['id']]