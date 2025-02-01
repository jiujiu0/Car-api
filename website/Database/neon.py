import psycopg2
from psycopg2 import sql
from flask import current_app


def neon_query_raw(query, query_params=None, database='default_db', log_depth=4):
    """
        Helper function for executing queries securely using parameterized queries.
        :param query: SQL query to execute
        :param query_params: Dictionary of parameters for the query
        :param database: Database name (not used directly but kept for consistency)
        :param log_depth: Logging depth for error handling
        :return: Query result as a list of dictionaries
    """
    if query_params is None:
        query_params = {}

    connection = getattr(current_app, 'db', None)
    if connection is None:
        raise RuntimeError("Database connection is not initialized in Flask app context.")

    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(sql.SQL(query), query_params)
        fetch_data = cursor.fetchall()

        # Convert the result into a list of dictionaries
        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in fetch_data]
        cursor.close()
    except psycopg2.DatabaseError as e:
        error_message = f"PostgreSQL Database Error: {e}"
        current_app.logger.error(error_message, exc_info=True)
        result = []
    finally:
        connection.commit()
    return result
