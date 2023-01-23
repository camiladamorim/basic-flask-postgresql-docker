#  up and running

## requirements
- docker
- docker-compose

## to run
- sudo docker-compose up
- access localhost 5000
- when finnished "sudo docker-compose down"

## debugging
- sudo docker-compose down
- sudo rmi -f {id-of-image}
- sudo fuser -k 5000/tcp
- go to "up and running"

## debugging (overkill)
- sudo docker-compose down
- sudo rmi -f {id-of-image}
- sudo docker container prune
- sudo fuser -k 5000/tcp
- sudo systemctl restart docker
- go to "up and running"
