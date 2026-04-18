from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)

def create_toc_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    
    # Title
    pdf.cell(0, 10, "TABLE OF CONTENTS", ln=True, align="C")
    pdf.ln(5)
    
    # Content body
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "1. CHAPTER 1 - INTRODUCTION ........................9-12", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "    1.1. Background...................................9", ln=True)
    pdf.cell(0, 8, "    1.2. Objectives...................................10", ln=True)
    pdf.cell(0, 8, "    1.3. Purpose of the Project.......................12", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2. CHAPTER 2 - LITERATURE SURVEY......................13-15", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "    2.1. Project Literature Review....................13", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "3. CHAPTER 3 - SYSTEM DESIGN..........................16-22", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "    3.1. Overview.....................................16", ln=True)
    pdf.cell(0, 8, "    3.2. Flowchart of the project.....................16", ln=True)
    pdf.cell(0, 8, "    3.3. High Level Architecture......................17", ln=True)
    pdf.cell(0, 8, "    3.4. Component-wise Design........................19", ln=True)
    pdf.cell(0, 8, "    3.5. Data Flow Diagram............................21", ln=True)
    pdf.cell(0, 8, "    3.6. Design Considerations........................21", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4. CHAPTER 4 - IMPLEMENTATION.........................23-31", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "    4.1. Technology Stack.............................23", ln=True)
    pdf.cell(0, 8, "    4.2. Frontend Overview and Dashboard UI...........25", ln=True)
    pdf.cell(0, 8, "    4.3. Text Preprocessing and Feature Extraction....27", ln=True)
    pdf.cell(0, 8, "    4.4. Model Integration (XGBoost & DistilBERT).....28", ln=True)
    pdf.cell(0, 8, "    4.5. Active Learning & Feedback Implementation....28", ln=True)
    pdf.cell(0, 8, "    4.6. Database Configuration and Data Isolation....30", ln=True)
    pdf.cell(0, 8, "    4.7. Prediction Workflow..........................30", ln=True)
    pdf.cell(0, 8, "    4.8. Handling Edge cases and Extensibility........31", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "5. CHAPTER 5 - RESULTS AND EVALUATION.................32-33", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "    5.1 Sample Outputs................................32", ln=True)
    pdf.cell(0, 8, "    5.2 Evaluation Criteria...........................34", ln=True)
    pdf.cell(0, 8, "    5.3 Performance & Responsiveness..................34", ln=True)
    pdf.cell(0, 8, "    5.4 Future Scope..................................35", ln=True)
    pdf.cell(0, 8, "    5.5 Project Summary...............................37", ln=True)
    pdf.ln(3)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "6. CHAPTER 6 - CONCLUSION.............................42", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "    6.1 Conclusion....................................42", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "LIST OF FIGURES", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "1. Fig 3.2 : Flow Chart for SMS Spam Detection System........16", ln=True)
    pdf.cell(0, 8, "2. Fig 3.5 : Data Flow Diagram...............................21", ln=True)
    pdf.cell(0, 8, "3. Fig 4.2 : Django Web UI for SMS Spam Dashboard............26", ln=True)
    pdf.cell(0, 8, "4. Fig 5.1.1 : Output for correctly identified Spam message..32", ln=True)
    pdf.cell(0, 8, "5. Fig 5.1.2 : User Dashboard indicating Prediction History..33", ln=True)
    pdf.cell(0, 8, "6. Fig 5.1.3 : Feedback view in the application database.....33", ln=True)

    pdf.output("Table_of_Contents.pdf", "F")
    print("PDF generated successfully.")

if __name__ == '__main__':
    create_toc_pdf()
