from block import Block
import datetime


class BlockChain :
    def __init__(self, genesis_block) -> None:
        self.genesis_block = genesis_block
        self.block_chain = {genesis_block.hash : genesis_block}

    def add_block(self, block:Block) -> bool:
        """
        try add block to block chain

        args :
            block -> type : Block

        return -> type : Bool 
        """
        if self.validity_of_block(block):
            self.block_chain[block.hash] = block
            return True
        else: 
            return False

    def validity_of_block(self, block:Block) -> bool:
        """
        Check the validity of the past block for accept th new one

        args:
            block -> type : Block

        return -> type : Bool
        """
        if block.previous_block_hash in self.block_chain:
            previous_block = self.block_chain[block.previous_block_hash]

            if previous_block.is_validate and not previous_block.is_connected_to_block:
                block.is_validate = True
                previous_block.is_connected_to_block = True
                return True
            
            raise BaseException(f"block error on validity or is already connected to another block of past block : {block.previous_block_hash}")
        
        else : 
            return False


if __name__ == '__main__':
    block = Block.create_genesis_block()

    block_chain = BlockChain(block)
    print(f"block d'origine cree -> {block.get_hash()}")
    print(block_chain.block_chain)

    for i in range(5):
        block = Block(block.get_hash(), {'la data'}, datetime.datetime.now())
        block_chain.add_block(block)
    print(block_chain.block_chain)


