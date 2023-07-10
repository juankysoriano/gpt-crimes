# GPT-Crime-Solver Telegram Bot

Welcome to the GPT-Crime-Solver project! This is an experimental Telegram bot designed to provide an immersive conversational adventure game experience. Powered by the advanced GPT (Generative Pretrained Transformer) technology, it presents interactive storytelling, conversational gameplay, and engaging crime-solving elements.

The bot narrates a crime story that is influenced by the choices and interactions of the player. It uses natural language processing to understand and respond to player inputs, creating a dynamic text-based gaming experience. While primarily a game, it can also be seen as a tool to enhance problem-solving, critical thinking, and language skills.

## Disclaimer

Please note that this is experimental code, not intended for production use. Many parts of the code have been generated with GPT, and while it's functional for its intended use case, it is not necessarily optimized or robust against all possible inputs or conditions.

## License

This project is licensed under the terms of the MIT license.

## Getting Started

1. First, you need to create a Telegram bot. If you're not sure how to do this, you can find instructions [here](https://core.telegram.org/bots#creating-a-new-bot).

2. Once you have created your bot, update your `.env` file with your Telegram bot token and your OpenAI API key. Your `.env` should look like this:

```
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
OPENAI_API_KEY=your-openai-api-key
```

If you don't have an `.env` file, you can use the provided `env_template` as a base. Just copy it to `.env` and fill in your credentials.

3. After setting up your `.env` file, you're ready to run the bot! Just use the following command in your terminal:

```bash
python main.py
```

And that's it! Enjoy interacting with your new Telegram bot!
