from brownie import accounts, config, TokenERC20


initial_supply = 1000000000000000000000  # Tokenin ilk tedarik edilecek miktari (genesisi)
token_name = "ISTANBUL"
token_symbol = "IST"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(initial_supply, token_name, token_symbol, {"from": account}, publish_source =  True)