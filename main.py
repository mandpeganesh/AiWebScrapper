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
	    {'open_tab': {'url': 'https://www.youtube.com/@campusx-official/videos'}}
    ]
    
    agent = Agent(
        task="Get the title and the url of the recent 5 videos of the channel",
        llm=llm,
        use_vision=True,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions
    )
    result = await agent.run()
    print(result.final_result())
    # data = result.final_result()
    # parsed: Posts = Posts.model_validate_json(result)
    await browser.close()

asyncio.run(main())
