def test_service_is_running(host):
    assert host.service('vector').is_running

def test_directory_is_exists(host): 
	assert host.exists('/home/vector')