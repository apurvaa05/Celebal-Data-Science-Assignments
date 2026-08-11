import pandas as pd
import plotly.express as px


class VisualizationService:

    def create_chart(self, result, chart_type="bar"):

        if result is None:
            return None

        if isinstance(result, pd.Series):

            df = result.reset_index()

        elif isinstance(result, pd.DataFrame):

            df = result

        else:

            return None

        if len(df.columns) < 2:
            return None

        x = df.columns[0]
        y = df.columns[1]

        if chart_type == "line":

            return px.line(df, x=x, y=y)

        elif chart_type == "pie":

            return px.pie(df, names=x, values=y)

        elif chart_type == "scatter":

            return px.scatter(df, x=x, y=y)

        elif chart_type == "histogram":

            return px.histogram(df, x=x)

        elif chart_type == "box":

            return px.box(df, y=y)

        return px.bar(df, x=x, y=y)