from agents.retriever_agent import RetrieverAgent
from agents.editor_agent import EditorAgent
from agents.validator_agent import ValidatorAgent
from agents.relativity_agent import RelativityAgent
from services.publisher import Publisher
from services.logger import log

class AgentOrchestrator:
    """Orchestrator to control the flow"""
    def __init__(self):
        self.retriever = RetrieverAgent()
        self.editor = EditorAgent()
        self.validator = ValidatorAgent()
        self.publisher = Publisher()

    def handle_pull_request(self, pr_event):
        files = self.retriever.get_changed_files(pr_event)
        for ev in pr_event:
            drafts = self.editor.generate_updates(files)
        valid, rejected = self.validator.check_drafts(drafts)

        for ev in pr_event:
            if any("README.md" in f["path"] for f in files) and "attachments" in ev["pull_request"]:
                relativity = RelativityAgent()
                review = relativity.evaluate_alignment(
                    [f["diff"] for f in files if "README.md" in f["path"]],
                    ev["pull_request"]["attachments"]
                )
                valid.append({"path": "README.md (alignment review)", "draft": str(review)})

            return {"valid": valid, "rejected": rejected}
            
        if valid:
            path = self.publisher.publish(valid, ev)
            log("Orchestrator", f"Published wiki updates: {path}", "cyan")
        else:
            log("Orchestrator", "No valid drafts to publish.", "red")

        return {"valid": valid, "rejected": rejected}
