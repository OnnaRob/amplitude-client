<!-- Here build and CI badges -->

---
<!-- PROJECT LOGO -->
<h1 align="center">
  <br>
  <img src="https://onna.com/wp-content/uploads/2020/03/h-onna-solid.png" alt="Onna Logo"></a>
</h1>

<h2 align="center">Amplitude Client</h2>


## About

[AIOHTTP](https://docs.aiohttp.org/en/stable/) based wrapper for the [Amplitude HTTP V2 API](https://developers.amplitude.com/docs/http-api-v2).

## Installation

```bash
pip install amplitude-client
```

## Usage

```python
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
```

