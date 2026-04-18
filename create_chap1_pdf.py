from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")

def create_chap1_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_margins(25.4, 25.4, 25.4) # 1 inch margins
    
    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "CHAPTER 1", ln=True, align="C")
    pdf.cell(0, 10, "INTRODUCTION", ln=True, align="C")
    pdf.ln(5)
    
    # Introduction Paragraph
    pdf.set_font("Arial", "", 12)
    intro_text = (
        "In today's interconnected digital ecosystem, SMS (Short Message Service) remains a primary "
        "communication channel for individuals and businesses. However, the proliferation of unsolicited "
        "and malicious messages - commonly known as spam - poses a significant threat to user privacy, "
        "security, and productivity. To address this persistent issue, the SMS Spam Dashboard project "
        "leverages Machine Learning (ML) and Natural Language Processing (NLP) to automatically classify "
        "and filter incoming text messages. The goal of this project is to create an intuitive, secure, "
        "and robust platform that empowers users to identify spam accurately, maintain isolated personal "
        "prediction histories, and continuously improve the system via active learning feedback mechanisms."
    )
    pdf.multi_cell(0, 7, intro_text)
    pdf.ln(5)
    
    # 1.1 Background
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "1.1 Background", ln=True)
    pdf.set_font("Arial", "", 12)
    background_text = (
        "With the increasing reliance on mobile communications, spam messages have evolved from mere "
        "annoyances to sophisticated phishing vectors. Effectively identifying these threats requires "
        "continuous vigilance and advanced text analysis. The SMS Spam Dashboard aims to mitigate these "
        "risks by combining traditional machine learning approaches and state-of-the-art transformer "
        "models to classify messages dynamically and securely.\n\n"
        "This project involves several key technical elements: data preprocessing, feature extraction, "
        "sequence classification, and user session management. By leveraging models like XGBoost and "
        "DistilBERT, the system can parse textual nuances and detect deceptive patterns effectively. "
        "Additionally, the secure, authenticated environment ensures that users can manage their "
        "prediction histories privately without data overlap.\n\n"
        "By automating the detection pipeline, this tool provides individuals and organizations with "
        "a reliable safeguard against SMS-based threats. Built using the Django web framework for "
        "scalable backend architecture and modern web design principles for the frontend, it delivers "
        "an end-to-end classification system. It not only saves users time but actively protects them "
        "in an increasingly complex telecommunications landscape."
    )
    pdf.multi_cell(0, 7, background_text)
    pdf.ln(5)

    # 1.2 Objectives
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "1.2 Objectives", ln=True)
    pdf.set_font("Arial", "", 12)
    obj_intro = (
        "The SMS Spam Dashboard project is designed with the goal of enabling users to effortlessly "
        "identify malicious messages in real-time through the power of advanced ML models. The system "
        "brings together modern NLP, secure web architecture, and continuous user-driven improvement. "
        "The following objectives have been set to guide the development and success of the project:"
    )
    pdf.multi_cell(0, 7, obj_intro)
    pdf.ln(3)

    objectives = [
        ("1. Robust Spam Classification", 
         "To design and implement a machine learning system capable of classifying SMS messages as "
         "'Spam' or 'Ham' with high accuracy. The application utilizes a hybrid approach, deploying "
         "both XGBoost for efficient statistical feature evaluation and DistilBERT for deep contextual "
         "analysis of vocabulary and sentence structure, providing highly reliable predictions."),
        ("2. Secure and Isolated User Dashboard",
         "To develop a clean, responsive, and secure user interface using Django templates and modern "
         "styling. The system mandates user authentication, ensuring that each user has a personalized, "
         "private dashboard where they can track their individual prediction histories, overall statistics, "
         "and recent activity securely, with strict tenant-level data isolation."),
        ("3. Active Learning and Feedback Loops",
         "To incorporate a continuous learning mechanism where users can provide feedback on the model's "
         "predictions. The system captures and stores this feedback (e.g., misclassified 'Ham' or 'Spam'), "
         "which acts as a foundational dataset for future active learning and periodic retraining. This "
         "ensures the model adapts to new and evolving spam patterns dynamically."),
        ("4. Comprehensive Data Visualization",
         "To provide users with insightful, easy-to-understand metrics regarding their usage and the "
         "platform's efficiency. The dashboard calculates and displays key performance indicators (KPIs), "
         "such as the total volume of messages scanned, the distribution of Spam versus Ham, and historical "
         "tracking to help users monitor trends effectively."),
        ("5. Scalable Backend Architecture",
         "To leverage the Django framework's robust Model-View-Template (MVT) architecture for clean "
         "separation of concerns. This includes distinct functional applications for core website routing "
         "(landing page), user authentication (profile system), and the AI prediction engine (model app), "
         "ensuring that the codebase is highly modular, maintainable, and extensible.")
    ]

    for title, desc in objectives:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 7, title, ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 7, desc)
        pdf.ln(3)

    # 1.3 Purpose of the project
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "1.3 Purpose of the project", ln=True)
    pdf.set_font("Arial", "", 12)
    purpose_text = (
        "The purpose of the SMS Spam Dashboard project is to develop an intelligent, secure tool that "
        "empowers users to detect and filter harmful SMS content automatically based on user-submitted "
        "text. By combining advanced NLP transformers (DistilBERT), machine learning classification "
        "(XGBoost), and a strictly isolated Django-based user interface, the project aims to simplify "
        "digital security for the everyday user. This tool provides peace of mind, allowing users to "
        "verify questionable messages instantly and maintain a safer personal telecommunications "
        "environment without needing technical expertise."
    )
    pdf.multi_cell(0, 7, purpose_text)

    pdf.output("Chapter_1_Introduction.pdf", "F")
    print("Chapter 1 PDF generated successfully.")

if __name__ == '__main__':
    create_chap1_pdf()
