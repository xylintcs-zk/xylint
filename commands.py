import base64

CLEAR_COMMAND = "clear chat"
COMMAND_LIST_CMD = "commands"
AVAILABLE_COMMANDS = [
    "encode base16 <text>",
    "decode base16 <text>",
    "encode base32 <text>",
    "decode base32 <text>",
    "encode base64 <text>",
    "decode base64 <text>",
    CLEAR_COMMAND,
    COMMAND_LIST_CMD
]

def process_command(cmd: str) -> str:
    cmd = cmd.strip()

    # list of commands
    if cmd.lower() == COMMAND_LIST_CMD:
        return "\n".join(f"- {c}" for c in AVAILABLE_COMMANDS)

    # encode commands
    if cmd.lower().startswith("encode base16 "):
        return base64.b16encode(cmd[14:].encode()).decode()
    elif cmd.lower().startswith("encode base32 "):
        return base64.b32encode(cmd[14:].encode()).decode()
    elif cmd.lower().startswith("encode base64 "):
        return base64.b64encode(cmd[14:].encode()).decode()

    # decode commands
    elif cmd.lower().startswith("decode base16 "):
        return base64.b16decode(cmd[14:].encode()).decode()
    elif cmd.lower().startswith("decode base32 "):
        return base64.b32decode(cmd[14:].encode()).decode()
    elif cmd.lower().startswith("decode base64 "):
        return base64.b64decode(cmd[14:].encode()).decode()

    # unknown command
    return "Unknown command. Type 'commands' to view all available commands."