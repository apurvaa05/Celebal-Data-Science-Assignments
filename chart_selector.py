class ChartSelector:

    def select(self, question: str):

        question = question.lower()

        if "line" in question:
            return "line"

        elif "pie" in question:
            return "pie"

        elif "scatter" in question:
            return "scatter"

        elif "histogram" in question:
            return "histogram"

        elif "box" in question:
            return "box"

        return "bar"