
__all__ = ["normalize_message"]


async def normalize_message(message: str, special_symbols: str = ""):

    return message.translate(
        {ord(c): f"\\{c}" for c in ".!@#%^-" + "".join(special_symbols)},
    )
