#!/usr/bin/python3
""" A function that lists all documents in a collection """
import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    Returns an empty list if no document is in the collection
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
