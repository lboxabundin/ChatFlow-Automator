import json

def load_rules(file_path="rules.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def chatbot():
    rules = load_rules()
    print("ChatFlow Automator is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        response = rules.get(user_input, "I don't understand that, but I'm learning!")
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
