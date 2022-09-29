import asyncio
from elarian import Elarian

client = Elarian(org_id='el_org_eu_u90EC6', app_id='el_app_efuX1k', api_key='el_k_test_d80d8db2c72f0e239d122a2cefbb2468b8d18ec7cebcc964bb74a2c4e9bb8a16')

async def start():
  client.set_on_connection_error(lambda err: print(f"Connnection error: {err}"))
  client.set_on_connected(lambda: print("App is running!"))
  await client.connect()

if __name__ == "__main__":
    xloop = asyncio.get_event_loop()
    xloop.create_task(start())
    xloop.run_forever()