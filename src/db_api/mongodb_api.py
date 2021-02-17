import logging
import os
from pymongo import MongoClient, cursor

from data_layer.detections import Detections
from utils.date_functions import move_date, get_current_date, str_to_datetime
from utils.files_operations import load_yaml


class MongoDB_API:

    def __init__(self, username, password, env='staging', ):

        self.__env = env
        self.__mongodb_url = f'mongodb://{username}:{password}@'
        self.__mongodb_url += {
            'staging': 'staging-gcp-shard-00-00-yaz2t.gcp.mongodb.net:27017,staging-gcp-shard-00-01-yaz2t.gcp.mongodb.net:27017,staging-gcp-shard-00-02-yaz2t.gcp.mongodb.net:27017/staging?ssl=true&replicaSet=staging-gcp-shard-0&authSource=admin',
            'production': 'production-gcp-shard-00-00-kxuwc.gcp.mongodb.net:27017,production-gcp-shard-00-01-kxuwc.gcp.mongodb.net:27017,production-gcp-shard-00-02-kxuwc.gcp.mongodb.net:27017/production?ssl=true&replicaSet=production-gcp-shard-0&authSource=admin'
        }[env]

    def execute(self, collection_name, action, query) -> cursor.Cursor:
        mongo_client = MongoClient(self.__mongodb_url, connect=False)
        try:
            mongodb_db = mongo_client[self.__env]
            logging.info(f"MongoDB env: {self.__env}")
            logging.info(f"MongoDB query: {collection_name}.{action}({query})")
            return getattr(getattr(mongodb_db, collection_name), action)(query)
        finally:
            mongo_client.close()

    def get_detections(self, detector_name: str, since_date: str, until_date: str) -> Detections:

        detections = Detections()
        mongo_db_query = {
            'detector.name': detector_name,
            'timestamp': {
                '$gte': str_to_datetime(since_date),
                '$lte': str_to_datetime(until_date),
            }
        }
        data = self.execute(collection_name='detections', action='find', query=mongo_db_query)
        [detections.add_detection(
            str(record['_id']),
            record['since'],
            record['until'],
            record['confidence'],
            record.get('review')
        ) for record in data]
        logging.info(f"{len(detections)} detection records fetched")
        return detections


def run_example() -> Detections:
    from pathlib import Path
    credentials_path = os.path.join(Path(__file__).parent.parent, 'configuration', 'mongodb_credentials.yaml')
    mongodb_credentials = load_yaml(credentials_path)
    mongodb_api = MongoDB_API(username=mongodb_credentials['username'], password=mongodb_credentials['password'])
    return mongodb_api.get_detections(
        detector_name='rapid_cliff',
        since_date=move_date(get_current_date(), - 30*5),
        until_date=move_date(get_current_date(), - 30*3)
    )


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    detections = run_example()
    print(f"{len(detections)} detections fetched from mongodb")
