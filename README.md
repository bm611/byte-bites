# Byte Bites - AI Recipe Generator

Byte Bites is a web application built with Reflex that generates recipes using AI. It features recipe scaling, ingredient conversion, and an intuitive user interface.

## Features
- AI-powered recipe generation
- Dynamic serving size adjustment
- Interactive recipe display
- Responsive design
- Modern UI with animations

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd byte-bites
```

2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install reflex
pip install -r requirements.txt
```

4. Environment Setup

Create a `.env` file in the root directory with your API keys:
```
TOGETHER_API_KEY=your_together_api_key_here
GEMINI_API_KEY=your_google_api_key_here
```

## Running the Application

1. Start the development server
```bash
reflex run
```

2. Open your browser and navigate to:
```
http://localhost:3000
```

## Development

To work on the application:
- Frontend components are in `byte-bites/app/sections/`
- Main app configuration is in `byte-bites/app/app.py`
- State management is handled in `byte-bites/app/sections/state.py`

## Project Structure
```
byte-bites/
├── app/
│   ├── sections/
│   │   ├── hero.py
│   │   ├── input.py
│   │   ├── nav.py
│   │   ├── recipe.py
│   │   └── state.py
│   └── app.py
├── assets/
├── requirements.txt
└── .env
```

## Libraries Used
- Reflex - Web framework
- Gemini - AI recipe generation
- Flux.1 schnell - Recipe image generation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
