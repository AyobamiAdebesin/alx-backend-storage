#!/usr/bin/env python3
""" A function that changes all topics of a school document based
on the name """
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on
    the name
    """
    return mongo_colection.update_many(
            {
                "name": name
                },
            {"$set": {"topics": topics}
                })
