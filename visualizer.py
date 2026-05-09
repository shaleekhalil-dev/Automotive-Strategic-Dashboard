import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    df = pd.read_csv('data/automotive_sales_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    
    sns.set_theme(style="darkgrid")
    
    # الرسم الأول: الخط الزمني للمبيعات
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Sales', hue='VehicleType', data=df, marker="o", palette="tab10")
    plt.title('Monthly Vehicle Sales Trend (2019-2023)')
    plt.ylabel('Sales Volume')
    plt.xlabel('Year')
    plt.savefig('figures/sales_trend.png')
    plt.close()
    
    # الرسم الثاني: تأثير الأزمات الاقتصادية
    plt.figure(figsize=(10, 6))
    sns.barplot(x='VehicleType', y='Sales', hue='EconomicCrisis', data=df, palette='Set2')
    plt.title('Average Monthly Sales: Normal (0) vs Crisis (1) Periods')
    plt.ylabel('Average Sales')
    plt.xlabel('Vehicle Type (ICE: Internal Combustion, EV: Electric)')
    plt.legend(title='Economic Crisis', labels=['Normal Period', 'Crisis Period'])
    plt.savefig('figures/crisis_impact.png')
    plt.close()
    
    print("Visualizations created successfully in figures/ folder.")

if __name__ == "__main__":
    create_visualizations()