FROM alpine:latest

RUN apk update && apk add bash curl

WORKDIR /tmp

COPY setup_ui.sh .
COPY export.ndjson .

ENTRYPOINT sh setup_ui.sh