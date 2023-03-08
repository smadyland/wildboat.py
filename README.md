# wildboat Discord Bot

WildBoat is a Discord bot written in Discord.py that uses several animal API's to send images of animals. The bot supports slash commands to make it easy for users to interact with the bot.

## Features

- Sends images of animals using API's
- Supports several animal categories like dogs, cats, foxes, etc.
- Slash command support

## Commands (overhaul soon)

- `/dog` - sends a random image of a dog
- `/cat` - sends a random image of a cat
- `/cat {breed specific}` - sends a random image of a cat breed of your choice
- `/dog {breed specific}` - sends a random image of a dog breed of your choice

## APIs Used

- [Dog API](https://dog.ceo/dog-api/)
- [TheCatAPI](https://thecatapi.com/)

## Installation and Usage

1. Clone the repository.
2. Install the required dependencies
3. Create a new bot on the [Discord Developer Portal](https://discord.com/developers/applications).
4. Add the bot to your server and copy the bot token.
5. Add your bot token to the "client.run" function
6. Run `python wildboat.py` or double click on `wildboat.py` to start the bot.

## Contributing

Contributions are always welcome! If you want to contribute to this project, please fork this repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
