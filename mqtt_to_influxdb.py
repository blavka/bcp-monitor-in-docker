#!/usr/bin/env python3
import os
import sys
from logging import DEBUG, INFO
import logging as log
import json
import time
import datetime
import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient

LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'


def mgtt_on_connect(client, userdata, flags, rc):
    log.info('Connected to MQTT broker with (code %s)', rc)

    client.subscribe('node/+/+/+/+')


def mgtt_on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode('utf-8'))
    except Exception as e:
        return

    topic = msg.topic.split('/')
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    if isinstance(payload, str):
        return

    if isinstance(payload, dict):
        return

    json_body = [{'measurement': topic[4],
                    'time': now,
                    'tags': { "device_id":topic[1], "dev": '/'.join(topic[2:4]) },
                    'fields': {'value': payload}}]
    userdata['influx'].write_points(json_body)


def main():
    log.basicConfig(level=INFO, format=LOG_FORMAT)

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'node')

    mqttc = mqtt.Client(userdata={'influx': client})
    mqttc.on_connect = mgtt_on_connect
    mqttc.on_message = mgtt_on_message

    mqttc.connect('localhost', 1883, keepalive=10)
    mqttc.loop_forever()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        log.error(e)
        if os.getenv('DEBUG', False):
            raise e
        sys.exit(1)
