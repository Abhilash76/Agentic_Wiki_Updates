from datetime import datetime
try:
    from rich.console import Console
    from rich.panel import Panel
    console = Console()
    USE_RICH = True
except Exception:
    USE_RICH = False

def log(title, msg, style="white"):
    ts = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    if USE_RICH:
        console.print(Panel(f"[{style}]{msg}[/]", title=f"[cyan]{title}[/]  [dim]{ts}"))
    else:
        print(f"[{title}] {ts}\n{msg}\n")
