from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class ReportService:

    def generate(
        self,
        filename,
        question,
        code,
        result,
        insights
    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Autonomous Data Science Co-Pilot</b>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Question:</b> {question}",
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                "<b>Generated Pandas Code</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"<pre>{code}</pre>",
                styles["Code"] if "Code" in styles else styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                "<b>Analysis Result</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                str(result),
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph(
                "<b>AI Insights</b>",
                styles["Heading2"]
            )
        )

        for item in insights:
            story.append(
                Paragraph(
                    "• " + item,
                    styles["BodyText"]
                )
            )

        doc.build(story)