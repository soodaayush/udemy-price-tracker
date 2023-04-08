import asyncio
import json
from pyppeteer import launch


async def main():
    browserObj = await launch({"headless": False})
    url = await browserObj.newPage()

    await url.goto('http://127.0.0.1:5500/index.html')
    await url.waitFor(5000)

    arr = []

    prices = await url.querySelectorAll("div .ud-sr-only > span")

    for price in prices:
        price = await price.getProperty("textContent")

        json_object = json.dumps(await price.jsonValue(), indent=0)
        print(await price.jsonValue())

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    # html = await url.content()
    await browserObj.close()


print(asyncio.get_event_loop().run_until_complete(main()))
