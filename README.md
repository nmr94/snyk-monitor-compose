# Snyk Monitor (Docker Compose)
A small utility to search for docker-compose.yml files, extract the images from those files and
finally run a Snyk monitor on them.

## Pre-reqs
* Python installed
* Snyk CLI

## Usage
1. Export your Snyk API token `export SNYK_TOKEN=abc1234-12312aa`
2. Run the tool `python3 snyk-monitor-compose.py`

You'll see the tool print out all of the compose files found, the images within those files, and
then it will start monitoring those with Snyk. Once the monitor has finished, you'll see the 
snapshot URL.

I use a cron to run this on a daily basis, this ensures that new images are monitored when I
add new docker compose files or update the images in existing ones.