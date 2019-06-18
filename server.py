#!/usr/bin/env python3

import logging
import time
from concurrent.futures.thread import ThreadPoolExecutor
from logging import Logger

import Levenshtein._levenshtein
import grpc

from distance import distance_pb2_grpc, distance_pb2

GRPC_PORT = 50051


class RouteGuideServicer(distance_pb2_grpc.RouteGuideServicer):
    logger: Logger

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)
        print(f"Bootstrapping {__class__.__name__}")

    def GetDistance(self, request, context):
        word1, word2 = request.word1, request.word2
        print(f"--> GetDistance Request {word1}, {word2}")
        d = Levenshtein._levenshtein.distance(word1, word2)
        return distance_pb2.Distance(distance=d)


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    distance_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port(f"[::]:{GRPC_PORT}")
    server.start()
    print("Server starting..")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
