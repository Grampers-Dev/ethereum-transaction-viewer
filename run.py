from web3 import Web3
import json
import requests

# Load API keys from creds.json
with open("creds.json") as creds_file:
    creds = json.load(creds_file)

coinmarketcap_api_key = creds.get("coinmarketcap_api_key", "")
infura_api_key = creds.get("infura_api_key", "")

# Your CoinMarketCap API key
api_key = coinmarketcap_api_key
infura_url = f"https://mainnet.infura.io/v3/{infura_api_key}"
web3 = Web3(Web3.HTTPProvider(
    "https://mainnet.infura.io/v3/your_infura_project_id"))


def display_transaction_info(tx):
    """
    Display transaction information.

    Args:
        tx (dict): Transaction information.

    Returns:
        None
    """
    # Define the function's code here
    labels_values = [
        ("Block Hash", tx.blockHash.hex()),
        ("Block Number", tx.blockNumber),
        ("From", tx['from']),
        ("To", tx.to),
        ("Gas", tx.gas),
        ("Gas Price (Wei)", tx.gasPrice),
        ("Hash", tx.hash.hex()),
        ("Nonce", tx.nonce),
        ("Type", tx.type),
        ("Value (Ether)", (tx.value)),
    ]
    for label, value in labels_values:
        print(f"{label}: {value}")


def get_transaction_info(block_hash):
    """
    Retrieve and display transaction information for a given block hash.

    Args:
        block_hash (str): Block hash for transaction info to be retrieved.

    Returns:
        None
    """
    try:
        tx = web3.eth.get_transaction_by_block(block_hash, 2)
        if tx:
            display_transaction_info(tx)
        else:
            print("Transaction not found.")
    except Exception as e:
        print("Error:", e)


def wei_to_ether(wei):
    """
    Convert wei to ether.

    Args:
        wei (int): Amount in wei to be converted.

    Returns:
        float: Equivalent amount in ether.
    """
    return web3.fromWei(wei, 'ether')


def get_ethereum_price(api_key):
    """
    Retrieve Ethereum price and market cap data from CoinMarketCap API.

    Args:
        api_key (str): Your CoinMarketCap API key.

    Returns:
        dict: Ethereum price and market cap data.
    """
    try:
        # CoinMarketCap API URL for Ethereum data
        url = (
            "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        )

        # Set the parameters for the API request
        params = {
            "symbol": "ETH",  # Symbol for Ethereum
            "convert": "USD",  # Convert prices to USD
        }

        # Set your CoinMarketCap API key in the headers
        headers = {
            "X-CMC_PRO_API_KEY": api_key,
        }

        # Make the API request
        response = requests.get(url, params=params, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            ethereum_data = data["data"]["ETH"]
            return ethereum_data
        else:
            print("Error:", response.status_code, response.text)
            return None
    except Exception as e:
        print("Error:", e)
        return None


def calculate_percentage_difference(value1, value2):
    """
    Calculate the percentage difference between two values.

    Args:
        value1 (float): The first value.
        value2 (float): The second value.

    Returns:
        float: The percentage difference between value2 and value1.
    """
    if value1 == 0:
        return 0  # Handle division by zero
    return ((value2 - value1) / value1) * 100

