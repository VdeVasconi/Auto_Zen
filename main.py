#Libraries
import requests
from zenpy.lib.api_objects import Ticket
from zenpy import Zenpy
from config.settingfile import zendesk_token
from config.settingfile import mail
from config.settingfile import subdomain
from config.settingfile import subdomain_name




if __name__ == "__main__":

  id_ticket = [ ]
  
  #Looping
  for idzen in id_ticket:
    zendesk_token()
    #Requets
    url = f"{subdomain()}/api/v2/tickets/{idzen}.json"

    headers = {
        "Authorization": f"{zendesk_token()}"
    }

    response = requests.get(url, headers=headers)
    json_zendesk = response.json()

    #Variavel Zendesk para armazenar o ticket do Zendesk
    idtck = json_zendesk['ticket']['id']
    
    #Envio Macro Zendesk
    creds = {
      'email' : f'{mail()}',
      'token' : f'{zendesk_token()}',
      'subdomain': f'{subdomain_name()}'
      }
    zenpy_client = Zenpy(**creds)
    #Id da Macro do zendesk
    id_macro = 1234 
    macro_result = zenpy_client.tickets.show_macro_effect(idtck, id_macro)
    zenpy_client.tickets.update(macro_result.ticket)
    print(f'Ticket {idtck} foi notificado!!!')