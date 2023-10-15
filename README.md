# Ethereum Transaction Viewer

Welcome to the Ethereum Transaction Viewer! This Python script allows you to explore Ethereum (Eth) blocks and Ethereum price using the Web3 library and CoinMarketCap API. You can perform the following actions:

- Get transaction information for the latest block.
- Retrieve the current Ethereum price and compare it to the latest block.
- Specify the number of previous blocks to compare with the latest block.
- Exit the program.

## Prerequisites

Before using this script, make sure you have the following prerequisites in place:

1. **Python**: You need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Required Python Libraries**:
   - `web3`: You can install it using pip: `pip install web3`
   - `dotenv`: Install using `pip install python-dotenv`
   - `requests`: Install using `pip install requests`

3. **Ethereum Node**: You need access to an Ethereum node to use the Web3 library. You can either run a local Ethereum node or use an external node provider.

4. **CoinMarketCap API Key**: To retrieve Ethereum price and market cap data, you'll need to obtain an API key from CoinMarketCap: [Sign up here](https://pro.coinmarketcap.com/signup/)

## Getting Started

1. Create a `.env.apikeys` file in the same directory as this script and add your environment variables as follows:

   ```env
   INFURA_URL=<Your Infura URL>
   CMC_API_KEY=<Your CoinMarketCap API Key>
Replace <Your Infura URL> with the URL of your Ethereum node provider, and <Your CoinMarketCap API Key> with your CoinMarketCap API key.

## Usage

Upon running the script, you will be presented with the following options:

- Enter 'info' to get transaction information for the latest block.
- Enter 'price' to get the current Ethereum price and compare it to the latest block.
- Enter 'blocks' to specify the number of previous blocks to compare with the latest block.
- Enter 'exit' to quit the program.

## Functions

### `display_transaction_info(tx)`

This function displays transaction information for a given transaction.

### `get_transaction_info(block_hash)`

Retrieves and displays transaction information for a given block hash.

### `wei_to_ether(wei)`

Converts an amount in Wei to Ether.

### `get_ethereum_price(api_key)`

Retrieves Ethereum price and market cap data from CoinMarketCap API using your API key.

### `calculate_percentage_difference(value1, value2)`

Calculates the percentage difference between two values.

## Example Usage

Here is an example of how you can use this script:

1. Enter 'info' to get transaction information for the latest block.
2. Enter 'price' to get the current Ethereum price and compare it to the latest block.
3. Enter 'blocks' to specify the number of previous blocks to compare.
4. Enter 'exit' to quit the program.
