from mmpy_bot import Bot, Settings
from my_plugin import MyPlugin


bot = Bot(
    settings=Settings(
        MATTERMOST_URL="https://mattermost.edtools.top",
        MATTERMOST_PORT=443,
        BOT_TOKEN="jijmaa55aj8suqxot9dx5ks94e",
        BOT_TEAM="aigc-in-education",
    ),  # Either specify your settings here or as environment variables.
    plugins=[MyPlugin()],  # Add your own plugins here.
)
bot.run()
