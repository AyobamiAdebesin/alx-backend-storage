#!/usr/bin/env python3
""" Returns a list of schools having a specific topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Find by specific value """
    return mongo_collection.find({"topics": {"$in": [topic]}})
