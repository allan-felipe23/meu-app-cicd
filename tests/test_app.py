import pytest
from app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHomeEndpoint:
    """Test home endpoint"""
    
    def test_home_returns_200(self, client):
        """Test that home endpoint returns 200"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_has_message(self, client):
        """Test that home has expected message"""
        response = client.get('/')
        assert response.json['message'] == "Bem-vindo ao CI/CD Pipeline!"
    
    def test_home_has_version(self, client):
        """Test that home includes version"""
        response = client.get('/')
        assert 'version' in response.json


class TestHealthEndpoint:
    """Test health check endpoint"""
    
    def test_health_returns_200(self, client):
        """Test that health endpoint returns 200"""
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_status_is_healthy(self, client):
        """Test that health status is healthy"""
        response = client.get('/health')
        assert response.json['status'] == 'healthy'


class TestUsersEndpoint:
    """Test users endpoint"""
    
    def test_users_returns_200(self, client):
        """Test that users endpoint returns 200"""
        response = client.get('/api/users')
        assert response.status_code == 200
    
    def test_users_has_users_list(self, client):
        """Test that users returns a list"""
        response = client.get('/api/users')
        assert 'users' in response.json
        assert len(response.json['users']) == 3
    
    def test_users_have_required_fields(self, client):
        """Test that users have required fields"""
        response = client.get('/api/users')
        users = response.json['users']
        for user in users:
            assert 'id' in user
            assert 'name' in user
            assert 'email' in user


class TestDetailedHealthEndpoint:
    """Test detailed health endpoint"""
    
    def test_detailed_health_returns_200(self, client):
        """Test that detailed health returns 200"""
        response = client.get('/api/health/detailed')
        assert response.status_code == 200
    
    def test_detailed_health_has_services(self, client):
        """Test that detailed health includes services"""
        response = client.get('/api/health/detailed')
        assert 'services' in response.json


class TestVersionEndpoint:
    """Test version endpoint"""
    
    def test_version_returns_200(self, client):
        """Test that version endpoint returns 200"""
        response = client.get('/version')
        assert response.status_code == 200
    
    def test_version_has_version_field(self, client):
        """Test that version includes version field"""
        response = client.get('/version')
        assert 'version' in response.json


class TestErrorHandling:
    """Test error handling"""
    
    def test_404_not_found(self, client):
        """Test 404 error handling"""
        response = client.get('/inexistent-endpoint')
        assert response.status_code == 404
    
    def test_404_has_error_message(self, client):
        """Test that 404 has error message"""
        response = client.get('/inexistent-endpoint')
        assert 'error' in response.json
