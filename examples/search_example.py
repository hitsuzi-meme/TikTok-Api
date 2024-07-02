from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get(
    "ms_token", None
)  # set your own ms_token, needs to have done a search before for this to work

ms_token = "sjQIXxBJKd77XEMzo2hXLvBBIU8Pi0Vqn-kXPxfr4MkGU3hT5VtiRiNiYl0Lk8mj7Rp2Y862hk4IFsk6iJ_pnbfeR7gtWxvYHZHzp4Zv5RZCuDvgMrdVLFPCPOf0NDb8VJScJILdokDvdCIyiK3FbHk="

async def search_users():
    async with TikTokApi() as api:
        # await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False, proxies=[{"server": "45.114.15.245:6226", "username": "rqemfkrr", "password": "zgcczh9te8yw"}])
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False, proxies=[{"server": "45.114.15.245:6226", "username": "rqemfkrr", "password": "zgcczh9te8yw"}])
        # async for user in api.search.users("PR", count=10):
        #     print(user)
        # async for user in api.search.search_type(search_term="PR", ojb_type="user", count=10):
        #     print(user)
        # async for user in api.search.general("PR", count=1000):
        # async for user in api.search.search_type("PR",obj_type="general", count=1000):
        #     # print(user)
        #     print(f"videoId: {user.as_dict['id']}")
        #     print(f"desc: {user.as_dict['desc']}")
        #     print(f"createTime: {user.as_dict['createTime']}")
        #     print(f"アカウントId: {user.as_dict['author']['uniqueId']}")
        #     print(f"ニックネーム: {user.as_dict['author']['nickname']}")
        #     print(f"いいね数: {user.as_dict['stats']['diggCount']}")
        #     print(f"シェア数: {user.as_dict['stats']['shareCount']}")
        #     print(f"再生数: {user.as_dict['stats']['playCount']}")
        #     print(f"ブックマーク数: {user.as_dict['stats']['collectCount']}")

        #     print('-------------')
        async for user in api.search.search_type("PR",obj_type="item", count=1000):
            print('-------------')
        # async for user in api.search.search_type(search_term="PR",obj_type="general", count=1):
        #     # print(user)
        #     print('aaaa')


if __name__ == "__main__":
    asyncio.run(search_users())
