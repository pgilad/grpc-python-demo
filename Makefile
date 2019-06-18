PROTO_TARGET_DIR := distance
PROTO_SRC_DIR := protos

.PHONY: build
build: $(PROTO_TARGET_DIR)/distance_pb2.py $(PROTO_TARGET_DIR)/distance_pb2_grpc.py

.PHONY: fmt
fmt: pyproject.toml
	pipenv run black *.py

.PHONY: lint
lint: .flake8
	pipenv run flake8 *.py

.PHONY: clean
clean:
	find . -type f -iname '*.pyc' -print -delete
	rm -f $(PROTO_TARGET_DIR)/*_pb2*.py

$(PROTO_TARGET_DIR)/__init__.py:
	mkdir -p $(PROTO_TARGET_DIR)
	touch $@

$(PROTO_TARGET_DIR)/distance_pb2.py: $(PROTO_SRC_DIR)/distance.proto
	mkdir -p $(PROTO_TARGET_DIR)
	pipenv run python3 -m grpc_tools.protoc -I $(<D) --python_out=$(PROTO_TARGET_DIR) $<

$(PROTO_TARGET_DIR)/distance_pb2_grpc.py: $(PROTO_SRC_DIR)/distance.proto
	mkdir -p $(PROTO_TARGET_DIR)
	pipenv run python3 -m grpc_tools.protoc -I $(<D) --grpc_python_out=$(PROTO_TARGET_DIR) $<
