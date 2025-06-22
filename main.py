import amino
import google.generativeai as genai

genai.configure(api_key="AIzaSyDHWbg7HlUszeETT8GBcPg19_c5qwVeAqs")
model = genai.GenerativeModel("gemini-pro")

client = amino.Client()
client.login(
    email="xpouxzedrtxzed@gmail.com",
    password="drtgzed21"
)

print("✅ بوت زاو فان يعمل الآن...")

@client.event("on_message")
def on_message(ctx):
    if isinstance(ctx.message.content, str) and ctx.message.content.startswith("!ai"):
        prompt = ctx.message.content[4:]
        if not prompt:
            ctx.reply("أرسل شيئًا بعد !ai لكي يتفاعل زاو فان.")
            return
        try:
            response = model.generate_content(prompt)
            if response and response.text:
                ctx.reply(response.text)
            else:
                ctx.reply("زاو فان لم يفهم الطلب.")
        except Exception as e:
            ctx.reply(f"⚠️ زاو فان واجه خطأ: {e}")

client.run()
