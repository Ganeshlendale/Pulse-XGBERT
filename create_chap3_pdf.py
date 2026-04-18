from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")

def create_chap3_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_margins(25.4, 25.4, 25.4) # 1 inch margins
    pdf.set_auto_page_break(auto=True, margin=25.4)
    
    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "CHAPTER 3", ln=True, align="C")
    pdf.cell(0, 10, "SYSTEM DESIGN", ln=True, align="C")
    pdf.ln(5)
    
    # 3.1 Overview
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "3.1 Overview", ln=True)
    pdf.set_font("Arial", "", 12)
    text_31 = (
        "The SMS Spam Dashboard project has been architected as a modular, end-to-end classification "
        "system leveraging Machine Learning (XGBoost) and Natural Language Processing (DistilBERT). The "
        "system is capable of accurately categorizing incoming SMS messages as \"Spam\" or \"Ham\" based "
        "on user inputs, historical dataset training, and contextual logic. It operates by combining a "
        "robust, tenant-isolated frontend interface with a backend driven by feature extraction, statistical "
        "inference, and an active learning feedback loop.\n\n"
        "This system has been designed with reusability, scalability, and security in mind, making it suitable "
        "not only for personal SMS spam filtering but also for scalable deployment across enterprise "
        "telecommunications networks."
    )
    pdf.multi_cell(0, 7, text_31)
    pdf.ln(5)

    # 3.2 Flow Chart
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "3.2 Flow Chart", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, "Fig 3.2 : Flow Chart for SMS Spam Detection System", ln=True)
    pdf.ln(5)

    # 3.3 High-Level Architecture
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "3.3 High-Level Architecture", ln=True)
    pdf.set_font("Arial", "", 12)
    text_33_intro = "At a high level, the system consists of the following layers:"
    pdf.cell(0, 7, text_33_intro, ln=True)
    pdf.ln(2)

    arch_points = [
        ("1. User Interface Layer (Frontend using Django Templates & UI styling)",
         "This layer provides the interactive frontend for users to interact with the system securely. "
         "Built using Django templates and modern styling, it includes:\n"
         "- Secure authentication gateways (login/register).\n"
         "- A central dashboard for inputting text to be classified.\n"
         "- Graphical representations of the user's prediction history and accuracy stats.\n"
         "This layer ensures the system is easy to use, visually intuitive, and secure from unauthorized access."),
        
        ("2. Application Logic Layer (Django Views & Routing)",
         "This is the core engine of the system that controls the logic behind:\n"
         "- Validating authenticated users and ensuring strict tenant data isolation.\n"
         "- Handling incoming HTTP requests and routing data to the appropriate model handlers.\n"
         "- Processing user feedback (misclassifications) for the active learning database.\n"
         "This layer handles the decision-making orchestration, ensuring secure execution and responsive interface updates."),

        ("3. Data Preparation & Preprocessing Layer",
         "This backend layer handles data cleaning and vectorization, which is a crucial step for accurate machine "
         "learning inference:\n"
         "- Takes raw SMS text input from the user.\n"
         "- Performs text normalization, stop-word removal, and stemming/lemmatization.\n"
         "- Applies Term Frequency-Inverse Document Frequency (TF-IDF) for the statistical model and neural tokenization "
         "for the transformer model.\n"
         "This layer transforms unfiltered text into computable matrices suitable for machine learning predictions."),

        ("4. Machine Learning Inference Layer (XGBoost & DistilBERT)",
         "This layer is responsible for the predictive classification modeling:\n"
         "- Integrates a trained predictive XGBoost algorithm for baseline statistical scoring.\n"
         "- Utilizes the DistilBERT model for deep sequence and contextual understanding.\n"
         "- Aggregates the confidence scores from both models to finalize the prediction.\n"
         "This hybrid modeling layout ensures low-latency execution while retaining complex intent understanding."),

        ("5. Data Storage (Relational Database)",
         "This is the storage and persistence layer managed by Django ORM:\n"
         "- User profiles and session management records are securely stored.\n"
         "- Prediction history containing input text, date, and spam probabilities are saved under isolated user-keys.\n"
         "- Active learning feedback logs are captured to maintain a growing ground-truth dataset.\n"
         "This highly organized approach ensures the robust tracking of analytics while maintaining absolute data privacy.")
    ]

    for title, desc in arch_points:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 7, title, ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 7, desc)
        pdf.ln(3)

    pdf.add_page() # Need new page probably or it handles it automatically. Auto is ON.

    # 3.4 Component-Wise Design
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "3.4 Component-Wise Design", ln=True)
    pdf.set_font("Arial", "", 12)

    comp_points = [
        ("1. Django MVT Frontend",
         "This component facilitates interaction between the user and the backend system. It captures inputs securely:\n"
         "- Profile System: Manages authentication, user creation, and session boundaries.\n"
         "- SMS Input Handler: A dedicated text area for user submissions.\n"
         "- Interactive Feedback: Buttons that allow users to flag predictions as correct or incorrect.\n"
         "Once the user submits a text, the system routes this input to the views.py modules, which act as the system controllers."),
        
        ("2. Text Preprocessing Pipeline",
         "This module is the foundation for model comprehension. It:\n"
         "- Reads raw text strings submitted from the frontend payload.\n"
         "- Cleans anomalies such as irregular casing or extraneous symbols.\n"
         "- Transforms the data through a TF-IDF vectorizer (for XGBoost) and a HuggingFace Tokenizer (for DistilBERT).\n"
         "This process translates unstructured data into high-dimensional numerical vectors that the models require for probabilistic scoring."),

        ("3. Prediction Engine",
         "The classification is the key technique implemented. This module:\n"
         "- Loads pre-trained model weights (XGBoost arrays and DistilBERT PyTorch states).\n"
         "- Executes real-time inference on the processed text.\n"
         "- Applies a thresholding equation to fuse the probabilities of both models into a single, definitive binary category (Spam vs. Ham).\n"
         "These steps are strictly optimized for computational efficiency, providing near-instantaneous feedback."),

        ("4. Active Learning Supervisor",
         "This component orchestrates the continuous improvement lifecycle. It:\n"
         "- Intercepts user feedback from the frontend (e.g., when a user clicks \"Report false positive\").\n"
         "- Formats the original text alongside the corrected label and commits it to a specialized feedback database table.\n"
         "- Acts as a repository for future model retuning, making the system adaptive to novel \"zero-day\" spam architectures."),

        ("5. Database Integration",
         "This module handles all long-term memory metrics. It:\n"
         "- Employs SQLite or PostgreSQL managed via Django ORM.\n"
         "- Enforces strict foreign-key relations connecting prediction records only to their authoring user accounts.\n"
         "- Aggregates system metrics (Total Scans, Spam Ratio) efficiently to populate the dynamic dashboard charts.")
    ]

    for title, desc in comp_points:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 7, title, ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 7, desc)
        pdf.ln(3)

    # 3.5 Data Flow Diagram
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "3.5 Data Flow Diagram", ln=True)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Fig 3.5 : Data Flow Diagram", ln=True)
    pdf.set_font("Arial", "", 12)
    
    flow_steps = (
        "1. User securely logs in and submits raw SMS text on the dashboard.\n"
        "2. Backend views capture the text and forward it to the preprocessing handlers.\n"
        "3. Preprocessed tokens are fed into the XGBoost and DistilBERT inference engines.\n"
        "4. The system aggregates confidence scores and commits the result to the user's database footprint.\n"
        "5. The dashboard dynamically updates to reflect the latest prediction, graph analytics, and offers the option to submit feedback."
    )
    pdf.multi_cell(0, 7, flow_steps)
    pdf.ln(5)

    # 3.6 Design Considerations
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "3.6 Design Considerations", ln=True)

    design_points = [
        ("Modularity",
         "The system is architected with a strict modular Model-View-Template design, where each key functionality "
         "is encapsulated within independent Django apps (core, pages, profile_system, model_app). This clean separation "
         "of concerns simplifies debugging, database migrations, and testing. It allows independent modules to be "
         "altered without disrupting user session logic."),
        
        ("Scalability",
         "The system is designed to accommodate a high volume of users. By separating the web server logic from the heavy "
         "machine learning inference processes, the deployment can scale horizontally. The relational database is similarly "
         "structured to support indexing large volumes of prediction histories and feedback metrics without querying bottlenecks."),

        ("Data Privacy and Isolation",
         "In contrast to public content generators, a security dashboard mandates absolute privacy. The design "
         "fundamentally segregates data through user-authenticated foreign keys. A user has zero physical or programmatic "
         "access to another user's spam history."),

        ("Reusability",
         "The preprocessing pipelines and machine-learning wrappers are implemented as stateless utility classes. This "
         "means they can easily be extracted to form a generic REST API if the project later requires deployment as a "
         "microservice for external mobile or web clients."),

        ("Customization and Lifespan",
         "While currently tuned to SMS formats, the design possesses adaptability. Through ongoing Active Learning pipelines, "
         "administrators can gradually shift the model's focus (for instance, to email classification or enterprise phishing "
         "detection) simply by pushing periodic model updates derived from new user feedback, ensuring indefinite platform relevancy.")
    ]

    for title, desc in design_points:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 7, title, ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 7, desc)
        pdf.ln(3)

    pdf.output("Chapter_3_System_Design.pdf", "F")
    print("Chapter 3 PDF generated successfully.")

if __name__ == '__main__':
    create_chap3_pdf()
