from fpdf import FPDF
import os

class AutomotiveReport(FPDF):
    def header(self):
        # شعار أو عنوان التقرير في الهيدر
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Automotive Strategic Analysis Report (2019-2023)', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # رقم الصفحة في الفوتر
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf_report():
    pdf = AutomotiveReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # القسم الأول: المقدمة
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "1. Executive Summary", 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, (
        "This strategic report analyzes vehicle sales performance (ICE vs EV) "
        "during periods of economic instability from 2019 to 2023. It aims to "
        "provide insights into market resilience and operational excellence."
    ))
    pdf.ln(5)

    # القسم الثاني: المنهجية
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "2. Methodology", 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, (
        "Data was synthesized monthly over a 5-year period. Economic crisis variables "
        "were introduced in 2020 and 2023 to measure the sensitivity of different vehicle segments."
    ))
    pdf.ln(5)

    # القسم الثالث: التحليل المرئي - الرسم الأول
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "3. Visual Analysis", 0, 1)
    
    if os.path.exists('figures/sales_trend.png'):
        pdf.image('figures/sales_trend.png', x=15, w=180)
        pdf.ln(2)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, "Figure 1: Comparison of monthly sales trends for ICE and EV models.", 0, 1, 'C')

    pdf.add_page()
    
    # القسم الثالث: التحليل المرئي - الرسم الثاني
    if os.path.exists('figures/crisis_impact.png'):
        pdf.image('figures/crisis_impact.png', x=15, w=180)
        pdf.ln(2)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, "Figure 2: Performance breakdown during normal vs. crisis economic periods.", 0, 1, 'C')

    # القسم الرابع: التوصيات
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "4. Strategic Recommendations", 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, (
        "1. Prioritize EV infrastructure investment due to proven market resilience.\n"
        "2. Implement AI-driven predictive modeling for risk management.\n"
        "3. Focus on sustainable growth to mitigate future economic shocks."
    ))

    output_path = 'outputs/Automotive_Strategic_Report.pdf'
    pdf.output(output_path)
    print(f"PDF report generated successfully at: {output_path}")

if __name__ == "__main__":
    create_pdf_report()