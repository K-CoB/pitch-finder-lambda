import os
import sys

import pymysql
import logging
import json

host = os.environ["DB_HOST"]
user = os.environ["DB_USERNAME"]
password = os.environ["DB_PASSWORD"]
db = os.environ["DB_NAME"]

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=host, user=user, passwd=password, db=db, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("연결 실패!")
    logger.error(e)
    sys.exit()

logger.info("연결 성공!")


def lambda_handler(event, context):
    if event["httpMethod"] == "GET":
        high = event['queryStringParameters']['high']
        low = event['queryStringParameters']['low']

        cur = conn.cursor()

        sql_string = f"select singer, song, highest_pitch, lowest_pitch, youtube_url \
                        from music where highest_pitch <= {high} and lowest_pitch >= {low} \
                        order by highest_pitch desc, lowest_pitch asc;"

        cur.execute(sql_string)
        rows = cur.fetchall()
        result = []
        logger.info(rows)
        for row in rows:
            result.append({
                "singer": row[0],
                "song": row[1],
                "high": row[2],
                "low": row[3],
                "youtube_url": row[4]
            })

        return {
            "statusCode": 200,
            "body": json.dumps(result),
        }