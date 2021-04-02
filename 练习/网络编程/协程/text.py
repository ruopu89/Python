import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession

logging.basicConfig(
	format="%(asctime)s %(levelname)s:%(name)s:%(message)s",
	level=logging.DEBUG,
	datefmt="%H:%M:%S",
	stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True
HREF_RE = re.compile(r'href="(.*?)"')
# .表示匹配除换行符外任意一个字符，*表示前面的正则表达式会重复0次或多次；?表示前面的正则表达式会重复0次或1次。后边多一个？表示懒惰模式。必须跟在*或者+后边，也就是匹配到一次就不匹配了，如
# =================================================
# re.compile(pattern, flags=0)
# # 设定flags，编译模式，返回正则表达式对象regex。
# # pattern就是正则表达式字符串，flags是选项。正则表达式需要被编译，为了提高效率，这些编译后的结果被保存，下
# # 次使用同样的pattern的时候，就不需要再次编译。re的其他方法为了提高效率都调用了编译方法，就是为了提速。
# *** 先用re.compile('pattern')方法编译并赋值给变量，再使用不同的方法（如：match、search、fullmatch）在指定的字符串内找被赋值的变量 ***
# 如：<img src="test.jpg" width="60px" height="80px"/>
# 如果用正则匹配src中内容非懒惰模式匹配
# src=".*"
# 匹配结果是：src="test.jpg" width="60px" height="80px"
# 意思是从="往后匹配，直到最后一个"匹配结束
 
# 懒惰模式正则：
# src=".*?"
# 结果：src="test.jpg"
# 因为匹配到第一个"就结束了一次匹配。不会继续向后匹配。因为他懒惰嘛。
 
# .表示除\n之外的任意字符
# *表示匹配0-无穷
# ========================================================

async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
	resp = await session.request(method="GET", url=url, **kwargs)
	resp.raise_for_status()
	logging.info("Got response [%s] for URL: %s", resp.status, url)
	html = await resp.text()
	# print(f"html: {html}")
	return html

async def parse(url: str, session:ClientSession, **kwargs) -> set:
	found = set()
	try:
		html = await fetch_html(url=url, session=session, **kwargs)
		# print(f"html11111: {html}")
	except (
		aiohttp.ClientError,
		aiohttp.http_exceptions.HttpProcessingError,
	) as e:
		logger.error(
			"aiohttp exception for %s [%s]: %s",
			url,
			getattr(e, "status", None),
			getattr(e, "message", None),
		)
		return found
	except Exception as e:
		logger.exception(
			"Non-aiohttp exception occured: %s", getattr(e, "__dict__", {})
		)

		return found
	else:
		for link in HREF_RE.findall(html):
			print(f"link: {link}")
			try:
				abslink = urllib.parse.urljoin(url, link)
				print(f"abslink: {abslink}, url: {url}, link: {link}")
			except (urllib.error.URLError, ValueError):
				logger.exception("Error parsing URL: %s", link)
				pass
			else:
				found.add(abslink)
		logger.info("Found %d links for %s", len(found), url)
		# print(f"found: {found}")
		return found

async def write_one(file: IO, url: str, **kwargs) -> None:
	res = await parse(url=url, **kwargs)
	if not res:
		return None
	async with aiofiles.open(file, "a") as f:
		for p in res:
			await f.write(f"{url}\t{p}\n")
		logger.info("Wrote results for source URL: %s", url)


async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
	"""Crawl & write concurrently to `file` for multiple `urls`."""
	async with ClientSession() as session:
		tasks = []
		for url in urls:
			tasks.append(
				write_one(file=file, url=url, session=session, **kwargs)
			)
		await asyncio.gather(*tasks)

if __name__ == "__main__":
	import pathlib
	import sys

	assert sys.version_info >= (3,), "Script requires Python3.7+"

	here = pathlib.Path(__file__).parent

	with open(here.joinpath("urls.txt")) as infile:
		urls = set(map(str.strip, infile))

	outpath = here.joinpath("foundurls.txt")
	with open(outpath, "w") as outfile:
		outfile.write("source_url\tparsed_url\n")

	# asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))
	loop = asyncio.get_event_loop()
	loop.run_until_complete(bulk_crawl_and_write(file=outpath, urls=urls))



# """Asynchronously get links embedded in multiple pages' HMTL."""

# import asyncio
# import logging
# import re
# import sys
# from typing import IO
# import urllib.error
# import urllib.parse

# import aiofiles
# import aiohttp
# from aiohttp import ClientSession

# logging.basicConfig(
#     format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
#     level=logging.DEBUG,
#     datefmt="%H:%M:%S",
#     stream=sys.stderr,
# ) 
# logger = logging.getLogger("areq") 
# logging.getLogger("chardet.charsetprober").disabled = True

# HREF_RE = re.compile(r'href="(.*?) "') 

# async def fetch_html(url: str, session: ClientSession, **kwargs)  -> str:
#     """GET request wrapper to fetch page HTML.

#     kwargs are passed to `session.request() `.
#     """

#     resp = await session.request(method="GET", url=url, **kwargs) 
#     resp.raise_for_status() 
#     logger.info("Got response [%s] for URL: %s", resp.status, url) 
#     html = await resp.text() 
#     return html

# async def parse(url: str, session: ClientSession, **kwargs)  -> set:
#     """Find HREFs in the HTML of `url`."""
#     found = set() 
#     try:
#         html = await fetch_html(url=url, session=session, **kwargs) 
#     except (
#         aiohttp.ClientError,
#         aiohttp.http_exceptions.HttpProcessingError,
#     )  as e:
#         logger.error(
#             "aiohttp exception for %s [%s]: %s",
#             url,
#             getattr(e, "status", None) ,
#             getattr(e, "message", None) ,
#         ) 
#         return found
#     except Exception as e:
#         logger.exception(
#             "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {}) 
#         ) 
#         return found
#     else:
#         for link in HREF_RE.findall(html) :
#             try:
#                 abslink = urllib.parse.urljoin(url, link) 
#             except (urllib.error.URLError, ValueError) :
#                 logger.exception("Error parsing URL: %s", link) 
#                 pass
#             else:
#                 found.add(abslink) 
#         logger.info("Found %d links for %s", len(found) , url) 
#         return found

# async def write_one(file: IO, url: str, **kwargs)  -> None:
#     """Write the found HREFs from `url` to `file`."""
#     res = await parse(url=url, **kwargs) 
#     if not res:
#         return None
#     async with aiofiles.open(file, "a")  as f:
#         for p in res:
#             await f.write(f"{url}\t{p}\n") 
#         logger.info("Wrote results for source URL: %s", url) 

# async def bulk_crawl_and_write(file: IO, urls: set, **kwargs)  -> None:
#     """Crawl & write concurrently to `file` for multiple `urls`."""
#     async with ClientSession()  as session:
#         tasks = []
#         for url in urls:
#             tasks.append(
#                 write_one(file=file, url=url, session=session, **kwargs) 
#             ) 
#         await asyncio.gather(*tasks) 

# if __name__ == "__main__":
#     import pathlib
#     import sys

#     assert sys.version_info >= (3, 7) , "Script requires Python 3.7+."
#     here = pathlib.Path(__file__).parent

#     with open(here.joinpath("urls.txt"))  as infile:
#         urls = set(map(str.strip, infile)) 

#     outpath = here.joinpath("foundurls.txt") 
#     with open(outpath, "w")  as outfile:
#         outfile.write("source_url\tparsed_url\n") 

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(bulk_crawl_and_write(file=outpath, urls=urls))
    # asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))