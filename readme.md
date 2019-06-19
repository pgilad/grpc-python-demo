# grpc-python-demo
> A minimal client-server gRPC example for finding Levenshtein distance between words

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Build Status](https://travis-ci.org/pgilad/grpc-python-demo.svg?branch=master)](https://travis-ci.org/pgilad/grpc-python-demo)

This is a minimal playable demo I did in order to learn gRPC. It involves a server with
a single entry RPC for calculating the Levenshtein distance between 2 words.

This demo includes a server and a client. The server is long-living (until stopped) and the
client runs several pre-defined RPC calls with different words.

[![asciicast](https://asciinema.org/a/l65iY1aDzDgfqXkSscaMaWC6B.svg)](https://asciinema.org/a/l65iY1aDzDgfqXkSscaMaWC6B)

## Requirements

- `python 3.7`
- `pipenv`
- `make`

## Install

```bash
$ git clone https://github.com/pgilad/grpc-python-demo.git
$ cd grpc-python-demo

# install dependencies
$ pipenv install --dev

# generate client stubs
$ make clean build

# start server
$ pipenv run python3 server.py

# start client
$ pipenv run python3 client.py
```

## Development

Run all required tasks:

`$ make clean lint fmt build`

## License

MIT © [Gilad Peleg](https://www.giladpeleg.com)
