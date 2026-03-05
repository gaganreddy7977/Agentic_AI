from fpdf import FPDF
import os
import datetime

class PDFAgent:

    def run(self, analysis_text):

        os.makedirs("pdf_outputs", exist_ok=True)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200,10,"Dataset Analysis Report", ln=True)
        pdf.ln(10)

        pdf.multi_cell(0,10,analysis_text)

        filename = f"report_{int(datetime.datetime.now().timestamp())}.pdf"
        path = os.path.join("pdf_outputs", filename)

        pdf.output(path)

        return path