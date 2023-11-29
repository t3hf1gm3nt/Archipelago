import logging
from worlds._bizhawk.client import BizHawkClient
from worlds._bizhawk import read

logger = logging.getLogger("Client")

class TLOZClient(BizHawkClient):
    system = "NES"
    patch_suffix = ".aptloz"
    game = "The Legend of Zelda"

    def __init__(self):
        super().__init__()

    async def validate_rom(self, ctx):
        game_name = await read(ctx.bizhawk_ctx, [(0x0, 3, "PRG ROM")])
        game_name = game_name[0].decode("ascii")
        if game_name in "LOZ":
            ctx.game = self.game
            ctx.items_handling = 0b101  # get sent remote and starting items
            return True
        return False

    async def set_auth(self, ctx):
        auth_name = await read(ctx.bizhawk_ctx, [(0x20, 16, "PRG ROM")])
        auth_name = auth_name[0].decode("ascii").split("\x00")[0]
        ctx.auth = auth_name

    async def game_watcher(self, ctx):
        #TODO
        pass
