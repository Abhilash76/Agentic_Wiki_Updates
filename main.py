from orchestrator import AgentOrchestrator
from services.logger import log
import json
import os

def run_demo():
    log("Demo", "Starting Agentic Wiki Editor demo (mocked)", "bold green")
    with open(os.path.join("data", "mock_pr_event.json")) as f:
        pr_event = json.load(f)

    orchestrator = AgentOrchestrator()
    summary = orchestrator.handle_pull_request(pr_event)

    log("Demo", f"Drafts Published: {len(summary['valid'])}, Rejected: {len(summary['rejected'])}", "cyan")

if __name__ == "__main__":
    run_demo()
