# ZEN QUOTE REST API

A simple REST API built with Flask.  
It can return random quotes, get quotes by ID, and add new quotes to a local JSON file.

## Features
- `GET /` → Home page
- `GET /quotes/` → Get a random quote (from external API)
- `GET /quotes/<id>/` → Get a quote by ID (from local JSON file)
- `POST /quotes/` → Add a new quote (saved in local JSON file)

## Requirements
- Python 3.10+
- Flask

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ZEN-QUOTE-REST-API.git
   cd ZEN-QUOTE-REST-API
