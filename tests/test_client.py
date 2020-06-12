from amplitude_client.logger import AmplitudeLogger
from amplitude_client.logger import API_URL

import json
import pytest

pytestmark = pytest.mark.asyncio


async def test_amplitude(mock_aioresponse):

    amp_logger = AmplitudeLogger(api_key="1234")

    request = {"user_id": "foo", "event_type": "Performed an action"}
    mock_aioresponse.post(API_URL, status=200, payload=json.dumps(request), body="ok")

    # Missing fields
    resp = await amp_logger.log_event(event={"foo": "bar"})

    assert resp is None

    resp = await amp_logger.log_event(event=request)

    assert resp.status == 200
