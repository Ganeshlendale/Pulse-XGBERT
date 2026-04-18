from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")

def create_chap6_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_margins(25.4, 25.4, 25.4) # 1 inch margins
    pdf.set_auto_page_break(auto=True, margin=25.4)
    
    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "CHAPTER 6", ln=True, align="C")
    pdf.cell(0, 10, "CONCLUSION", ln=True, align="C")
    pdf.ln(5)

    # 6.1
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "6.1 Conclusion", ln=True)
    pdf.set_font("Arial", "", 12)
    
    conclusion_txt = (
        "The SMS Spam Dashboard project has shown how Machine Learning and Natural Language Processing "
        "can simplify and enhance digital security for everyday users. By combining a secure and robust "
        "Django web interface with powerful inference algorithms (XGBoost and DistilBERT), the tool makes "
        "it easy to accurately identify and filter malicious messages in real-time.\n\n"
        "With advanced features like intelligent token extraction, strict tenant data isolation, and active "
        "learning feedback loops, the system ensures that personal communication remains protected and digital "
        "privacy is strictly enforced. The dual-model architecture efficiently parses deceptive vocabulary "
        "to catch spear-phishing attempts while maintaining near-instantaneous backend responsiveness. The "
        "knowledge gained through extensive data science research enabled a deep understanding of text "
        "vectorization and predictive cloud pipelines, which directly contributed to architecting this "
        "application.\n\n"
        "In the future, the system can be improved further by automating offline model retraining, expanding "
        "detailed threat categorization, and integrating directly with live mobile messaging APIs. Overall, "
        "this project has been a profoundly valuable learning experience and a strong, definitive step toward "
        "building proactive, AI-powered cybersecurity solutions."
    )
    pdf.multi_cell(0, 7, conclusion_txt)

    pdf.output("Chapter_6_Conclusion.pdf", "F")
    print("Chapter 6 PDF generated successfully.")

if __name__ == '__main__':
    create_chap6_pdf()
