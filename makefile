port ?= 8443
all: certificate run
run: run_server run_client
run_server:
	python3 server.py &
run_client:
	python3 client.py &
include certificate.mk
