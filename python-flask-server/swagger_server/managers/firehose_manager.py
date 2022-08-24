## This file is a wrapper for communication between our Flask application and the AWS Kinesis Firehose.

import boto3
from flask import json

# TODO: This can be set as a system FLAG in the future to disable debug messages in production.
DEBUG = False


def init():

    global kinesis
    kinesis = KinesisFirehose(StreamName="KDS-S3-daredata-datalake")

    kinesis_description = kinesis.describe

    if DEBUG:
        print(
            "\n[DEBUG - Kinesis Data Stream]\n\
            This is a description of the Kinesis Firehose configuration parameters in use:\n"
        )

        print(kinesis_description)


class KinesisFirehose:
    def __init__(self, StreamName):
        """
        Instantiates a Kinesis Firehose stream object.
        :param StreamName: string
        :return: None
        """
        self.streamName = StreamName
        self.client = boto3.client("firehose", region_name="eu-central-1")

    @property
    def describe(self):
        """
        Method returns information about the Kinesis Firehose
        :return: JSON response
        """
        response = self.client.describe_delivery_stream(
            DeliveryStreamName=self.streamName, Limit=100
        )
        return json.dumps(response)

    def post(self, payload):
        """
        Uploads a JSON payload to Kinesis Firehose
        :param payload: JSON
        :return: JSON response
        """
        json_payload = json.dumps(payload) + "\n"
        json_payload_encoded = json_payload.encode("utf-8")

        response = self.client.put_record(
            DeliveryStreamName=self.streamName, Record={"Data": json_payload_encoded}
        )

        return json.dumps(response)
