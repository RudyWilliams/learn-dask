import pandas as pd 


df09 = pd.read_csv('data\\florida_flights_2009.csv')
df19 = pd.read_csv('data\\florida_flights_2019.csv')
#since only two I'll do this way
data = [df09, df19]
n_delays = []
n_flights = []

def delay_count(df):
    return (df['DEP_DELAY'] > 0).sum()

def flight_count(df):
    return df.shape[0]

for df in data:
    n_delays.append(delay_count(df))
    n_flights.append(flight_count(df))

if __name__ == '__main__':
    print(n_delays)
    print(n_flights)

    print(sum(n_delays) / sum(n_flights) * 100)
