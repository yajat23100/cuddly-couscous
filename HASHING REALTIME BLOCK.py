import hashlib
import json
from time import time
def block(proof,previous_hash = None):
 transaction_dict = {
 "Sender" : "Relando",
 "Reciever" : "Mousi",
 "ETH" : "150ETH"
 }

 data = {
 "Block Height" : 12907355,
 "Timestamp" : time(),
 "Transactions" : transaction_dict,
 "Block Reward" : 2.046327048499942521,
 "Uncles Reward" : 0,
 "Difficulty" : 7293278291370357,
 "Total Difficulty" : 28070572181009216929429,
 "Size" : str("81010bytes"),
 "Gas Used" : str("1499330599.96%"),
 "Gas Limit" : 14999907,
 "proof" : proof,
 "Previous hash" : previous_hash


 }

 print("Block Information : ",data)
 string_object = json.dumps(data)
 block_string = hashlib.sha3_512(string_object.encode())
 hexobject = block_string.hexdigest()
 print("Hash : ",hexobject)
block(proof = 0,previous_hash="No previous hash as this is first block")