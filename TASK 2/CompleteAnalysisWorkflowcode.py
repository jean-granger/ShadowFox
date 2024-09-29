import pandas as pd
import matplotlib.pyplot as plt

#  LOAD THE AQI DATA SET PROVIDED FROM A CSV FILE FORMAT
df = pd.read_csv('../delhiaqi.csv', parse_dates=['date'])


# PREPARE THE DATA
  # CHECKING THE MISSING VALUES
print("THE MISSING VALUES ARE:\n", df.isnull().sum())

  # DESCRIPTIVE STATISTICS
print("Descriptive Statistics:\n", df[['co', 'no2', 'o3', 'pm2_5', 'pm10', 'nh3']].describe())


# VISUALIZATIONS OF THE DATA
  # PLOTTING TRENDS OF THE VARIOUS POLLUANTS OVER TIME
plt.figure(figsize=(14, 8))
for POLLUTANT in ['co', 'no2', 'o3', 'pm2_5', 'pm10', 'nh3']:
    plt.plot(df['date'], df[POLLUTANT], label=POLLUTANT)
plt.title('TRENDS OF THE MAIN POLLUTANTS OVER TIME')
plt.xlabel('date')
plt.ylabel('CCONCENTRATION (µg/m³)')
plt.legend()
plt.grid()
plt.show()
