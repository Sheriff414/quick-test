import pytest
import sys
import os

# Ensures pytest can find your 'src' directory folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app as flask_app

@pytest.fixture()
def client():
    """Configures the Flask application for testing."""
    flask_app.config.update({
        "TESTING": True,
    })
    return flask_app.test_client()

def test_home_route(client):
    """Tests that the home route returns the correct DevOps string."""
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I am DevOps engineer!"
