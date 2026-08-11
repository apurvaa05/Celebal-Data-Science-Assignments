# 🤖 Autonomous Data Science Co-Pilot

An AI-powered data analysis application that allows users to upload CSV, Excel, and JSON datasets and perform data analysis using natural-language questions.

The system uses an LLM through LangChain to generate Python/Pandas code, executes the generated code, detects failures, retrieves relevant Python/Pandas documentation using RAG, and uses a Recovery Agent to correct failed code and re-execute it. The system can also generate visualizations, insights, and downloadable PDF reports.

---

## 🚀 Features

- Upload CSV, Excel (.xlsx), and JSON datasets
- Ask data-analysis questions using natural language
- AI-generated Python/Pandas code
- Automatic code execution
- Execution error detection
- Automatic error recovery
- Retrieval-Augmented Generation (RAG)
- Sentence Transformer embeddings
- FAISS vector similarity search
- LangChain-based LLM orchestration
- OpenRouter API integration
- Automatic chart selection
- Interactive Plotly visualizations
- AI-generated data insights
- Downloadable PDF analysis reports
- Streamlit web interface

---

## 📸 Project Screenshots

### Demo 1 — JSON Dataset

![Demo 1](screenshots/image1.jpeg)

### Demo 2 — Excel Dataset

![Demo 2](screenshots/image2.jpeg)

### Demo 3 — Titanic CSV Dataset

![Demo 3](screenshots/image3.jpeg)

### Demo 4 — Iris CSV Dataset

![Demo 4](screenshots/image4.jpeg)

### Demo 5 — Employee CSV Dataset

![Demo 5](screenshots/image5.jpeg)

### Demo 6

![Screenshot 6](screenshots/image6.jpeg)

### Demo 7

![Screenshot 7](screenshots/image7.jpeg)

### Demo 8

![Screenshot 8](screenshots/image8.jpeg)

### Demo 9

![Screenshot 9](screenshots/image9.jpeg)

### Demo 10

![Screenshot 10](screenshots/image10.jpeg)

### Demo 11

![Screenshot 11](screenshots/image11.jpeg)

### Demo 12

![Screenshot 12](screenshots/image12.jpeg)

### Demo 13

![Screenshot 13](screenshots/image13.jpeg)

-------

## 🏗️ Project Architecture

    User
      |
      v
    Streamlit Interface
      |
      v
    Dataset Upload
      |
      v
    Natural Language Question
      |
      v
    Planner Agent
      |
      v
    LangChain + LLM
      |
      v
    Generated Python/Pandas Code
      |
      v
    Execution Engine
      |
      +--------------------+
      |                    |
    Success              Error
      |                    |
      v                    v
    Result           Recovery Agent
                           |
                           v
                         RAG
                           |
                           v
                 Sentence Transformers
                           |
                           v
                         FAISS
                           |
                           v
                Relevant Documentation
                           |
                           v
                    LangChain + LLM
                           |
                           v
                    Corrected Code
                           |
                           v
                     Re-execution
                           |
                           v
                  Final Result
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
       Visualization    Insights      PDF Report

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | Data loading and analysis |
| NumPy | Numerical operations |
| LangChain | LLM integration and orchestration |
| ChatOpenAI | LLM interface used through LangChain |
| OpenRouter | LLM API provider |
| Sentence Transformers | Text embeddings |
| FAISS | Vector similarity search |
| Plotly | Interactive visualizations |
| ReportLab | PDF report generation |

---

## 📂 Project Structure

    autonomous-data-science-copilot/
    │
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    │
    ├── agents/
    │   ├── planner.py
    │   ├── executor.py
    │   └── recovery.py
    │
    ├── services/
    │   ├── llm_service.py
    │   ├── rag_service.py
    │   ├── visualization_service.py
    │   ├── chart_selector.py
    │   ├── insight_service.py
    │   └── report_service.py
    │
    ├── utils/
    │   └── loader.py
    │
    ├── generated/
    │   └── analysis_report.pdf
    │
    ├── uploads/
    │
    ├── vectorstore/
    │
    ├── test_executor.py
    ├── test_llm.py
    └── test_recovery.py

---

## ⚙️ Project Flow

### 1. Dataset Upload

The user uploads a CSV, Excel, or JSON file through the Streamlit interface.

The application loads the dataset into a Pandas DataFrame.

### 2. User Query

The user asks a question in natural language.

Example:

    Show average salary by department

### 3. Planner Agent

The Planner Agent analyzes the user's question and the dataframe schema.

It prepares a prompt for the LLM so that the model understands the available columns and the required data-analysis operation.

### 4. LangChain + LLM

LangChain is used to communicate with the LLM.

The project uses the ChatOpenAI interface from LangChain with OpenRouter as the API provider.

The LLM generates Python/Pandas code.

Example:

    df.groupby("Department")["Salary"].mean()

### 5. Execution Engine

The generated Python code is passed to the Execution Engine.

The Execution Engine executes the code against the uploaded dataframe and captures the result.

Example result:

    Finance    72000.0
    HR         50000.0
    IT         60000.0

### 6. Failure Detection

If the generated code produces an exception, the failure is captured instead of simply stopping the application.

For example:

    KeyError: 'salary'

This can happen when the LLM generates:

    df["salary"]

while the actual dataframe contains:

    Salary

### 7. Recovery Agent

The Recovery Agent receives:

- Generated code
- Execution error
- DataFrame columns/schema

It then attempts to correct the generated code.

### 8. RAG System

The Recovery Agent uses the RAG system to retrieve relevant documentation.

The project contains Python/Pandas documentation that is converted into searchable vector representations.

The query is converted into an embedding using Sentence Transformers.

FAISS performs similarity search and retrieves the most relevant documentation.

Example:

    Query:
    Pandas KeyError when accessing a dataframe column

The RAG system can retrieve information explaining that a KeyError may occur when a dataframe column does not exist and that df.columns can be used to verify the actual column names.

### 9. Corrected Code

The retrieved documentation is provided as context to the LLM through the recovery process.

The LLM generates corrected Python/Pandas code.

### 10. Re-execution

The corrected code is executed again.

If successful, the final result is returned to the user.

This creates the self-correction loop:

    Generate
        ↓
    Execute
        ↓
    Error
        ↓
    Retrieve relevant knowledge
        ↓
    Recover
        ↓
    Re-execute

### 11. Visualization

The system determines an appropriate chart based on the analysis result.

Plotly is used to create interactive visualizations.

### 12. Insights

The system generates useful observations from the analysis results.

### 13. PDF Report

The application can generate a professional PDF report using ReportLab.

---

## 🔎 RAG Pipeline

    Documentation
          |
          v
      Text Chunks
          |
          v
    Sentence Transformer
          |
          v
       Embeddings
          |
          v
         FAISS
          |
          v
    Similarity Search
          |
          v
    Relevant Documents
          |
          v
    Recovery Context
          |
          v
     LangChain + LLM
          |
          v
    Corrected Code

---

## 🧠 Why RAG Is Used

A normal LLM may generate incorrect code because it does not know the exact dataframe schema or may make assumptions about Python/Pandas APIs.

RAG provides additional relevant documentation to the model during recovery.

This improves the chances of generating a correct solution and makes the recovery process more reliable.

---

## 🔗 Why LangChain Is Used

LangChain is an important part of the project because it provides the framework used to integrate and orchestrate the LLM.

The project uses LangChain's ChatOpenAI interface to communicate with the OpenRouter-hosted model.

The basic flow is:

    Application
        ↓
    LangChain
        ↓
    ChatOpenAI
        ↓
    OpenRouter API
        ↓
    LLM
        ↓
    Response

LangChain is also useful for structuring prompts and managing the interaction between the different components of the AI pipeline.

---

## 🔐 API Configuration

The project uses OpenRouter as the LLM API provider.

The API key is stored in an environment variable instead of being hard-coded.

Create a .env file:

    OPENROUTER_API_KEY=your_api_key_here

Never commit the actual API key to GitHub.

The .env file should be included in .gitignore.

---

## ▶️ Installation

### 1. Clone the repository

    git clone <YOUR_GITHUB_REPOSITORY_URL>

    cd autonomous-data-science-copilot

### 2. Create a virtual environment

    python -m venv venv

### 3. Activate the virtual environment

Windows PowerShell:

    .\venv\Scripts\Activate.ps1

### 4. Install dependencies

    pip install -r requirements.txt

---

## ▶️ Run the Application

After activating the virtual environment:

    streamlit run app.py

The application will open in the browser.

---

## 🧪 Testing

### Test LLM

    python test_llm.py

This verifies that the LLM integration is generating Python/Pandas code.

### Test Execution Engine

    python test_executor.py

Example:

    Generated Code:

    df.groupby("Department")["Salary"].mean()

    Execution Result:

    Finance    72000.0
    HR         50000.0
    IT         60000.0

### Test Recovery Agent

    python test_recovery.py

This verifies that the Recovery Agent can receive failed code and an execution error and attempt to recover the solution using the RAG pipeline.

### Test RAG

The RAG system can be tested by retrieving documentation relevant to a query such as:

    Pandas KeyError when accessing a dataframe column

The system uses Sentence Transformers and FAISS to retrieve relevant documentation.

---

## 📊 Supported File Formats

The application supports:

- CSV
- Excel (.xlsx)
- JSON

---

## 💡 Example Questions

The user can ask questions such as:

    Show average salary by department

    Which department has the highest average salary?

    Show the distribution of salary.

    Which region has the highest sales?

    Show sales by category.

    Show the trend of sales over time.

    Find the top 5 products by sales.

---

## ⚠️ Difficulties Faced During Development

### 1. LLM-generated code errors

LLMs can generate syntactically valid code that is still incorrect for the uploaded dataset.

For example, the model may use:

    df["salary"]

when the actual column is:

    df["Salary"]

This was handled using the Recovery Agent and RAG.

### 2. DataFrame schema differences

Different datasets contain different column names, data types, and structures.

The system therefore provides dataframe information to the LLM instead of assuming fixed columns.

### 3. RAG integration

The documentation had to be converted into embeddings and indexed using FAISS so that relevant information could be retrieved based on semantic similarity.

### 4. Dependency compatibility

The project uses several AI/ML libraries such as PyTorch, Sentence Transformers, Transformers, FAISS, and LangChain.

Ensuring compatible package versions and Python versions was an important part of setting up the project.

### 5. LLM API integration

The project required integrating an external LLM API while keeping the API key secure using environment variables.

### 6. Automatic visualization

Different analysis results require different chart types.

Therefore, chart selection was separated into its own service instead of hard-coding one visualization.

---

## 🔒 Security Considerations

The project should not expose API keys in source code.

The API key is stored in .env.

The .env file should never be pushed to GitHub.

Generated Python code should ideally be executed inside a restricted sandbox in a production environment because executing LLM-generated code directly can introduce security risks.

---

## 🎯 Key Advantages

- Allows non-technical users to perform data analysis using natural language
- Automates Python/Pandas code generation
- Uses LangChain for LLM integration
- Uses RAG for knowledge retrieval
- Uses FAISS for semantic search
- Includes automatic error recovery
- Provides interactive visualizations
- Generates AI-based insights
- Produces PDF reports
- Uses a modular architecture

---

## 🔮 Future Improvements

### 1. Secure Code Sandbox

Move generated code execution into an isolated subprocess, container, or sandbox.

### 2. Better Agent Planning

Improve the Planner Agent so complex questions can be broken into multiple analysis steps.

### 3. Improved Recovery

Allow bounded recovery attempts instead of unlimited retries.

### 4. Better RAG

Improve document chunking, metadata filtering, reranking, and retrieval quality.

### 5. Conversation Memory

Allow users to ask follow-up questions based on previous analysis.

Example:

    User:
    What is the average salary by department?

    User:
    Now show it as a bar chart.

### 6. Database Support

Extend the system to support SQL databases in addition to uploaded files.

### 7. Cloud Deployment

Deploy the application on a cloud platform for public or private access.

### 8. Authentication

Add user authentication and role-based access control.

### 9. Evaluation Framework

Add automated evaluation metrics for:

- Code correctness
- Retrieval quality
- Recovery success rate
- Response accuracy
- Execution success rate

---

## 📌 Project Summary

The Autonomous Data Science Co-Pilot is an AI-powered data-analysis system that automates the complete workflow from dataset upload to final insights.

The key idea is:

    Natural Language
          ↓
    Planner Agent
          ↓
    LangChain + LLM
          ↓
    Python/Pandas Code
          ↓
    Execution
          ↓
    Success OR Failure
          ↓
    RAG + Recovery Agent
          ↓
    Corrected Code
          ↓
    Re-execution
          ↓
    Visualization + Insights
          ↓
    PDF Report

The combination of LLM-based code generation, LangChain, RAG, FAISS, Sentence Transformers, automatic execution, and recovery makes the system more autonomous than a traditional data-analysis application.

---

## 👩‍💻 Author

Apurva Dighe

MCA Student

---

## 📌 Project Type

Academic / Internship Project

Project Name:

Autonomous Data Science Co-Pilot