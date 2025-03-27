import asyncio
from langchain_anthropic import ChatAnthropic
from browser_use import Agent, Browser, BrowserConfig, Controller
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
load_dotenv()


class Post(BaseModel):
    title: str
    url: str
    
    
class Posts(BaseModel):
    posts: List[Post]
    

controller = Controller(output_model=Posts)

llm = ChatAnthropic(
    model_name="claude-3-5-sonnet-20240620",
    temperature=0.0,
    timeout=100,  # Increase for complex tasks
)

browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    )
)


async def main():
    initial_actions = [
	    {'open_tab': {'url': 'https://docs.google.com/document/d/1xWipCGja65lI_isvLQK3VJSUw_hHJTnrcYFsjH_S8U4/edit?tab=t.0'}}
    ]
    
    agent = Agent(
        task="Write a letter in Google Docs to my Papa, thanking him for everything, and save the document as a PDF.",
        llm=llm,
        use_vision=True,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions
    )
    result = await agent.run()
    print(result.final_result())
    await browser.close()

asyncio.run(main())
