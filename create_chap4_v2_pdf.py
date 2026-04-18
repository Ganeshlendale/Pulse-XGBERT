from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")

def create_chap4_v2_pdf():
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
        "The implementation of the SMS Spam Dashboard spans five primary domains: Machine Learning "
        "model compilation, text preprocessing integration, Django backend architecture, frontend UI "
        "construction, and relational database design. Each domain is implemented as an independent "
        "module with well-defined interfaces, enabling parallel development and isolated testing. This "
        "chapter details the implementation decisions, code architecture, and key technical challenges "
        "resolved during development."
    )
    pdf.multi_cell(0, 7, intro_txt)
    pdf.ln(5)

    # 4.1
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.1 Technology Stack", ln=True)
    pdf.set_font("Arial", "", 12)
    
    tech_table = (
        "Table 4.1 : Technology Stack of SMS Spam Dashboard\n\n"
        "- Django Framework: Core web framework - renders the dashboard, routing, and user interface.\n"
        "- XGBoost: Machine Learning library - manages the statistical classification of tabular text arrays.\n"
        "- DistilBERT (HuggingFace): Deep Learning Transformer - executes sequence classification on text intent.\n"
        "- SQLite / PostgreSQL: Relational Database - securely stores user profiles, scanned SMS records, and feedback.\n"
        "- scikit-learn & NLTK: NLP tools - performs text normalization and TF-IDF feature extraction.\n"
        "- HTML / CSS: Frontend styling - provides responsive UI design across desktop and mobile viewports.\n"
        "- Django ORM: Database Abstraction - securely handles SQL transactions and user data isolation."
    )
    pdf.multi_cell(0, 7, tech_table)
    pdf.ln(5)

    # 4.2
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.2 Frontend and UI", ln=True)
    pdf.set_font("Arial", "", 12)
    frontend_txt = (
        "The SMS Spam Dashboard application is bootstrapped using Django's template engine for fast, server-side "
        "rendering. The UI is styled directly, providing a clean, utility-first, responsive design system that "
        "renders correctly across desktop, tablet, and mobile viewports.\n\n"
        "The central Dashboard page renders a text validation area and fetches paginated data from the backend "
        "database. Each history record displays the original text, predicted classification label (Ham/Spam), "
        "confidence score, timestamp, and quick-action buttons for verifying accuracy to flag misclassifications.\n\n"
        "Table 4.2 : System Interaction Types\n"
        "- Standard Scan: Single SMS execution, instant evaluation, immediate UI redirect.\n"
        "- Active Feedback: User modifies predicted context; adds text metrics back to learning database.\n"
        "- Batch Review: User navigates history page to review overarching analytical trends and threat levels."
    )
    pdf.multi_cell(0, 7, frontend_txt)
    pdf.ln(5)

    # 4.3
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.3 Prediction Engine Implementation", ln=True)
    pdf.set_font("Arial", "", 12)
    engine_txt = (
        "The processing logic is the technical heart of the SMS Dashboard. Distinct Django views and function "
        "wrappers work in concert to power all system operations securely.\n\n"
        "Table 4.3 : Key Handlers and Functions\n"
        "- predict_message(text): Model App - Cleans string, executes dual-inference (XGB & BERT), emits ratio.\n"
        "- record_feedback(id, label): Profile System - Updates specific classification record for future active learning.\n"
        "- user_dashboard(request): Pages App - Fetches active historical records bound to the user's session key.\n"
        "- auth_user(request): Core App - Manages creation and destruction of secure login cookies."
    )
    pdf.multi_cell(0, 7, engine_txt)
    pdf.ln(5)

    # 4.4
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.4 Text Preprocessing and Feature Extraction", ln=True)
    pdf.set_font("Arial", "", 12)
    preproc_txt = (
        "When a user initiates a scan, the frontend POSTs the raw SMS. Preprocessing algorithms remove whitespace, "
        "stop words, and normalize punctuation directly before interference execution.\n"
        "Upon successful cleaning, the backend splits the pipeline:\n"
        "1. TF-IDF vectorization transforms the string into an array matrix for the XGBoost statistical tree.\n"
        "2. Tokenization via the HuggingFace engine generates semantic representations for the DistilBERT neural process.\n"
        "These highly formatted mathematical parameters are essential; the models do not process native strings natively."
    )
    pdf.multi_cell(0, 7, preproc_txt)
    pdf.ln(5)

    # 4.5
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.5 Django Backend UI and MVT Structure", ln=True)
    pdf.set_font("Arial", "", 12)
    backend_txt = (
        "The web application backend is strictly organized using a domain-driven Model-View-Template directory layout: "
        "/core, /pages, /model_app, and /profile_system. The server communicates directly with the designated SQLite "
        "database securely utilizing built-in ORM protections.\n"
        "Events executed by the python application are indexed utilizing session checks. Context payloads containing "
        "model accuracy strings, database logs, and graph metrics are processed seamlessly on the backend before the "
        "HTML rendering cycle concludes."
    )
    pdf.multi_cell(0, 7, backend_txt)
    pdf.ln(5)

    # 4.6
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.6 Relational Schema Design", ln=True)
    pdf.set_font("Arial", "", 12)
    schema_txt = (
        "The primary prediction document schema securely stores: user_id (tenant foreign key), prediction_label, "
        "confidence_score, initial_text, feedback_status, and createdAt timestamp. Django's aggregated annotations "
        "compute derived fields dynamically such as ratio distributions over time.\n"
        "Trend scores are evaluated chronologically via active session tokens. All relational mapping is handled via "
        "migrations, heavily indexing lookup tables mapped tightly preventing massive query lags."
    )
    pdf.multi_cell(0, 7, schema_txt)
    pdf.ln(5)

    # 4.7
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.7 End-to-End Prediction Workflow", ln=True)
    pdf.set_font("Arial", "", 12)
    workflow_txt = (
        "The complete classification workflow proceeds as follows:\n"
        "(1) User pastes the raw SMS string into the frontend form.\n"
        "(2) Form triggers a secure POST request intercept to the Django backend routing.\n"
        "(3) The predict handler captures payload, confirming session authorizations to thwart unauthorized access.\n"
        "(4) Payload passes to textual processing: variables stripped and numeric arrays formed.\n"
        "(5) Deep learning inference runs on parsed tokens in memory. Ratio combined against statistical baselines.\n"
        "(6) Model synthesizes final designation and establishes a new committed dataset log.\n"
        "(7) The View re-fires a successful HTTP block, updating UI cleanly displaying the verdict to the user."
    )
    pdf.multi_cell(0, 7, workflow_txt)
    pdf.ln(5)

    # 4.8
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "4.8 Handling Edge Cases and Extensibility", ln=True)
    pdf.set_font("Arial", "", 12)
    edge_txt = (
        "Edge cases are handled systematically at each layer. Empty strings or exclusively non-UTF characters are "
        "rejected swiftly at the frontend. If inference engines panic due to mathematical overflow, the backend "
        "gracefully cascades an exception block preventing a total server crash.\n"
        "The platform's module boundaries are designed for future extensibility. New language models or SMS parsing "
        "APIs can be integrated by attaching additional application nodes to the primary Django project without "
        "overwriting core authentication logic."
    )
    pdf.multi_cell(0, 7, edge_txt)

    pdf.output("Chapter_4_Implementation_v2.pdf", "F")
    print("Chapter 4 Alternative PDF generated successfully.")

if __name__ == '__main__':
    create_chap4_v2_pdf()
