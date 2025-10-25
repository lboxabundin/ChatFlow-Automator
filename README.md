# ChatFlow Automator

ChatFlow Automator is an open source lightweight chatbot + automation system. It allows you to define conversation triggers and automated responses using simple JSON rules.

## Features
- Simple chatbot system in Python
- Rule-based automation using JSON workflow files
- Extensible and open source
- No external API calls required
- Fully offline capable

## Usage

### Install dependencies
```
pip install -r requirements.txt
```

### Run chatbot
```
python chatbot.py
```

### Add your own rules
Modify `rules.json` to define chatbot triggers and automated responses.

## Example Rule
```json
{
  "hello": "Hello! How can I assist you today?",
  "bye": "Goodbye! Have a nice day!"
}
```

## License
MIT
