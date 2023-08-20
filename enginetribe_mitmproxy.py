from dataclasses import dataclass
from typing import Literal

@dataclass
class Config:
    # Game platform.
    # "PC" for PC, "MB" for Android
    platform: Literal["PC", "MB"] = "PC"

    # Game language.
    # "ES" for Spanish, "CN" for Chinese, "EN" for English, "PT" for Portuguese
    locale: Literal["ES", "CN", "EN", "PT"] = "CN"

    original_token: str = "382041526"
    original_host: str = "199.127.62.141"
    original_port: int = 25624
    replace_token: str = f"SMMWE{platform}{locale}"
    replace_host: str = "hexpserver.ddns.net"
    replace_port: int = 30000


class EngineTribeProxy:
    def request(self, flow):
        if flow.request.host == Config.original_host and flow.request.port == Config.original_port:
            # Apply replacement
            flow.request.host = Config.replace_host
            flow.request.port = Config.replace_port
            flow.request.text = flow.request.text.replace(
                "token=" + Config.original_token,
                "token=" + Config.replace_token
            )

addons = [
    EngineTribeProxy()
]