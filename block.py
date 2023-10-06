import hashlib
import datetime

class Block:

    def __init__(self, previous_block_hash, data, timestamp) -> None:
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.is_validate = False
        self.is_connected_to_block = False
        self.timestamp = timestamp
        self.hash = self.get_hash()

    @staticmethod
    def create_genesis_block():
        """
        create the first block

        args:
            None

        return -> block : Block
        """
        block = Block("0","0", datetime.datetime.now())
        block.is_validate = True
        return block
    
    def get_hash(self) -> str:
        """
        get the hash of the current block

        args : 
            None
        
        return -> hash : str
        """
        header_bin = (str(self.previous_block_hash) + str(self.data) + str(self.timestamp)).encode()
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash