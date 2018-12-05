import requests
import xmltodict

auth_details = ('YannThomassen@gmail.com', '3_91x7YtBlG9RDfZxJluXR5YZJlxfI5U592'
                                           'pU2BzSTl0hlhhiEITBA')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(api_url, auth = auth_details)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']
    vertrektijd = vertrektijd[11:16]

    print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)