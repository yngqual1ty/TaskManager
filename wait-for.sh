#!/bin/sh

HOST="$1"
PORT="$2"
shift 2
CMD="$@"

echo "Ждём, пока $HOST:$PORT станет доступен..."

while ! nc -z $HOST $PORT; do
  sleep 1
done

echo "$HOST:$PORT готов, запускаем команду: $CMD"
exec $CMD