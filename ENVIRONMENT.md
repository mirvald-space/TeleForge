# Environment Setup

This document explains how to set up the environment variables for the Telegram Bot Starter.

## Required Environment Variables

Create a `.env` file in the project root with the following variables:

```
# Bot settings
BOT_TOKEN=your_bot_token_from_botfather
BOT_NAME=YourBotName

# MongoDB settings
MONGODB_URI=mongodb://localhost:27017/tg_bot

# Admin settings - can be a single ID or a comma-separated list
ADMIN_IDS=123456789
# OR for multiple admins:
# ADMIN_IDS=123456789,987654321

# Localization
DEFAULT_LANGUAGE=en
```

## Variable Details

### Bot Settings

- `BOT_TOKEN`: The token provided by BotFather when creating a new bot
  - Example: `123456789:ABCdefGHIJKlmnoPQRSTUvwxyz`
- `BOT_NAME`: A friendly name for your bot (used in logs and some messages)

### MongoDB Settings

- `MONGODB_URI`: The connection string for MongoDB
  - Local example: `mongodb://localhost:27017/tg_bot`
  - Atlas example: `mongodb+srv://user:password@cluster.mongodb.net/tg_bot`
  
  **Important Notes on MongoDB URI:**
  - Make sure the database name (e.g., `tg_bot`) is properly separated in the URI path
  - If using connection parameters, add them after the database name with a question mark: 
    `mongodb://localhost:27017/tg_bot?retryWrites=true`
  - Do NOT include write concern in the database name part of the URI

### Admin Settings

- `ADMIN_IDS`: User ID(s) of the bot administrator(s)
  - Single admin: `123456789`
  - Multiple admins: `123456789,987654321`
  - How to find your user ID: Send a message to @userinfobot

### Localization

- `DEFAULT_LANGUAGE`: Default language code for the bot
  - Options: `en` (English), `ru` (Russian)
  - Add more languages by following the instructions in the README.md

## Getting Started

1. Copy the template from this document
2. Create a new file named `.env` in the project root
3. Replace the placeholder values with your actual configuration
4. The bot will automatically load these settings on startup 