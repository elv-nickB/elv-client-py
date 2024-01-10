
import requests
from typing import Any, Dict
from typing import List

from .utils import get

class ElvClient():
    def __init__(self, config_url: str, static_token: str):
        config = get(config_url)
        self.fabricURIs = config["network"]["services"]["fabric_api"]
        self.searchURIs = config["network"]["services"]["search_v2"]
        self.ethereumURIs = config["network"]["services"]["ethereum_api"]
        self.token = static_token
    
    def content_object_metadata(self, 
                                library_id: str=None, 
                                object_id: str=None, 
                                version_hash: str=None, 
                                metadata_subtree: str=None,
                                select: List[str]=None, 
                                remove: List[str]=None
                                ) -> Any:
        url = '/'.join([self.fabricURIs[0], 'q', version_hash if version_hash else object_id, 'meta', metadata_subtree])
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, params={"select": select, "remove": remove}, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def call_bitcode_method(self, 
                            library_id: str=None, 
                            object_id: str=None, 
                            version_hash: str=None, 
                            method: str=None, 
                            params: Dict[str, Any]=None,
                            representation: bool=False,
                            host: str=None) -> Any:
        assert method is not None, "Method must be specified"
        call_type = 'rep' if representation else 'call'
        path = '/'.join(['q', version_hash if version_hash else object_id, call_type, method])
        if library_id:
            path = '/'.join(['qlibs', library_id, path])
        if host is None:
            host = self.fabricURIs[0]
        url = '/'.join([host, path])
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.post(url, json=params, headers=headers)
        response.raise_for_status()
        return response.json()
    
    # Search on a given index object
    def search(self, 
               library_id: str=None, 
               object_id: str=None,
               version_hash: str=None,
               query: Dict[str, Any]=None) -> Any:
        assert query is not None, "Query must be specified"
        return self.call_bitcode_method(library_id, object_id, version_hash, "search", query, host=self.searchURIs[0], representation=True)
    
    def content_object_library_id(self, 
                       object_id: str=None, 
                       version_hash: str=None
                       ) -> str:
        pass
    
if __name__ == "__main__":

    client = ElvClient("https://main.net955305.contentfabric.io/config", "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJlbHYiLCJleHAiOjE2MjQwMzQyNjgsImlhdCI6MTYyMzQyMjI2OCwiaXNzIjoiZWx2IiwianRpIjoiMjQ5ZjU3YzItMzQ3ZS00ZjY0LWE3ZTUtYzYxYjUxZjY3MzQwIiwibmJmIjoxNjIzNDIyMjY3LCJzdWIiOiJlbHYiLCJ0eXAiOiJhY2Nlc3MifQ.8K6q7Q2eKfZ9gqkQJ5ZKlNz6g6VW8qJYm4j6o5K1nX7z0tB7n1K8JY7Q7Km8V7Cf8Y9l4Z6Qnqf7v9R8Q6t2qQ")
    print(client.content_object_library_id(object_id='iq__2oENKiVcWj9PLnKjYupCw1wduUxj'))