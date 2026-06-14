
from typing import Callable

from assistant.skills.browser import open_firefox
from assistant.skills.steam import open_steam
from assistant.skills.clock import print_time
from assistant.core.responder import handle_chat


_ACTION_HANDLERS: dict[str, Callable[[str], None]] = {
    "FIREFOX": lambda comando: open_firefox(),
    "STEAM": lambda comando: open_steam(),
    "HORA": lambda comando: print_time(),
    "CHAT": lambda comando: handle_chat(comando),
}


def dispatch(action: str, comando: str) -> None:
    """Ejecuta el handler asociado a la acción si existe.

    Silencioso si la acción no está registrada (comportamiento similar al
    original donde no se hacía nada explícito en ese caso).
    """
    handler = _ACTION_HANDLERS.get(action)
    if handler:
        handler(comando)
