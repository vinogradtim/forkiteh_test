import pytest

from src.db.repositories import WalletQueryRepository


@pytest.mark.asyncio
async def test_save_wallet_query(mocker):
    mock_session = mocker.AsyncMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.commit = mocker.AsyncMock()
    mock_session.refresh = mocker.AsyncMock()
    mock_session.add = mocker.Mock()

    mocker.patch("src.db.repositories.async_session_maker", return_value=mock_session)

    repo = WalletQueryRepository()

    result = await repo.save_wallet_query(
        address="T123",
        balance=100,
        bandwidth=50,
        energy=200
    )

    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once()

    assert result['status'] == 'saved'
    assert result['query'].address == "T123"
    assert result['query'].balance == 100
    assert result['query'].energy == 200
    assert result['query'].bandwidth == 50
