curl -X POST http://localhost:8000/login \
	 -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin&password=1234"

curl -X POST http://localhost:8000/register \
	 -H "Content-Type: application/json"  \
     -d "{\"username\":\"admin\",\"password\":\"1234\"}"