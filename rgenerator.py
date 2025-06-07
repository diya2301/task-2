import pandas as pd
from fpdf import FPDF

# Step 1: Read the data
data = pd.read_csv("data.csv")  # Make sure to have this file in the same folder
summary = data.describe()  # Basic analysis

# Step 2: Create the PDF report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Automated Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_summary_table(self, dataframe):
        self.set_font("Arial", size=10)
        col_width = self.w / (len(dataframe.columns) + 1)
        row_height = 10

        # Header
        self.set_fill_color(200, 220, 255)
        self.cell(col_width, row_height, " ", border=1, fill=True)
        for col in dataframe.columns:
            self.cell(col_width, row_height, str(col), border=1, fill=True)
        self.ln(row_height)

        # Rows
        for i, row in dataframe.iterrows():
            self.cell(col_width, row_height, str(i), border=1)
            for item in row:
                self.cell(col_width, row_height, f"{item:.2f}", border=1)
            self.ln(row_height)

# Step 3: Generate and save PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Data Summary:", ln=True)
pdf.ln(5)
pdf.add_summary_table(summary)
pdf.output("report.pdf")

print("PDF report generated successfully.")
