from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")

def create_chap2_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_margins(25.4, 25.4, 25.4) # 1 inch margins
    pdf.set_auto_page_break(auto=True, margin=25.4)
    
    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "CHAPTER 2", ln=True, align="C")
    pdf.cell(0, 10, "LITERATURE REVIEW", ln=True, align="C")
    pdf.ln(5)
    
    # 2.1
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1 Literature Review", ln=True)
    pdf.ln(2)

    # 2.1.1
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1.1 Machine Learning in Spam Detection", ln=True)
    pdf.set_font("Arial", "", 12)
    text_211 = (
        "Machine learning, a cornerstone of artificial intelligence, has fundamentally transformed the field "
        "of cybersecurity and data filtering. In the realm of spam detection, models like Support Vector "
        "Machines, Random Forests, and Gradient Boosting algorithms (e.g., XGBoost) have revolutionized the "
        "process of classifying malicious communications. These models are trained on large datasets containing "
        "labeled examples of legitimate (\"Ham\") and unsolicited (\"Spam\") messages. They excel at identifying "
        "statistical patterns, word frequencies, and heuristics indicative of spam.\n\n"
        "The SMS Spam Dashboard project utilizes XGBoost, an optimized distributed gradient boosting library. "
        "This model powers rapid, highly accurate classification based on extracted textual features, serving as "
        "the application's baseline defense against unsolicited texts."
    )
    pdf.multi_cell(0, 7, text_211)
    pdf.ln(5)

    # 2.1.2
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1.2 Natural Language Processing (NLP) and Transformer Models", ln=True)
    pdf.set_font("Arial", "", 12)
    text_212 = (
        "NLP techniques are critical in enabling machines to understand, interpret, and process human language "
        "computationally. In the context of this project, NLP is used for strict contextual analysis of SMS "
        "messages. Modern NLP architecture relies heavily on transformer models, such as BERT and its distilled "
        "variants like DistilBERT. These models process text by capturing bidirectional context and long-range "
        "dependencies between words, allowing them to comprehend semantic nuances that traditional bag-of-words "
        "models might miss.\n\n"
        "In this project, DistilBERT acts as a secondary, highly sophisticated layer of sequence classification. "
        "It evaluates the intricate structure and intent behind the message content, ensuring the classification "
        "remains accurate even when spammers employ obfuscation tactics or advanced vocabulary."
    )
    pdf.multi_cell(0, 7, text_212)
    pdf.ln(5)

    # 2.1.3
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1.3 Active Learning and User Feedback Mechanisms", ln=True)
    pdf.set_font("Arial", "", 12)
    text_213 = (
        "Active learning is a subfield of machine learning where the learning algorithm can interactively query "
        "the user to label new continuous data points. It is particularly effective in environments where data "
        "distribution shifts over time, such as spam filtering where new tactics emerge constantly. By capturing "
        "false-positives and false-negatives, systems can iteratively refine their decision boundaries.\n\n"
        "The SMS Spam Dashboard project incorporates an active learning loop through user feedback integration. "
        "Users can flag misclassified messages directly from their personal dashboards. This feedback acts as "
        "ground-truth data, allowing the system to log trends and ultimately retrain models periodically and "
        "ensuring the application's defensive capabilities evolve dynamically alongside emerging spam frameworks."
    )
    pdf.multi_cell(0, 7, text_213)
    pdf.ln(5)

    # 2.1.4
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1.4 Data Preprocessing for Textual Analysis", ln=True)
    pdf.set_font("Arial", "", 12)
    text_214 = (
        "Data preprocessing is a crucial step in any machine learning or NLP pipeline. It involves cleaning "
        "and preparing raw text data to ensure it is in the right mathematical format for modeling. In the case "
        "of the SMS Spam Dashboard, preprocessing includes text normalization, stop-word removal, and vectorization "
        "techniques like Term Frequency-Inverse Document Frequency (TF-IDF) for the XGBoost model, or specific "
        "neural tokenization for the DistilBERT model.\n\n"
        "The application processing handlers process raw SMS inputs to extract relevant numerical representations "
        "before passing them to the models. This step guarantees that noise - such as special characters, "
        "inconsistent capitalization, or formatting irregularities - is minimized, leading to more robust "
        "classification results."
    )
    pdf.multi_cell(0, 7, text_214)
    pdf.ln(5)

    # 2.1.5
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1.5 User Interface Design for Security Dashboards", ln=True)
    pdf.set_font("Arial", "", 12)
    text_215 = (
        "A well-structured user interface (UI) is critical for any security or predictive tool, as it directly "
        "influences how efficiently users can interpret risks. The front-end representation needs clarity above "
        "all, separating raw data from actionable insights seamlessly.\n\n"
        "For the SMS Spam Dashboard, data isolation is crucial. The interface ensures that each authenticated "
        "user views only their personalized prediction histories. Clear visualizations and historical logs provide "
        "instantaneous feedback on messaging threat levels, while distinctly formatted Call-to-Action elements "
        "simplify the reporting of misclassifications to the active learning pipeline."
    )
    pdf.multi_cell(0, 7, text_215)
    pdf.ln(5)

    # 2.1.6
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1.6 Use of Django Framework for Web Development", ln=True)
    pdf.set_font("Arial", "", 12)
    text_216 = (
        "Django is a high-level Python web framework designed for rapid development and clean, pragmatic design. "
        "It adheres to the Model-View-Template (MVT) architectural pattern, which neatly separates data access, "
        "business logic, and presentation logic.\n\n"
        "In this project, Django acts as the foundational web server. Django's built-in authentication system "
        "manages user isolation effectively, while its Object-Relational Mapping (ORM) layer handles complex "
        "prediction records efficiently. Its robust architecture securely bridges the front-end user experience "
        "with the high-compute backend machine learning inference tasks seamlessly, ensuring stability and "
        "scalability over extended sessions."
    )
    pdf.multi_cell(0, 7, text_216)
    pdf.ln(5)

    # 2.1.7
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "2.1.7 Database Integration for Analytics and History", ln=True)
    pdf.set_font("Arial", "", 12)
    text_217 = (
        "Robust database management is essential for applications that track historical predictions and analytics. "
        "The system requires scalable persistence to store user inputs, generated predictions, and subsequent "
        "feedback securely.\n\n"
        "The SMS Spam Dashboard project leverages a relational database architecture managed natively via "
        "Django's built in ORM to manage these interactions. This ensures that every prediction is securely "
        "logged and associated with the correct user profile. Furthermore, the systematic storage of prediction data "
        "enables the dashboard to render accurate historical metrics, overall spam volume, and timeline statistics, "
        "creating a cohesive analytical tool for the user."
    )
    pdf.multi_cell(0, 7, text_217)

    pdf.output("Chapter_2_Literature_Review.pdf", "F")
    print("Chapter 2 PDF generated successfully.")

if __name__ == '__main__':
    create_chap2_pdf()
