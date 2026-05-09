import pandas as pd

def process_data():
    df = pd.read_csv('data/automotive_sales_data.csv')
    
    total_sales = df['Sales'].sum()
    
    crisis_impact = df.groupby(['VehicleType', 'EconomicCrisis'])['Sales'].mean().unstack()
    crisis_impact.columns = ['Normal_Periods', 'Crisis_Periods']
    
    summary_report = f"""
    Automotive Sales Analysis Summary
    =================================
    Total Vehicles Sold (5 Years): {total_sales}
    
    Average Monthly Sales Comparison:
    {crisis_impact.to_string()}
    """
    
    with open('outputs/automotive_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary_report)
    
    print("Data processing complete. Summary report generated in outputs/ folder.")

if __name__ == "__main__":
    process_data()