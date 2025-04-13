from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message
from mattermostautodriver import Driver


driver = Driver(
    {
        "url": "mattermost.edtools.top",
        "token": "qftj3tshbfyxp8j14mzf8xybwh",
        "port": 443,
    }
)

driver.login()


class MyPlugin(Plugin):
    @listen_to("wake up")
    async def wake_up(self, message: Message):
        self.driver.reply_to(message, "I'm awake!", ephemeral=True)

    @listen_to("clear (.*)")
    async def broom_all(self, message, something):
        # posts_num = len(driver.posts.get_posts_for_channel(message.channel_id)["posts"])
        # print(driver.posts.get_posts_for_channel(message.channel_id))
        # driver.commands.execute_command(
        #     {"channel_id": message.channel_id, "command": f"/broom last {posts_num}"}
        # )
        for post in driver.posts.get_posts_for_channel(message.channel_id)["order"]:
            driver.posts.delete_post(post)
        self.driver.reply_to(message, "Here is %s" % something, ephemeral=True)
