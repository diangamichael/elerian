import asyncio
from elarian import Elarian

client = Elarian(org_id='el_org_eu_u90EC6', app_id='el_app_efuX1k', api_key='el_k_test_d80d8db2c72f0e239d122a2cefbb2468b8d18ec7cebcc964bb74a2c4e9bb8a16')

async def on_connected():
  print("App is running!")

  alice = Customer(client=client, number="+254712345678", provider="cellular")

  data = {"name": "Alice"}
  await alice.update_metadata(data)

  resp = await alice.get_state()

async def start():
  client.set_on_connection_error(lambda err: print(f"Connnection error: {err}"))
  client.set_on_connected(on_connected)
  await client.connect()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start())
    loop.run_forever()