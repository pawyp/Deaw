
import json
from time import time
from bson.objectid import ObjectId
import aiohttp_jinja2
from aiohttp_session import get_session
from aiohttp import web


class home(web.View):
    async def get(self):
        return web.Response(body=bytes('It works !', 'utf-8'))
