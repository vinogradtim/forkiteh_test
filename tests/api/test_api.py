import pytest


@pytest.mark.parametrize("address", [
    "TMBPqMxCpz2JNtKyQqiENr5CSdgQY4nt6x",
    "TMBPqMxCpz2JNtKyQqiENr5CSdgQY4nt6y",
    "TMBPqMxCpz2JNtKyQqiENr5CSdgQY4nt6z",
    "TMBPqMxCpz2JNtKyQqiENr5CSdgQY4nt6a"
])
async def test_get_wallet_info_endpoint(address, client, tron_client):
    resp = await client.post("/wallet/info", json={"address": address})

    assert resp.status_code == 200

    data = resp.json()
    mock_data = await tron_client.get_wallet_info(address)

    assert data['address'] == mock_data['address']
    assert data["balance"] == mock_data['balance']
    assert data["bandwidth"] == mock_data['bandwidth']
    assert data["energy"] == mock_data['energy']


@pytest.mark.parametrize("address", [
    "TMBPqMxCpz2",
    "TMBPqMxCpz2JNtKyQqiENr5CSdgQY4nt6y5848ff",
    ""
])
async def test_get_wallet_info_endpoint_fail(address, client):
    resp = await client.post("/wallet/info", json={"address": address})

    assert resp.status_code == 422
    assert resp.json()['detail'][0]['msg'] == 'Value error, Invalid address'
    assert resp.json()['detail'][0]['type'] == 'value_error'
    assert resp.json()['detail'][0]['input'] == address
