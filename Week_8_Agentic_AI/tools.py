from datetime import datetime

def calculator_tool(query):
    expression = query.replace("calculate", "").strip()

    try:
        result = eval(expression)
        return f"Result: {result}"

    except Exception:
        return "Invalid mathematical expression."


def keyword_tool(query):
    text = query.replace("keyword", "").strip()

    words = text.split()

    keywords = [word.strip(".,!?") for word in words if len(word) > 5]

    if len(keywords) == 0:
        return "No important keywords found."

    return "Keywords: " + ", ".join(keywords)


def greeting_tool(query):

    greetings = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good evening"
    ]

    if any(word in query.lower() for word in greetings):

        return "Hello! 👋 How can I assist you today?"

    return "I'm here to help you."


def datetime_tool():

    now = datetime.now()

    return now.strftime("Current Date & Time : %d-%m-%Y %I:%M:%S %p")