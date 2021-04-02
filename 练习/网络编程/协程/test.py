# import asyncio
# import aiofiles

# async def wirte_demo():
# 	async with aiofiles.open("text.txt","w",encoding="utf-8") as fp:
# 		await fp.write("helo world")
# 		print("数据定稿成功")

# async def read_demo():
# 	async with aiofiles.open("text.txt","r",encoding="utf-8") as fp:
# 		content = await fp.read()
# 		print(f'content: {content}')

# async def read2_demo():
# 	async with aiofiles.open("text.txt","r",encoding="utf-8") as fp:
# 		async for line in fp:
# 			print(f"line: {line}")

# if __name__ == "__main__":
# 	asyncio.run(wirte_demo())
# 	asyncio.run(read_demo())
# 	asyncio.run(read2_demo())

import sys

print(sys.version_info)