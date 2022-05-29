# Dean Dunbar - Hacker Industrial
# Sample code for interacting with erc20 token with python


from web3 import Web3


contractAddress = "0x9561C133DD8580860B6b7E504bC5Aa500f0f06a7"
abi = [
    {
        'inputs': [
            {
                'internalType': "uint256",
                'name': "initialSupply",
                'type': "uint256"
            }
        ],
        'name': "constructor",
        'stateMutability': "nonpayable",
        'type': "constructor"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': True,
                'internalType': "address",
                'name': "owner",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "address",
                'name': "spender",
                'type': "address"
            },
            {
                'indexed': False,
                'internalType': "uint256",
                'name': "value",
                'type': "uint256"
            }
        ],
        'name': "Approval",
        'type': "event"
    },
    {
        'anonymous': False,
        'inputs': [
            {
                'indexed': True,
                'internalType': "address",
                'name': "from",
                'type': "address"
            },
            {
                'indexed': True,
                'internalType': "address",
                'name': "to",
                'type': "address"
            },
            {
                'indexed': False,
                'internalType': "uint256",
                'name': "value",
                'type': "uint256"
            }
        ],
        'name': "Transfer",
        'type': "event"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "owner",
                'type': "address"
            },
            {
                'internalType': "address",
                'name': "spender",
                'type': "address"
            }
        ],
        'name': "allowance",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "spender",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "amount",
                'type': "uint256"
            }
        ],
        'name': "approve",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "account",
                'type': "address"
            }
        ],
        'name': "balanceOf",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "decimals",
        'outputs': [
            {
                'internalType': "uint8",
                'name': "",
                'type': "uint8"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "spender",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "subtractedValue",
                'type': "uint256"
            }
        ],
        'name': "decreaseAllowance",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "spender",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "addedValue",
                'type': "uint256"
            }
        ],
        'name': "increaseAllowance",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "name",
        'outputs': [
            {
                'internalType': "string",
                'name': "",
                'type': "string"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "symbol",
        'outputs': [
            {
                'internalType': "string",
                'name': "",
                'type': "string"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [],
        'name': "totalSupply",
        'outputs': [
            {
                'internalType': "uint256",
                'name': "",
                'type': "uint256"
            }
        ],
        'stateMutability': "view",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "recipient",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "amount",
                'type': "uint256"
            }
        ],
        'name': "transfer",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "nonpayable",
        'type': "function"
    },
    {
        'inputs': [
            {
                'internalType': "address",
                'name': "sender",
                'type': "address"
            },
            {
                'internalType': "address",
                'name': "recipient",
                'type': "address"
            },
            {
                'internalType': "uint256",
                'name': "amount",
                'type': "uint256"
            }
        ],
        'name': "transferFrom",
        'outputs': [
            {
                'internalType': "bool",
                'name': "",
                'type': "bool"
            }
        ],
        'stateMutability': "nonpayable",
        'type': "function"
    }
]


# Http testnet provider
# w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Http MATIC network provider
w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com/'))

contract_instance = w3.eth.contract(address=contractAddress, abi=abi)


totalSupply = contract_instance.functions.totalSupply().call()

decimals = contract_instance.functions.decimals().call()


print(f"the total supply is {totalSupply / (10 ** decimals)}")
