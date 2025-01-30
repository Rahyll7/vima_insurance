Use Postman for testing 

1.To get Policies
http://127.0.0.1:5001/get_policies

no Payload

2.Search Policies


http://127.0.0.1:5001//search_policies

{
    "name":""
}

3.Filter Policies

http://127.0.0.1:5001/filter_policies

{
  "min_premium": "",
  "max_premium": "",
  "type": "",
  "min_coverage": "",
  "sort": "asc"
}

Pip install flask - install flask to run

python app.py  - to run backend

npm start to run front end 

deployed url - 

1.To get Policies
https://vimainsurance-production.up.railway.app/get_policies

no Payload

2.Search Policies

https://vimainsurance-production.up.railway.app/search_policies

{
    "name":""
}

3.Filter Policies



{
  "min_premium": "",
  "max_premium": "",
  "type": "",
  "min_coverage": "",
  "sort": "asc"
}