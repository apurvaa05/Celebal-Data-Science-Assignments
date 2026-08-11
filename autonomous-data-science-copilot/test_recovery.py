from agents.recovery import RecoveryAgent

agent = RecoveryAgent()

bad_code = """
df.groupby("salary").mean()
"""

error = """
KeyError: 'salary'
"""

columns = [
    "Name",
    "Age",
    "Department",
    "Salary",
    "Experience"
]

fixed = agent.recover(
    bad_code,
    error,
    columns
)

print(fixed)