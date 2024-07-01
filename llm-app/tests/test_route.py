# import pytest
# from flask import current_app, json
from unittest.mock import patch, Mock
from app.models.ask import QA



def test_ask_invalid_input(client):
    response = client.post('/api/ask', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input: question is required'}


@patch('app.routers.client.chat.completions.create')
@patch('app.controllers.ask_controller.AskController.get_answer')
def test_ask_success(mock_get_answer, mock_create, client, db_session):
    mock_response = Mock()
    mock_response.choices = [Mock(text="AI stands for Artificial Intelligence.")]
    mock_create.return_value = mock_response

    # Corrected mock value for `get_answer`
    mock_get_answer.return_value = "AI stands for Artificial Intelligence."

    response = client.post('/api/ask', json={'question': 'What is AI?'})

    assert response.status_code == 200
    assert response.json == {
        'question': 'What is AI?',
        'answer': "AI stands for Artificial Intelligence."
    }

