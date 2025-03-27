# AI Web Scraper

A Python-based web automation tool that uses AI agents to browse and interact with websites using the browser-use library.

## Overview

This project utilizes the browser-use library and Claude AI models to create an agent capable of automating web browsing tasks. The agent can navigate websites, interact with web elements, and extract structured data based on defined tasks.

## Features

- AI-powered web browsing automation
- Chrome browser integration
- Task-based interaction with websites
- Structured data extraction
- Support for vision-enabled models

## Requirements

- Python 3.11+
- Chrome browser
- Anthropic API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AiWebScrapper.git
   cd AiWebScrapper
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   playwright install
   ```

3. Set up environment variables:
   Create a `.env` file in the project root with:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

The `main.py` file configures and runs the browser-use agent:

```python
async def main():
    initial_actions = [
        {'open_tab': {'url': 'https://your-target-website.com'}}
    ]
    
    agent = Agent(
        task="Your task description here",
        llm=llm,
        use_vision=True,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions
    )
    result = await agent.run()
    print(result.final_result())
    await browser.close()
```

Run the script:
```
python main.py
```

## Project Structure

- `main.py`: Entry point containing configuration and execution logic
- The browser-use library provides the Agent, Browser, and Controller classes

## Output Models

The project uses Pydantic models to structure data:

```python
class Post(BaseModel):
    title: str
    url: str
    
class Posts(BaseModel):
    posts: List[Post]
```

## Example

The included example connects to a Google Doc and performs a specific task:
- Opens a Google Document
- Writes a thank you letter
- Saves the document as PDF

## Resources

- [browser-use Documentation](https://docs.browser-use.com/)

## License

[Your license information here]

## Acknowledgements

- [browser-use](https://docs.browser-use.com/)
- [Anthropic](https://www.anthropic.com/)
