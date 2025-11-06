from fastapi.testclient import TestClient
from app import app
import json

c = TestClient(app)
res = c.get('/model-status')
print(json.dumps(res.json(), indent=2))
