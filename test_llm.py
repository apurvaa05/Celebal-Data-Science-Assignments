from agents.planner import PlannerAgent

planner = PlannerAgent()

columns = [
    "Name",
    "Age",
    "Department",
    "Salary",
    "Experience"
]

question = "Show average salary by department"

result = planner.plan(question, columns)

print("\nGenerated Code:\n")
print(result)