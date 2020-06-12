from amplitude_client.logger import AmplitudeLogger

import asyncio

logger = AmplitudeLogger(api_key="YOUR_API_KEY")


async def run():
    event_payload = {
        "user_id": "user@example.com",
        "event_type": "Performed some action",
        "event_properties": {"load_time": 0.5},
    }

    await logger.log_event(event=event_payload)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
