# 🤖 Agentic AI Pipeline using LangGraph

## 📌 Overview

This project demonstrates a simple Agentic AI Pipeline developed using **Python** and **LangGraph**. The system accepts user queries, identifies their intent, routes them to the appropriate tool, and returns the corresponding response.

The project demonstrates the fundamental concepts of agentic AI, including state management, conditional routing, and modular tool execution.

---

## 🚀 Features

- Stateful workflow using LangGraph
- Conditional query routing
- Calculator Tool
- Keyword Extraction Tool
- Greeting Tool
- Date & Time Tool
- Modular and reusable code structure
- Interactive command-line interface

---

## 📂 Project Structure

```
Agentic AI/
│── main.py
│── workflow.py
│── tools.py
│── requirements.txt
│── README.md
│── LICENSE
└── .gitignore
```

---

## ⚙️ Technologies Used

- Python
- LangGraph
- LangChain
- LangChain Core

---

## 🏗 Workflow

```
                User Query
                     │
                     ▼
             LangGraph Router
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Calculator     Keyword Tool   Greeting Tool
      │              │              │
      └──────────────┼──────────────┘
                     │
                     ▼
              Return Response
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/agentic-ai-pipeline.git
```

Navigate to the project folder:

```bash
cd agentic-ai-pipeline
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Agentic AI workflow
- Stateful graph execution
- Conditional routing
- Tool-based task execution
- Modular Python programming
- LangGraph fundamentals

---

## 🔮 Future Enhancements

- Integrate Google Gemini or OpenAI API
- Add web search capability
- Add conversation memory
- Support additional AI tools
- Build a web interface using Streamlit

---

## 👨‍💻 Author

**Apurva Dighe**

Master of Computer Applications (MCA) Student

---

## 📜 License

This project is licensed under the MIT License.