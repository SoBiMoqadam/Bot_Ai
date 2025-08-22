<h1 align="center">🤖 BOT_AI – Telegram AI Chatbot</h1>
<p align="center">
A smart and open-source Telegram bot built with Python that answers questions, chats naturally, and runs 24/7 on server or Docker.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Telegram%20Bot-AI-%239b30ff?style=flat-square&logo=telegram&logoColor=white" alt="Telegram Badge" />
  <img src="https://img.shields.io/badge/Made%20with-Python-%239b30ff?style=flat-square&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Docker-Supported-%239b30ff?style=flat-square&logo=docker&logoColor=white" alt="Docker Badge" />
  <img src="https://img.shields.io/badge/Open%20Source-Yes-%239b30ff?style=flat-square&logo=github&logoColor=white" alt="Open Source Badge" />
</p>

<p align="center">
  <a href="https://t.me/Translatedbyvoisebot" target="_blank" style="display:inline-block; padding:12px 24px; font-size:16px; color:white; background-color:#9b30ff; border-radius:6px; text-decoration:none;">Start chatting with BOT_AI</a>
</p>
<p align="center"><strong>Username:</strong> <code>@Translatedbyvoisebot</code></p>


<hr/>

<h2> About </h2>
<p>
<strong>BOT_AI</strong> is an advanced <strong>Telegram AI chatbot</strong> built with Python.<br/>
It can answer any kind of question, chat naturally with users, and is designed to run <strong>24/7</strong> on servers or inside Docker containers.<br/>
Fully open-source and customizable.
</p>

<hr/>

<h2> Features </h2>
<ul>
  <li>Natural AI-powered conversation</li>
  <li>Answers to questions (science, general knowledge, fun, etc.)</li>
  <li>Easy to customize and extend</li>
  <li>Docker support for deployment</li>
  <li>Runs continuously on servers</li>
</ul>

<hr/>

<h2> Project Structure </h2>
<pre><code>BOT_AI/
├── main.py
├── requirements.txt
├── Dockerfile
└── .env
</code></pre>

<hr/>

<h2> Installation & Setup </h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/SoBiMoqadam/BOT_AI.git
cd BOT_AI
</code></pre>

<h3>2. Install Python packages</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Create virtual environment (optional)</h3>
<pre><code>python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
</code></pre>

<h3>4. Configure environment</h3>
<pre><code>TELEGRAM_TOKEN=your_api_token_here
</code></pre>

<hr/>

<h2> Running the Bot </h2>

<h3>Run locally</h3>
<pre><code>python bot.py
</code></pre>

<h3>Run with Docker</h3>
<pre><code>docker build -t bot_ai .
docker run -d --name bot_ai --env-file .env bot_ai
</code></pre>

<p><strong>⚠️ Do not upload .env file to GitHub.</strong></p>

<hr/>

<h2> Custom Commands </h2>
<p>Example of adding a custom command:</p>
<pre><code class="language-python">
from telegram.ext import CommandHandler

def hello(update, context):
    update.message.reply_text("Hello, I'm your AI bot!")

dispatcher.add_handler(CommandHandler("hello", hello))
</code></pre>

<p>Type <code>/hello</code> in your bot chat to test it. You can create additional commands and integrate APIs.</p>

<hr/>

<h2> Usage Examples </h2>
<ul>
  <li><code>/start</code> → Start the bot</li>
  <li>“Tell me a motivational quote” → Bot replies with a quote</li>
  <li>“Explain machine learning” → Bot explains the concept</li>
  <li>“Tell me a joke” → Bot replies with a joke</li>
</ul>

<hr/>

<h2> Contributing </h2>
<ol>
  <li>Fork the repo</li>
  <li>Create a feature branch</li>
  <li>Submit a Pull Request</li>
</ol>

<hr/>

<h2> License </h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>
