<h1>🤖 BOT_AI – Telegram AI Chatbot</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Telegram%20Bot-AI-blue?style=flat-square&logo=telegram" alt="Telegram Badge" />
  <img src="https://img.shields.io/badge/Made%20with-Python-green?style=flat-square&logo=python" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Docker-Supported-blue?style=flat-square&logo=docker" alt="Docker Badge" />
  <img src="https://img.shields.io/badge/Open%20Source-Yes-orange?style=flat-square&logo=github" alt="Open Source Badge" />
</p>

<p align="center">
👉 <a href="https://t.me/Translatedbyvoisebot" target="_blank">Start chatting with BOT_AI</a>
</p>

<hr/>

<h2>🚀 About</h2>
<p>
<strong>BOT_AI</strong> is an advanced <strong>Telegram AI chatbot</strong> built with Python.<br/>
It can answer any kind of question, chat naturally with users, and is designed to run <strong>24/7</strong> on servers or inside Docker containers.<br/>
The project is fully <strong>open-source</strong> and customizable for your needs.
</p>

<hr/>

<h2>✨ Features</h2>
<ul>
  <li>💬 Natural AI-powered conversation</li>
  <li>❓ Answers to questions (science, general knowledge, fun, etc.)</li>
  <li>🛠 Easy to customize and extend</li>
  <li>🐳 Docker support for deployment</li>
  <li>📌 Runs continuously on servers</li>
</ul>

<hr/>

<h2>📂 Project Structure</h2>
<pre><code>BOT_AI/
├── bot.py             # Main script
├── requirements.txt   # Dependencies
├── Dockerfile         # Docker configuration
└── .env               # Environment variables (not included in repo)
</code></pre>

<hr/>

<h2>🛠️ Installation & Setup</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/YourUsername/BOT_AI.git
cd BOT_AI
</code></pre>

<h3>2. Install Python packages</h3>
<p>Make sure you have <strong>Python 3.9+</strong> installed. Then install dependencies:</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Create virtual environment (optional but recommended)</h3>
<pre><code>python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
</code></pre>

<h3>4. Configure environment</h3>
<p>Create a file named <code>.env</code> in the root directory and add your Telegram bot token:</p>
<pre><code>TELEGRAM_TOKEN=your_api_token_here
</code></pre>

<hr/>

<h2>▶️ Running the Bot</h2>

<h3>Run locally</h3>
<pre><code>python bot.py
</code></pre>

<h3>Run with Docker</h3>
<pre><code># Build Docker image
docker build -t bot_ai .

# Run container
docker run -d --name bot_ai --env-file .env bot_ai
</code></pre>

<p><strong>⚠️ Important:</strong> Do not upload <code>.env</code> file to GitHub.</p>

<hr/>

<h2>🛠️ Custom Commands</h2>
<p>You can easily extend BOT_AI with your own commands. Example:</p>

<pre><code class="language-python">
from telegram.ext import CommandHandler

def hello(update, context):
    update.message.reply_text("👋 Hello, I'm your AI bot!")

dispatcher.add_handler(CommandHandler("hello", hello))
</code></pre>

<p>
Now type <code>/hello</code> in your bot chat and it will respond! 🎉<br/>
You can create any custom commands (like <code>/news</code>, <code>/weather</code>, etc.) and integrate APIs.
</p>

<hr/>

<h2>💡 Usage Examples</h2>
<ul>
  <li><code>/start</code> → Start the bot</li>
  <li>“Tell me a motivational quote” → Bot replies with an inspiring quote</li>
  <li>“Explain machine learning” → Bot explains the concept</li>
  <li>“Tell me a joke” → Bot replies with a random joke</li>
</ul>

<hr/>

<h2>🎯 Live Demo</h2>
<p>Try BOT_AI on Telegram right now 👇</p>
<p>👉 <a href="https://t.me/Translatedbyvoisebot" target="_blank">Start chatting with BOT_AI</a></p>

<hr/>

<h2>🤝 Contributing</h2>
<ol>
  <li>Fork the repo 🍴</li>
  <li>Create a feature branch 🔧</li>
  <li>Submit a Pull Request 🚀</li>
</ol>

<hr/>

<h2>📜 License</h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>
