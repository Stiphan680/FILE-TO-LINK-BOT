# 🚀 File to Link Bot

A powerful Telegram bot that generates direct download and streaming links for any file.

## 🌟 Key Features

### 📥 File to Link Generation
- Generates **High-Speed Direct Download Links**
- Provides **Streaming Links** for video files
- Supports **all file types** (Video, Audio, Document, etc.)

### 📺 Advanced Web Player
- **In-Browser Streaming**: Watch videos directly without downloading
- **External Player Support**: One-click integration with **MX Player**, **VLC**, and **PlayIt**
- **Responsive Design**: Beautiful UI compatible with Mobile & Desktop

### ⚡ Batch Processing
- **Batch Link Creation**: Convert multiple files into a single batch link
- **Post Protection**: Option to protect batch content from forwarding

### 🔐 Security Features
- **Force Subscribe**: Require users to join your channel before using the bot (Optional)
- **Content Protection**: Prevent file forwarding (Optional)

### 🛠️ Admin Controls
- **Broadcast**: Send messages to all bot users
- **User Management**: View real-time statistics
- **Database**: Robust MongoDB integration

---

## 🤖 Bot Commands

### **Public Commands**
- `/start` - Start the bot and get instructions
- `/help` - View help menu
- `/about` - View bot information
- `/files` - List your uploaded files
- `/del_files` - Manage and delete your files

### **Admin Commands**
- `/broadcast` - Broadcast a message to all users
- `/stats` - View bot statistics
- `/batch` - Create a batch link for multiple files

---

## 📋 Environment Variables

To run this bot, set up the following environment variables:

### Required:
- `API_ID`: Get from **my.telegram.org**
- `API_HASH`: Get from **my.telegram.org**
- `BOT_TOKEN`: Get from **@BotFather**
- `OWNER_ID`: Your Telegram User ID (as ADMINS)
- `DATABASE_URI`: **MongoDB** connection string
- `LOG_CHANNEL`: Channel ID for logs (start with -100)
- `BIN_CHANNEL`: Channel ID for file storage

### Optional:
- `FSUB`: Enable Force Subscribe (True/False) - Default: False
- `PROTECT_CONTENT`: Protect content from forwarding (True/False) - Default: False
- `DATABASE_NAME`: Database name - Default: filetolinkbot
- `CHANNEL`: Your channel link
- `SUPPORT`: Your support channel/group link

---

## 🚀 Deployment

### Deploy on Render

1. Fork this repository
2. Go to [Render.com](https://render.com)
3. Create a new Web Service
4. Connect your forked repository
5. Select **Docker** as environment
6. Add environment variables
7. Deploy!

### Deploy on Railway

1. Fork this repository
2. Go to [Railway.app](https://railway.app)
3. Create new project from GitHub
4. Add environment variables
5. Deploy!

---

## 📝 Credits

Based on the original codebase by [Botsthe](https://github.com/Botsthe/FILE-TO-LINK-BOT)

---

## ⚖️ License

This project is for educational purposes only.
