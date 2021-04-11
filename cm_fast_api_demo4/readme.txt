https://curlbuilder.com/

curl -X POST http://localhost:8000/login

curl -XPOST -H "Content-type: application/json" -d '{"username":"admin","password":"1234"}' 'http://localhost:8000/register'


pip3 install python-multipart
curl -X POST http://localhost:8000/register  -H "Content-Type: application/x-www-form-urlencoded" -d "username=admin&password=555"