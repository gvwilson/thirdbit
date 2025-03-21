#!/usr/bin/env bash

# save the process group ID of this script
pgid=`ps -o pgid= $$`

# create CA key and cert simultaneously
openssl req -x509 -newkey RSA -nodes -keyout CA.key -days 10 -out CA.pem -reqexts \
	v3_ca -subj "/C=CA/ST=ON/L=Toronto/O=Third Bit/OU=x509"

# create server key and cert
openssl req -new -newkey RSA -nodes -keyout server.key -out server.csr -batch \
	-reqexts v3_req -subj "/CN=localhost"

# sign server CSR with CA key
openssl x509 -req -days 10 -in server.csr -CAkey CA.key -CA CA.pem -CAcreateserial \
	-out server.pem -extfile extfile.txt
echo "certificates created"

# check the subject in the signed server certificate
echo "Subject field in server.pem:" $(openssl x509 -in server.pem -noout -text | grep "Subject:")

# run server
python server.py &
echo "server launched"

# wait for server to be listening on port 1443
while ! lsof -n -iTCP:1443|grep -qw LISTEN ; do
    sleep 0.5
    printf "*"
done
echo "server listening, launching client"

# run client
python client.py

# kill this script and its children (client and server) when client finishes
echo "terminating"
pkill -TERM -g $pgid
