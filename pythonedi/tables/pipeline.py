import psycopg2

from subscriber.subscriber import SubscriberProcessor


def main(mapped_data: dict):

    conn = psycopg2.connect(
        host="localhost",
        database="edi_pipeline",
        user="postgres",
        password="postgres"
    )

    subscriber_processor = SubscriberProcessor(conn)

    subscriber_processor.process(mapped_data)

    conn.close()