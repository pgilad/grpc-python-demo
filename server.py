#!/usr/bin/env python3

import logging
import time
from concurrent.futures.thread import ThreadPoolExecutor

import Levenshtein._levenshtein
import grpc

from distance import distance_pb2_grpc, distance_pb2

GRPC_PORT = 50051


class WordsHelperServicer(distance_pb2_grpc.WordsHelperServicer):
    def __init__(self) -> None:
        logging.info(f"Bootstrapping")

    def GetDistance(self, request, context):
        word1, word2 = request.word1, request.word2
        logging.info(f"--> GetDistance Request {word1}, {word2}")
        d = Levenshtein._levenshtein.distance(word1, word2)
        return distance_pb2.Distance(distance=d)


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    distance_pb2_grpc.add_WordsHelperServicer_to_server(WordsHelperServicer(), server)
    server.add_insecure_port(f"[::]:{GRPC_PORT}")
    server.start()
    logging.info("Server starting..")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
