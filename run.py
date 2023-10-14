from web3 import Web3
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env.apikeys
load_dotenv(dotenv_path='.env.apikeys')


infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))
api_key = os.getenv("CMC_API_KEY")


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
    return web3(wei, 'ether')


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


if __name__ == "__main__":
    print("Welcome to the Ethereum Transaction Viewer!")
    print("This script allows you to explore Eth blocks and Eth price.")
    print("You can perform the following actions:")
    print("  - Enter 'info' to get transaction info for the latest block.")
    print("  - Enter 'price' Get Ether price and compare to the latest block.")
    print("  - Enter 'blocks' specify number of previous blocks to compare.")
    print("  - Enter 'exit' to quit the program.")
    print()

    latest_block = web3.eth.get_block('latest')
    block_hash = latest_block.hash.hex()

    print(f"Latest Block Hash: {block_hash}")
    latest_ethereum_data = get_ethereum_price(api_key)
    latest_ethereum_price = latest_ethereum_data["quote"]["USD"]["price"]
    latest_market_cap = latest_ethereum_data["quote"]["USD"]["market_cap"]

    block_history = []  # Store data from previous blocks
    block_history.append(
        (latest_block, latest_ethereum_price, latest_market_cap))
    while True:
        selection = input(
            "Enter 'info' to get transaction info, 'price' to get Eth price, "
            "'blocks' to specify the number of previous blocks to compare, or "
            "'exit' to quit: "
        )
        if selection.lower() == 'exit':
            break
        elif selection.lower() == 'info':
            # You can continue to use the existing block_hash
            get_transaction_info(block_hash)
        elif selection.lower() == 'price':
            new_block = web3.eth.get_block('latest')
            new_block_hash = new_block.hash.hex()  # Update block_hash here
            new_ethereum_data = get_ethereum_price(api_key)
            new_ethereum_price = new_ethereum_data["quote"]["USD"]["price"]
            new_market_cap = new_ethereum_data["quote"]["USD"]["market_cap"]

            # Calculate percentage difference with the latest block
            price_difference_percentage = calculate_percentage_difference(
                latest_ethereum_price, new_ethereum_price)
            market_cap_difference_percentage = calculate_percentage_difference(
                latest_market_cap, new_market_cap)

            print("Percentage Difference in Ethereum Price with Latest Block:",
                  price_difference_percentage)
            print("Percentage Difference in Market Cap with Latest Block:",
                  market_cap_difference_percentage)

            # Update the latest data and block
            latest_block = new_block
            latest_ethereum_price = new_ethereum_price
            latest_market_cap = new_market_cap

            # Store data from the new block
            block_history.append(
              (new_block, new_ethereum_price, new_market_cap))
            block_hash = new_block_hash  # Update block_hash

        elif selection.lower() == 'blocks':
            num_blocks = int(input(
             "Enter the number of previous blocks to compare: "))
    if num_blocks <= 0:
        print("Invalid number of blocks.")
    else:
        for i, prev_block_data in enumerate(
            reversed(block_history[-num_blocks:])
        ):
            prev_block, prev_ethereum_price, prev_market_cap = prev_block_data
            price_difference_percentage = calculate_percentage_difference(
                prev_ethereum_price, latest_ethereum_price)
            market_cap_difference_percentage = calculate_percentage_difference(
                prev_market_cap, latest_market_cap)
            print(
                f"Percentage Diff in Eth Price with Block {prev_block.number} "
                f"(Latest vs. {i+1} blocks ago): "
                f"{price_difference_percentage}"
            )
            print(
                f"Percentage Diff in MarketCap with Block {prev_block.number} "
                f"(Latest vs. {i+1} blocks ago): "
                f"{market_cap_difference_percentage}"
            )
