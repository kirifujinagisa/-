from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类

# 注册插件
@register(name="BanUser", description="Ban a user in group chat", version="0.1", author="RockChinQ")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        sender_id = ctx.event.sender_id
        if msg.startswith("ban") and sender_id == "2160899714":  # 如果消息以"ban"开头并且发起者是管理员

            # 解析命令，提取要禁言的群号和目标用户QQ号
            _, group_id, target_user_id, duration = msg.split(" ")
            group_id = int(group_id)
            target_user_id = int(target_user_id)
            duration = int(duration)

            # 禁言目标用户
            await self.ban_user(group_id, target_user_id, duration)

    # 异步禁言用户
    async def ban_user(self, group_id, user_id, duration):
        # 这里填写禁言用户的代码，可以根据你的机器人所使用的接口进行调用
        pass

    # 插件卸载时触发
    def __del__(self):
        pass
