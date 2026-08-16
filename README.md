kubectl exec -it backend-9859b86c8-7dckb -- python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:5000/health').read().decode())"

for status health 

http://44.204.99.5:31461/health ---> url
