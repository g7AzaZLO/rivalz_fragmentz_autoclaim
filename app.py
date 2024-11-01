import time
import random
from web3automatization import Client, read_file
from config import CONTRACT_ADDRESS, CONTRACT_METHOD, CHAIN_ID, RPC_URL


def get_logo():
    print("""
████╗░██████╗░███████╗████╗ ░█████╗░███████╗░█████╗░███████╗██╗░░░░░░█████╗░
██╔═╝██╔════╝░╚════██║╚═██║ ██╔══██╗╚════██║██╔══██╗╚════██║██║░░░░░██╔══██╗
██║░░██║░░██╗░░░░░██╔╝░░██║ ███████║░░███╔═╝███████║░░███╔═╝██║░░░░░██║░░██║
██║░░██║░░╚██╗░░░██╔╝░░░██║ ██╔══██║██╔══╝░░██╔══██║██╔══╝░░██║░░░░░██║░░██║
████╗╚██████╔╝░░██╔╝░░████║ ██║░░██║███████╗██║░░██║███████╗███████╗╚█████╔╝
╚═══╝░╚═════╝░░░╚═╝░░░╚═══╝ ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝░╚════╝░
Telegram community: https://t.me/g7team_ru
""")


def main():
    while True:
        accounts = read_file("wallets.txt")
        for account in accounts:
            client = Client(account, RPC_URL)
            print(f"Клеймим NFT на адресе {client.public_key}")
            for i in range(20):
                if client.get_native_balance() > 0.00001:
                    claim_nft(client)
                    time.sleep(random.randint(5, 15))
                else:
                    print(f"На адресе {client.public_key} недостаточный баланс")
                    break

        sleep = random.randint(43201, 45000)
        print(f"Спим {sleep // 60} минут")
        time.sleep(sleep)


def claim_nft(client: Client):
    transaction = {
        'to': CONTRACT_ADDRESS,
        'value': 0,
        'gas': 300000,
        'gasPrice': client.connection.eth.gas_price,
        'nonce': client.get_nonce(),
        'data': CONTRACT_METHOD,
        'chainId': CHAIN_ID
    }
    try:
        tx_hash = client.send_transaction(transaction)
        print(f"NFT claim hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"Ошибка при выполнении транзакции: {e}")


if __name__ == "__main__":
    get_logo()
    main()
