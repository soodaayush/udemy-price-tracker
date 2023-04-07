import asyncio
from pyppeteer import launch


async def main():
    browserObj = await launch({"headless": False})
    url = await browserObj.newPage()

    await url.goto('https://www.udemy.com/courses/search/?src=ukw&q=Python')
    await url.waitFor(10000)

    prices = await url.querySelectorAll("span")

    for price in prices:
        price = await price.getProperty("textContent")
        print(await price.jsonValue())

    html = await url.content()
    await browserObj.close()
    return prices


print(asyncio.get_event_loop().run_until_complete(main()))
