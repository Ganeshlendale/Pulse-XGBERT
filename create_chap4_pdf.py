from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")

def create_chap4_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_margins(25.4, 25.4, 25.4) # 1 inch margins
    pdf.set_auto_page_break(auto=True, margin=25.4)
    
    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "CHAPTER 4", ln=True, align="C")
    pdf.cell(0, 10, "IMPLEMENTATION", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", "", 12)
    intro_txt = (
        "The implementation of the SMS Spam Dashboard project involves the seamless integration of "
        "multiple components, each designed to handle a specific responsibility - from parsing raw user "
        "SMS inputs to producing highly accurate classification results. This chapter explores each part "
        "of the implementation in detail, focusing on how different layers work together to enable "
        "intelligent security metrics using standard machine learning frameworks and secure architectural "
        "principles."
    )
    pdf.multi_cell(0, 7, intro_txt)
    pdf.ln(5)

    # 4.1
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.1 Technology Stack", ln=True)
    pdf.set_font("Arial", "", 12)
    text_41 = (
        "The SMS Spam Dashboard project leverages a robust and modern technology stack to deliver an "
        "intelligent, responsive, and secure spam detection system. Each technology used in the stack "
        "plays a specific role in enabling seamless interaction, efficient data handling, and accurate "
        "message classification.\n\n"
        "Table 4.1: Technology Stack\n"
        "- Python: Core programming language used for developing backend logic, ML inference, and data handling.\n"
        "- Django: Used to build the secure web-based MVT architecture where users log in and view results.\n"
        "- XGBoost: Gradient Boosting Machine Learning algorithm used as the baseline statistical classifier.\n"
        "- DistilBERT: Neural transformer model used to process sequence semantics for complex classification.\n"
        "- SQLite / PostgreSQL: Relational database systems for storing user profiles and prediction histories safely.\n"
        "- scikit-learn & NLTK: Libraries utilized for text normalization and feature extraction (TF-IDF generator).\n\n"
        "Programming Language: Python\n"
        "Python serves as the backbone of this project due to its extensive ecosystem of libraries and frameworks "
        "suited for rapid development, data processing, and machine learning. Its readability and flexibility allow "
        "for modular code organization across the various Django apps.\n\n"
        "Backend & Routing Development: Django\n"
        "The main web system is built using Django, a high-level Python web framework that relies on the "
        "Model-View-Template (MVT) architecture. Django provides secure authentication gates, Object-Relational "
        "Mapping (ORM) to communicate safely with the database, and a robust template engine.\n\n"
        "Machine Learning Integration: XGBoost & DistilBERT\n"
        "A core component of the project is the integration with two targeted Machine Learning frameworks: "
        "XGBoost evaluates statistical term frequency arrays (fast, highly scalable), and DistilBERT evaluates "
        "semantic nuances and complex vocabulary obfuscation through sequence analysis.\n\n"
        "Data Handling & Feature Extraction\n"
        "Unlike generic NLP tasks, spam detection requires rigorous mathematical formatting. NLTK is employed "
        "to filter out useless stop words, while scikit-learn standardizes term-frequency vectorization, mapping "
        "textual strings into high-dimensional numerical formats.\n\n"
        "Configuration & Security\n"
        "Django's native configuration dictates security definitions like CSRF protection, safeguarding the analytical session."
    )
    pdf.multi_cell(0, 7, text_41)
    pdf.ln(5)

    # 4.2
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.2 Frontend Overview and Dashboard UI", ln=True)
    pdf.set_font("Arial", "", 12)
    text_42 = (
        "The frontend of the SMS Spam Dashboard is designed to provide a smooth and secure user experience, "
        "ensuring that users can focus strictly on verifying message safety. Built using Django integration with "
        "HTML, CSS, and interactive design elements, the interface offers a cohesive environment.\n\n"
        "User Input Mechanism\n"
        "Upon launching the dashboard interface, users are presented with a minimalistic, clean layout that "
        "prioritizes text evaluation. The interface includes:\n"
        "- A large validation text area for copying and pasting suspicious SMS messages.\n"
        "- Clear action buttons indicating predictive execution.\n"
        "- Visual navigation bars separating the prediction system from historical database charts.\n\n"
        "User-Centric Security Philosophy\n"
        "Beyond simply classifying text, the dashboard relies heavily on Data Isolation. The UI ensures that a user "
        "only sees charts, graphs, and histories belonging to their specific account, drastically mitigating "
        "digital privacy risks. Historical data updates dynamically to provide real-time accuracy evaluations."
    )
    pdf.multi_cell(0, 7, text_42)
    pdf.ln(5)

    # 4.3
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.3 Text Preprocessing and Feature Extraction", ln=True)
    pdf.set_font("Arial", "", 12)
    text_43 = (
        "The system's ability to classify text accurately is deeply rooted in its preprocessing module. Raw SMS texts "
        "are notoriously noisy - filled with emojis, irregular capitalization, obscure acronyms, and missing punctuation. "
        "A separate module handles standardizing this data:\n\n"
        "- Lowercasing and Stripping: Transforming characters to lowercase to prevent vector duplication.\n"
        "- Punctuation Filtering: Removing unnecessary elements while potentially capturing spam indicators.\n"
        "- Vectorization (TF-IDF): Transforming text using a pretrained model to numerical weights relative to length.\n"
        "- Tokenization: Employing DistilBERT's tokenizer to formulate neural input IDs and mapping sequences.\n\n"
        "This normalization step isolates the structure, significantly reducing artificial inference anomalies."
    )
    pdf.multi_cell(0, 7, text_43)
    pdf.ln(5)

    # 4.4
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.4 Model Integration (XGBoost & DistilBERT)", ln=True)
    pdf.set_font("Arial", "", 12)
    text_44 = (
        "At the heart of the detection process is a dual-integration approach. A dedicated handler file initializes "
        "and manages the loaded Pickle format objects and transformer states.\n"
        "The pipeline delegates numeric arrays to XGBoost to generate a rapid probabilistic base score, while parallel "
        "preprocessing sends tokenized context data to DistilBERT for sequential abstraction.\n"
        "The inference results are mathematically fused based on an optimizing threshold to emit the final binary "
        "verdict (Ham or Spam). The architectural strategy of separating inference scripts from website views prevents "
        "downtime and ensures modular model replacing over time."
    )
    pdf.multi_cell(0, 7, text_44)
    pdf.ln(5)

    # 4.5
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.5 Active Learning & Feedback Implementation", ln=True)
    pdf.set_font("Arial", "", 12)
    text_45 = (
        "The application actively curates new datasets from real-world usage. After a prediction displays, the UI "
        "prompts the user to provide corrective feedback if they suspect a misclassification.\n"
        "When initiated, the system stores the initial message alongside the validated label via Django ORM. This "
        "forms a grounded active-learning table within the server's database. Periodically, network administrators "
        "export this localized dataset back into offline training pools, ensuring deployed models adapt immediately "
        "against novel zero-day spam variants."
    )
    pdf.multi_cell(0, 7, text_45)
    pdf.ln(5)

    # 4.6
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.6 Database Configuration and Data Isolation", ln=True)
    pdf.set_font("Arial", "", 12)
    text_46 = (
        "The records used for personal dashboards and global metrics are handled dynamically through Relational Databases.\n"
        "Structural database architectures include independent user profiles holding secure passwords alongside individual "
        "prediction ledgers. A paramount feature is Data Isolation: strict foreign-key bindings dictate that prediction "
        "histories query only within the active session boundaries. Consequently, no user possesses overlapping access "
        "rights, fulfilling primary data-privacy directives."
    )
    pdf.multi_cell(0, 7, text_46)
    pdf.ln(5)

    # 4.7
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.7 Prediction Workflow", ln=True)
    pdf.set_font("Arial", "", 12)
    text_47 = (
        "The core functionality revolves around the automated verification algorithm. The entire workflow follows:\n"
        "1. User Input Collection: Authenticated user submits raw text.\n"
        "2. Routing & Validation: Backend controllers parse payload integrity and session keys.\n"
        "3. Preprocessing: Handlers extract language nodes and convert strings into compatible format tensors.\n"
        "4. ML Inference: XGBoost & DistilBERT crunch metrics to yield respective probability outputs.\n"
        "5. Storage Binding: The server logs the cumulative classification verdict securely against the user profile.\n"
        "6. Display Rendering: Response passes instantly back to UI via dynamic template population."
    )
    pdf.multi_cell(0, 7, text_47)
    pdf.ln(5)

    # 4.8
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.8 Handling Edge cases and Extensibility", ln=True)
    pdf.set_font("Arial", "", 12)
    text_48 = (
        "The system gracefully accounts for anomalous payloads. Extremely short strings, heavy punctuation densities, "
        "or erratic language switches generally default to neutral confidence limits reducing panic alerts. Furthermore, "
        "the application's highly detached machine learning layer demonstrates enormous programmatic extensibility; "
        "substituting core inference engines for entirely distinct operations (e.g. email or financial classification) "
        "can be seamlessly engineered."
    )
    pdf.multi_cell(0, 7, text_48)

    pdf.output("Chapter_4_Implementation.pdf", "F")
    print("Chapter 4 PDF generated successfully.")

if __name__ == '__main__':
    create_chap4_pdf()
