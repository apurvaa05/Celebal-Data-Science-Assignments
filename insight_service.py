import pandas as pd


class InsightService:

    def generate(self, result):

        insights = []

        if result is None:
            return insights

        if isinstance(result, pd.Series):

            highest = result.idxmax()
            lowest = result.idxmin()

            insights.append(
                f"Highest value: {highest} ({result.max():,.2f})"
            )

            insights.append(
                f"Lowest value: {lowest} ({result.min():,.2f})"
            )

            insights.append(
                f"Difference: {(result.max()-result.min()):,.2f}"
            )

        elif isinstance(result, pd.DataFrame):

            insights.append(
                f"Returned {len(result)} records."
            )

            insights.append(
                f"Columns: {', '.join(result.columns)}"
            )

        return insights