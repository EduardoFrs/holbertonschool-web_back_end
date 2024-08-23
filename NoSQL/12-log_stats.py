#!/usr/bin/env python3

"""12. Log stats"""

from pymongo import MongoClient


def nginx_stats():
    """provides some stats about Nginx logs"""
    client = MongoClient('mongodb://localhost:27017/')

    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f'{total_logs} logs')

    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check_query = {
        "method": "GET",
        "path": "/status"
    }
    status_check_count = collection.count_documents(status_check_query)
    print(f'{status_check_count} status check')


if __name__ == "__main__":
    nginx_stats()
