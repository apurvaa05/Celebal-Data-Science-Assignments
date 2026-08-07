from workflow import build_graph

def main():
    graph = build_graph()

    print("=" * 60)
    print("🤖 Agentic AI Pipeline using LangGraph")
    print("=" * 60)
    print("Available commands:")
    print("- calculate 25*10")
    print("- keyword Artificial Intelligence is transforming education")
    print("- hello")
    print("- exit\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        response = graph.invoke({"query": query})

        print("\nAgent:", response["result"])
        print("-" * 60)

if __name__ == "__main__":
    main()