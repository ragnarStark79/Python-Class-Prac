import asyncio

# First Example

# async def task():
#     await asyncio.sleep(2)
#     print("Done")

# async def main():
#     await task()
#     print("Next line")

# asyncio.run(main())



# Second Example

# async def task(name):
#     print(f"{name} started")
#     await asyncio.sleep(2)
#     print(f"{name} done")

# async def main():
#     t1 = asyncio.create_task(task("A"))
#     t2 = asyncio.create_task(task("B"))

#     print("Next line")
#     await t1
#     await t2

# asyncio.run(main())



# Third Example
async def task():
    await asyncio.sleep(2)
    print("Done")

async def main():
    t1 = asyncio.create_task(task())
    print("Next line")
    await t1
    # await asyncio.sleep(3)  # keep event loop alive

asyncio.run(main())
