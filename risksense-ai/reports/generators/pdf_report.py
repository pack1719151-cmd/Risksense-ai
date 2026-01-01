from fpdf import FPDF

# pdf_report.py
# Generates PDF risk reports
class PDFReportGenerator:
    def __init__(self, title="Risk Report"):
        self.pdf = FPDF()
        self.title = title

    def header(self):
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, self.title, ln=True, align="C")
        self.pdf.ln(10)

    def add_section(self, heading, content):
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, heading, ln=True)
        self.pdf.set_font("Arial", "", 11)
        self.pdf.multi_cell(0, 10, content)
        self.pdf.ln(5)

    def add_table(self, data, col_widths=None, align="L"):
        if not data:
            return
        self.pdf.set_font("Arial", "B", 11)
        headers = data[0]
        if not col_widths:
            col_widths = [self.pdf.w / len(headers) - 10] * len(headers)
        for i, header in enumerate(headers):
            self.pdf.cell(col_widths[i], 10, str(header), border=1, align=align)
        self.pdf.ln()
        self.pdf.set_font("Arial", "", 11)
        for row in data[1:]:
            for i, item in enumerate(row):
                self.pdf.cell(col_widths[i], 10, str(item), border=1, align=align)
            self.pdf.ln()
        self.pdf.ln(5)

    def generate(self, sections, output_path, tables=None):
        self.pdf.add_page()
        self.header()
        for heading, content in sections:
            self.add_section(heading, content)
        if tables:
            for table in tables:
                heading = table.get("heading", "")
                data = table.get("data", [])
                col_widths = table.get("col_widths", None)
                align = table.get("align", "L")
                if heading:
                    self.add_section(heading, "")
                self.add_table(data, col_widths, align)
        self.pdf.output(output_path)