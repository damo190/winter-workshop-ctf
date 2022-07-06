#!/bin/bash
app="abiramen/compclub-ctf-epf"
docker build -t ${app} .
docker run -d -p 1337:80 \
  --env JWT_SECRET=yeeet \
  --name=${app} \
  -v $PWD:/app ${app}
