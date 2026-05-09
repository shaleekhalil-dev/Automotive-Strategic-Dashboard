import pandas as pd
import numpy as np

def generate_automotive_data():
    np.random.seed(7)
    months = pd.date_range(start='2019-01-01', periods=60, freq='M')
    
    data = []
    for date in months:
        is_crisis = 1 if (date.year == 2020 or date.year == 2023) else 0
        
        base_sales_ice = 5000
        base_sales_ev = 1000
        
        if is_crisis:
            sales_ice = base_sales_ice * np.random.uniform(0.5, 0.7)
            sales_ev = base_sales_ev * np.random.uniform(0.8, 1.1)
        else:
            sales_ice = base_sales_ice * np.random.uniform(0.9, 1.2)
            sales_ev = (base_sales_ev + (date.year - 2019) * 500) * np.random.uniform(0.9, 1.3)
            
        data.append([date, 'ICE', int(sales_ice), is_crisis])
        data.append([date, 'EV', int(sales_ev), is_crisis])

    df = pd.DataFrame(data, columns=['Date', 'VehicleType', 'Sales', 'EconomicCrisis'])
    df.to_csv('data/automotive_sales_data.csv', index=False)
    print("Automotive synthetic data generated in data/ folder.")

if __name__ == "__main__":
    generate_automotive_data()