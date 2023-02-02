@echo off

if "%1" == "up" (
    docker-compose -f deploy/docker-compose.yml up -d --build --force-recreate
) else if "%1" == "run" (
    docker-compose -f deploy/docker-compose.yml up -d
) else if "%1" == "down" (
    docker-compose -f deploy/docker-compose.yml down
) else if "%1" == "update" (
    docker-compose -f deploy/docker-compose.yml build --no-cache --progress=plain
) else (
    echo Invalid command: %1
)
