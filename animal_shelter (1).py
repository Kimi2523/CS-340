"""
CS 340 Project Two
Grazioso Salvare Animal Rescue Dashboard

MongoDB CRUD Module
Developer: Kimberly Ceballos
"""

import logging
from collections.abc import Mapping

from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Configure logging
LOGGER = logging.getLogger(__name__)


class AnimalShelter:
    """MongoDB CRUD interface for Austin Animal Center data."""

    def __init__(
        self,
        username,
        password,
        host="localhost",
        port=27017,
        database="aac",
        collection="animals",
        auth_source="aac"
    ):
        """Initialize the MongoDB connection."""

        self.client = MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            authSource=auth_source,
            serverSelectionTimeoutMS=5000
        )

        self.database = self.client[database]
        self.collection = self.database[collection]

    # ========================================================
    # CREATE
    # ========================================================

    def create(self, data):
        """Insert a new animal record into MongoDB."""

        if not isinstance(data, Mapping) or not data:
            return False

        try:
            result = self.collection.insert_one(dict(data))
            return (
                result.acknowledged
                and result.inserted_id is not None
            )

        except (PyMongoError, TypeError, ValueError):
            LOGGER.exception("Create operation failed")
            return False

    # ========================================================
    # READ
    # ========================================================

    def read(self, query, projection=None):
        """
        Retrieve animal records from MongoDB.

        Parameters:
            query: MongoDB query dictionary
            projection: Optional MongoDB field projection

        Returns:
            List of matching documents.
        """

        if not isinstance(query, Mapping):
            return []

        if projection is not None and not isinstance(
            projection, Mapping
        ):
            return []

        try:
            results = self.collection.find(
                dict(query),
                dict(projection)
                if projection is not None else None
            )

            return list(results)

        except (PyMongoError, TypeError, ValueError):
            LOGGER.exception("Read operation failed")
            return []

    # ========================================================
    # UPDATE
    # ========================================================

    def update(self, query, updates):
        """Update matching animal records."""

        if (
            not isinstance(query, Mapping)
            or not isinstance(updates, Mapping)
            or not updates
        ):
            return 0

        try:
            result = self.collection.update_many(
                dict(query),
                {"$set": dict(updates)}
            )

            return result.modified_count

        except (PyMongoError, TypeError, ValueError):
            LOGGER.exception("Update operation failed")
            return 0

    # ========================================================
    # DELETE
    # ========================================================

    def delete(self, query):
        """Delete matching animal records."""

        if not isinstance(query, Mapping):
            return 0

        try:
            result = self.collection.delete_many(
                dict(query)
            )

            return result.deleted_count

        except (PyMongoError, TypeError, ValueError):
            LOGGER.exception("Delete operation failed")
            return 0

    # ========================================================
    # TEST DATABASE CONNECTION
    # ========================================================

    def test_connection(self):
        """Verify that MongoDB authentication succeeds."""

        try:
            self.client.admin.command("ping")
            print("MongoDB connection successful!")
            return True

        except PyMongoError as error:
            LOGGER.error(
                "MongoDB connection failed: %s",
                error
            )
            return False

    # ========================================================
    # CLOSE DATABASE CONNECTION
    # ========================================================

    def close(self):
        """Close the MongoDB connection."""
        self.client.close()