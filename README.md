# 🤖 Python Blog Generator

An AI-powered blog content generator using OpenAI API through OpenRouter. Create engaging blog posts with multiple interface options - command line, desktop GUI, or web interface.

## ✨ Features

- **Multiple Interfaces**: Choose between command line, desktop GUI (tkinter), or web interface (Streamlit)
- **AI-Powered**: Uses OpenAI models via OpenRouter for high-quality content generation
- **UTF-8 Support**: Full support for international characters and emojis
- **User-Friendly**: Simple and intuitive interfaces for all skill levels
- **Flexible**: Import the generator function into your own projects

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- OpenRouter API key (get one at [openrouter.ai](https://openrouter.ai))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ovezthaking/Python-Blog-Generator.git
cd Python-Blog-Generator
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openrouter_api_key_here
```

## 🎯 Usage Options

### 1. Command Line Interface
```bash
python blog_generator.py
```
Interactive command-line interface for quick blog generation.

### 2. Desktop GUI Application
```bash
python blog_gui.py
```
Modern desktop application with:
- Text input field for topics
- Results display area
- Copy to clipboard functionality
- Save to file option
- Progress indicators

### 3. Web Interface
```bash
streamlit run blog_gen_web.py
```
Beautiful web interface accessible at `http://localhost:8501` with:
- Real-time preview
- Modern UI design
- Mobile-friendly layout
- Easy sharing capabilities

### 4. Python Module
```python
from blog_generator import generate_blog

# Generate content
result = generate_blog("Your topic here")
print(result)
```

## 📁 Project Structure

```
Python-Blog-Generator/
├── blog_generator.py      # Core generator function and CLI
├── blog_gui.py           # Desktop GUI application
├── blog_gen_web.py       # Streamlit web interface
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
├── LICENSE             # Project license
└── README.md           # This file
```

## ⚙️ Configuration

The application uses OpenRouter to access OpenAI models. Configure your API key in the `.env` file:

```env
OPENAI_API_KEY=your_openrouter_api_key_here
```

### Supported Models
- `openai/gpt-oss-20b:free` (default - free tier)
- Other OpenAI models available through OpenRouter

## 🛠️ Development

### Adding New Features
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Structure
- `generate_blog()` - Core function for content generation
- GUI applications import and use the core function
- UTF-8 encoding ensures international character support

## 📋 Requirements

- `python-dotenv>=1.0.0` - Environment variable management
- `openai>=1.0.0` - OpenAI API client
- `streamlit>=1.48.0` - Web interface framework
- `tkinter` - Desktop GUI (included with Python)

## 🐛 Troubleshooting

### Common Issues

**API Key Errors (401)**
- Verify your OpenRouter API key in `.env`
- Check if the key has sufficient permissions

**Quota Exceeded (429)**
- Check your OpenRouter account balance
- Verify monthly spending limits
- Consider upgrading your plan

**GUI Not Working (Linux)**
```bash
sudo apt install python3-tk
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenRouter](https://openrouter.ai) for providing access to OpenAI models
- [Streamlit](https://streamlit.io) for the amazing web framework
- [OpenAI](https://openai.com) for the powerful language models

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Search existing GitHub issues
3. Create a new issue with detailed information

---


