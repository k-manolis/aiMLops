# aiMLops

An API using Python Flask with the following endpoints:   \
POST /models: Accepts an ML model file (e.g., .pkl) and metadata (name, version, accuracy).   \
GET /models: Returns metadata for all registered models.   \
GET /models/{name}: Retrieves metadata for a specific mode   \

execute locally run ` docker-compose up -d`    \
to run the test locally  `pytest test_api.py `   \
