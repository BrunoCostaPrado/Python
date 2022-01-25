from geopy.geocoders import Nominatim
from Funcoes_JSON import ler_arquivo,gravar_arquivo

geolocator=Nominatim(user_agent="wazeyes")
dicionario=ler_arquivo("entrada.json")
lista=dicionario["endereco"]
endereco=lista[0]+","+lista[1]+" "+lista[2]+" "+lista[3]
location=geolocator.geocode(endereco)
saida={"Coordenadas: "(location.latitude, location.longitude)}
gravar_arquivo(saida,"saida.json")