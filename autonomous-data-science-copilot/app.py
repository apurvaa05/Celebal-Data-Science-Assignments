import streamlit as st
import time

from utils.loader import load_data

from agents.planner import PlannerAgent
from agents.executor import ExecutionEngine
from agents.recovery import RecoveryAgent

from services.visualization_service import VisualizationService
from services.chart_selector import ChartSelector
from services.insight_service import InsightService
from services.report_service import ReportService
# -------------------- PAGE CONFIG -------------------- #

st.set_page_config(
    page_title="Autonomous Data Science Co-Pilot",
    page_icon="📊",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

section[data-testid="stSidebar"]{
    background:#1E293B;
}

section[data-testid="stSidebar"] *{
    color:white;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:48px;
    font-weight:bold;
    font-size:16px;
}

.stDownloadButton>button{
    width:100%;
    border-radius:12px;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,.08);
}

div.stDataFrame{
    border-radius:15px;
    overflow:hidden;
}

h1,h2,h3{
    color:#0F172A;
}

</style>
""", unsafe_allow_html=True)

# -------------------- AGENTS -------------------- #

planner = PlannerAgent()
executor = ExecutionEngine()
recovery = RecoveryAgent()

visualizer = VisualizationService()
selector = ChartSelector()
insight_engine = InsightService()
report_service = ReportService()

# -------------------- SIDEBAR -------------------- #

st.sidebar.title("📊 Autonomous Data Science Co-Pilot")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📂 Dataset",
        "🤖 Analysis"
    ]
)


# -------------------- TITLE -------------------- #

st.markdown("""
# 📊 Autonomous Data Science Co-Pilot

### AI-Powered Dataset Analysis using Natural Language
""")
st.caption("AI-Powered Data Analysis using Natural Language")


# -------------------- FILE UPLOAD -------------------- #

with st.container():

    st.subheader("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "",
        type=["csv","xlsx","json"]
    )


if uploaded_file is not None:

    df = load_data(uploaded_file)

    st.success(
        f"✅ **{uploaded_file.name}** uploaded successfully!"
    )


    # ====================================================
    # HOME
    # ====================================================

    if page == "🏠 Home":

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        st.divider()

        c1, c2, c3 = st.columns(3)

        c1.metric("Rows", df.shape[0])
        c2.metric("Columns", df.shape[1])
        c3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.divider()

        st.subheader("📋 Dataset Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**File Name:** {uploaded_file.name}")
            st.write(f"**Rows:** {df.shape[0]}")
            st.write(f"**Columns:** {df.shape[1]}")

        with col2:
            numeric_cols = len(df.select_dtypes(include="number").columns)
            categorical_cols = len(df.select_dtypes(exclude="number").columns)

            st.write(f"**Numeric Columns:** {numeric_cols}")
            st.write(f"**Categorical Columns:** {categorical_cols}")
            st.write(f"**Missing Values:** {int(df.isnull().sum().sum())}")

    # ====================================================
    # DATASET
    # ====================================================

    elif page == "📂 Dataset":

        st.subheader("Complete Dataset")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Column Names")

            st.write(list(df.columns))

        with col2:

            st.subheader("Data Types")

            st.write(df.dtypes)

        st.divider()

        st.subheader("Statistical Summary")

        st.dataframe(
            df.describe(include="all"),
            use_container_width=True
        )


    # ====================================================
    # ANALYSIS
    # ====================================================

    elif page == "🤖 Analysis":

        st.subheader("Ask AI About Your Dataset")

        st.markdown("""
        ### 💡 Try asking

        - Show summary statistics
        - Show missing values
        - Show distribution of a numeric column
        - Show count by category
        - Show average of a numeric column by category
        - Show correlation between numeric columns
        """)

        question = st.text_input(
          "Enter your question",
         placeholder="Example: Show average salary by department as a pie chart"
        )

        analyze = st.button(
            "🚀 Analyze Dataset",
            use_container_width=True
        )

        if analyze:

            if not question.strip():

                st.warning("Please enter a question.")

                st.stop()

            # ------------------------------------
            start_time = time.time()
            with st.spinner("🤖 Planner Agent is generating code..."):

                code = planner.plan(
                    question,
                    list(df.columns)
                )

            st.subheader("Generated Pandas Code")

            st.code(
                code,
                language="python"
            )

            # ------------------------------------
            # Execute Generated Code
            # ------------------------------------

            result = executor.execute(code, df)

            # ------------------------------------
            # Recovery Agent
            # ------------------------------------

            if not result["success"]:

                st.warning("⚠️ Initial execution failed.")

                st.info("🤖 Recovery Agent is fixing the code...")

                fixed_code = recovery.recover(
                    code,
                    result["error"],
                    df.columns
                )

                st.subheader("Recovered Code")

                st.code(
                    fixed_code,
                    language="python"
                )

                result = executor.execute(
                    fixed_code,
                    df
                )

            # ------------------------------------
            # Display Result
            # ------------------------------------

            if result["success"]:

                output = result["result"]

                st.subheader("Analysis Result")

                if output is None:

                    st.success("Code executed successfully.")

                else:

                    if hasattr(output, "to_frame"):

                        st.dataframe(
                            output.to_frame(),
                            use_container_width=True
                        )

                    elif hasattr(output, "columns"):

                        st.dataframe(
                            output,
                            use_container_width=True
                        )

                    else:

                        st.write(output)

                    # --------------------------------
                    # Visualization
                    # --------------------------------

                    chart_type = selector.select(question)

                    chart = visualizer.create_chart(
                        output,
                        chart_type
                    )

                    if chart is not None:

                        st.subheader("📊 Visualization")

                        st.plotly_chart(
                            chart,
                            use_container_width=True
                        )

                    # --------------------------------
                    # Insights
                    # --------------------------------

                    insights = insight_engine.generate(output)

                    if insights:

                        st.subheader("💡 AI Insights")

                        for insight in insights:

                            st.success(insight)

                    

                        report_service.generate(
                                "generated/analysis_report.pdf",
                                question,
                                code,
                                output,
                                insights
                            )

                        with open("generated/analysis_report.pdf", "rb") as pdf_file:

                                st.download_button(
                                    label="📥 Download Analysis Report",
                                    data=pdf_file,
                                    file_name="analysis_report.pdf",
                                    mime="application/pdf"
                                )

                                end_time = time.time()
                                st.success(f"Analysis completed in {end_time - start_time:.2f} seconds.")

            else:

                st.error("❌ Recovery Agent could not fix the error.")

                st.code(result["error"])


else:

    st.info("📂 Upload a CSV, Excel or JSON dataset to begin.")

st.divider()

st.caption(
    "Built with ❤️ using Streamlit • Pandas • Plotly • OpenRouter • ReportLab"
)