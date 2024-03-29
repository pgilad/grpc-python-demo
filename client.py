#!/usr/bin/env python3

import logging
import time

import grpc

from distance import distance_pb2_grpc, distance_pb2

GRPC_PORT = 50051


def get_distance(stub, word1, word2):
    words = distance_pb2.Words(word1=word1, word2=word2)
    result: distance_pb2.Distance = stub.GetDistance(words)
    logging.info(f"Word distance between {word1} and {word2} is {result.distance}")


def run():
    with grpc.insecure_channel(f"localhost:{GRPC_PORT}") as channel:
        stub = distance_pb2_grpc.WordsHelperStub(channel)
        get_distance(stub, "gilad", "gil")
        get_distance(stub, "gilad", "giles")
        get_distance(stub, "tommy", "thomas")
        get_distance(stub, "yonathan", "jonathan")

        request = distance_pb2.FibonacciRequest()
        for result in stub.GetFibonacci(request):
            logging.info(f"Got next fib number {result.number}")
            time.sleep(0.2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
