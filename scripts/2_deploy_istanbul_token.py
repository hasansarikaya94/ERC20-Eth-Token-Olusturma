from brownie import accounts, config, IstanbulToken


initial_supply = 1000000000000000000000  # Tokenin ilk tedarik edilecek miktari (genesisi)
token_name = "ISTANBUL"
token_symbol = "IST"

def main():
    account = accounts[0]
    erc20 = IstanbulToken.deploy({"from": account})