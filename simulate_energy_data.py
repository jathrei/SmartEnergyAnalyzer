import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# generate simulated data
def simulate_energy_data(start_date, end_date):
    # date range
    date_range = pd.date_range(start=start_date, end=end_date, freq='h')

    # check length of date range (my own curiosity, change later)
    print(len(date_range))

    # simulate energy consumption data (in kWh)
    energy_consumption = np.random.uniform(low=5, high=15, size=len(date_range))

    # simulate temperature data (in farenheight)
    temperature = np.random.uniform(low=20, high=80, size=len(date_range))

    # simulate humidity data (in %)
    humidity = np.random.uniform(low=30, high=90, size=len(date_range))

    # create a DataFrame
    data = pd.DataFrame({
        'Timestamp': date_range,
        'Energy_Consumption_kWh': energy_consumption,
        'Temperature_F': temperature,
        'Humidity_%': humidity
    })

    return data

# simulating data for one year
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
energy_data = simulate_energy_data(start_date, end_date)

# display the first few rows of the dataset
print(energy_data.head())

# save the DataFrame to a CSV file
file_name = "simulated_energy_data.csv"
energy_data.to_csv(file_name, index=False)
print(f"Data saved to {file_name}")