# Ethereum Transaction Viewer

Welcome to the Ethereum Transaction Viewer! This Python script allows you to explore Ethereum (ETH) blocks and Ethereum price using the Web3 library and CoinMarketCap API. You can perform the following actions:

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

## Purpose and Goals of the Application

### Purpose

The purpose of the Python script is to serve as an interactive tool for users interested in exploring the Ethereum blockchain and monitoring the price of Ethereum (ETH) from CoinMarketCap. It provides the following functions:

### Goals

1. **Transaction Information**: Allow users to retrieve and display detailed information about transactions on the Ethereum blockchain. Users can explore specific transaction details, including block number, sender, receiver, gas, and more.

2. **Ethereum Price Tracking**: Enable users to obtain real-time data on the price of Ethereum (ETH) in USD and compare it to the latest block. This feature helps users stay updated on the cryptocurrency market.

3. **Historical Data Comparison**: Allow users to specify a number of previous blocks to compare with the latest block. The script calculates and displays the percentage differences in Ethereum price and market capitalization between the latest block and the selected historical blocks.

4. **User-Friendly Interface**: Provide a user-friendly command-line interface with clear instructions and prompts for available actions, such as 'info,' 'price,' 'blocks,' and 'exit.'

5. **Continuous Updates**: Ensure the script continuously updates and tracks the latest block's data and Ethereum price, providing users with the most up-to-date information.

6. **Error Handling**: Implement robust error handling to gracefully manage network issues, API errors, and invalid user inputs, enhancing the application's reliability.

The application's primary objective is to empower users to explore Ethereum transactions and monitor Ethereum's real-time price, facilitating a better understanding of the cryptocurrency ecosystem.

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

## Technology Used

The technology used in this project is as follows:

1. **Python**: The primary programming language for developing the script.

2. **Web3**: A Python library for interacting with the Ethereum blockchain. It provides the necessary functionality to connect to an Ethereum node, retrieve blockchain data, and work with Ethereum transactions.

3. **dotenv**: A Python library used for loading environment variables from a `.env` file. It helps securely manage sensitive information like API keys and URLs.

4. **Requests**: A Python library for making HTTP requests. It's used in this script to communicate with the CoinMarketCap API to retrieve Ethereum price and market cap data.

5. **Infura**: Infura provides Ethereum nodes as a service. It's likely used as the Ethereum node provider for interacting with the Ethereum blockchain.

6. **CoinMarketCap API**: The script uses the CoinMarketCap API to obtain real-time data on Ethereum's price and market capitalization. Users need an API key from CoinMarketCap to access this data.

These technologies are integrated to create an application that allows users to explore Ethereum transactions and monitor the real-time price of Ethereum.

## Example Usage

Here is an example of how you can use this script:

1. Enter 'info' to get transaction information for the latest block.
2. Enter 'price' to get the current Ethereum price and compare it to the latest block.
3. Enter 'blocks' to specify the number of previous blocks to compare.
4. Enter 'exit' to quit the program.
