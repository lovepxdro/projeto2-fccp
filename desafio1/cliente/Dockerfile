FROM alpine:latest

RUN apk add --no-cache curl

COPY start.sh /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]