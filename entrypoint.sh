#!/bin/sh
set -e

# Wait for the database to be ready (optional but recommended)
# You might use a tool like 'wait-for-it.sh' or a custom script
# to ensure the database container is accessible before migrations.

echo "Running Alembic migrations..."
export PYTHONPATH=$PWD
alembic upgrade head

echo "Starting application..."
exec "$@" # This executes the command passed to the Docker container