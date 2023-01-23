# arteflask

## requirements
- docker
- docker-compose

## up and running
- sudo docker-compose up
- access localhost 5000

## debugging (overkill)
- sudo docker-compose down
- sudo rmi -f {id-of-image}
- sudo docker container prune
- sudo fuser -k 5000/tcp
- go to "up and running"
