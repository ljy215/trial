import os
from dotenv import load_dotenv
from llm_agent import get_llm_response
from email_agent import send_email, send_email_google

load_dotenv()

print("\n👋 欢迎使用聊天机器人！输入 'send email' 或 '发送邮件' 来发送邮件，输入 'exit' 结束对话\n")


def main():
    print("\n👋 欢迎使用智能邮件助手！输入 'send email' 发送邮件，输入 'exit' 退出\n")

    while True:
        user_input = input("你: ").strip()

        if user_input.lower() in ["exit", "退出"]:
            print("再见！")
            break

        elif user_input.lower() in ["send email", "发送邮件"]:
            # 获取发送信息
            provider = input("选择服务商 (resend/google): ").lower()
            to_email = input("收件人邮箱: ").strip()
            subject = input("邮件主题: ").strip()
            user_content = input("邮件内容: ").strip()

            # 生成AI回复
            print("\n🤖 正在生成AI回复...")
            ai_content = get_llm_response(user_content)

            if not ai_content:
                print("❌ AI回复生成失败，取消发送")
                continue

            # 发送邮件
            if provider == "google":
                result = send_email_google(to_email, subject, ai_content)
            else:
                result = send_email(to_email, subject, ai_content)

            # 处理结果
            if result:
                print(f"\n✅ 邮件发送成功！已发送内容：\n{ai_content}\n")
            else:
                print("\n❌ 邮件发送失败\n")

        else:
            # 普通对话模式
            response = get_llm_response(user_input)
            print(f"\n🤖 机器人: {response}\n")


if __name__ == "__main__":
    main()