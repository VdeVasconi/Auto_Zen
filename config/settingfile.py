def zendesk_token():
  '''Nessa Função eu armazeno o token do zendesk para utilizar no main.py'''
  token = 'Basic abc123'
  return token


def jira_token():
  '''Nessa Função eu armazeno o token do jira para utilizar no main.py'''
  jtok = ''
  return jtok


def id_jira():
  '''Nessa Função eu armazeno o id do report jira para utilizar no main.py para abertura da task do jira para utilizar no
  Caso seja necessario na v2'''
  id = ''
  return id


def subdomain():
  '''Nessa função armazeno o endereço do dominio do zendesk para usar na requests'''
  url = 'https://subdomain.zendesk.com'
  return url


def subdomain_name():
  '''Nessa função armazeno o nome do dominio para usar no main.py'''
  name = 'subdomain'
  return name


def mail():
  '''Nessa Função armazeno o email para o envio da macro no Zendesk utilizando o zenpy a biblioteca do Zendesk no python!!'''
  email = 'dominio@dominio.com'
  return email
