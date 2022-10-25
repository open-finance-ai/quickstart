import requests
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

OF_CLIENT_ID = os.getenv("OF_CLIENT_ID")
OF_CLIENT_SECRET = os.getenv("OF_CLIENT_SECRET")

token_data = {
  "userId": "someuser",
  "clientId": OF_CLIENT_ID,
  "clientSecret": OF_CLIENT_SECRET,
}

def list_to_df(res_list: list) -> pd.DataFrame:
    list_for_df = []
    for item in res_list:
        list_for_df.append(item)

    df = pd.DataFrame.from_dict(list_for_df)

    return df

def get_token(userId: str, clientId: str, clientSecret: str) -> str:
  token_r = requests.post("https://api.open-finance.ai/oauth/token", json={ "userId": userId, "clientId": clientId, "clientSecret": clientSecret })
  token = token_r.json()["accessToken"]
  return token

def create_connection(token: str) -> str:
  create_connection_data = {
    "refreshData": True,
    "includeFakeProviders": True,
  }
  headers = {
    "authorization": "Bearer " + token 
  }
  create_connection_r = requests.post("https://api.open-finance.ai/v2/connections", json=create_connection_data, headers=headers)
  connect_url = create_connection_r.json()["connectUrl"]
  return connect_url

def get_connections(token: str) -> dict[str, str]:
  headers = {
    "authorization": "Bearer " + token 
  }
  get_connections_r = requests.get("https://api.open-finance.ai/v2/connections", headers=headers)
  return get_connections_r.json()

def get_accounts(token: str) -> dict[str, str]:
  headers = {
    "authorization": "Bearer " + token 
  }
  get_accounts_r = requests.get("https://api.open-finance.ai/v2/data/accounts", headers=headers)
  return get_accounts_r.json()

def get_transactions(token: str) -> dict[str, str]:
  headers = {
    "authorization": "Bearer " + token 
  }
  get_transactions_r = requests.get("https://api.open-finance.ai/v2/data/transactions", headers=headers)
  return get_transactions_r.json()

def user_has_active_connections(token: str) -> bool:
  connections = get_connections(token)["items"]
  active_connection = list(filter(lambda connection: connection["status"] == "ACTIVE", connections))
  return bool(active_connection)





try:
  token = get_token(**token_data)
  is_user_has_active_connections = user_has_active_connections(token)
  if is_user_has_active_connections:
    print('user has active connections, fetching connections, accounts and transactions')
    connections = get_connections(token)
    accounts = get_accounts(token)
    transactions = get_transactions(token)
    print('connections', list_to_df(connections["items"]))
    print('accounts', list_to_df(accounts["items"]))
    print('transactions', list_to_df(transactions["items"]))
  else:
    print('user does not have active connections, please follow the url to create them (more info is in docs.open-finance.ai)')
    connect_url = create_connection(token)
    print(connect_url)
except Exception as e:
  print(e)