from services.logger import log

class RetrieverAgent:
    def get_changed_files(self, pr_event):
        for ev in pr_event:
            log("Retriever", f"Processing PR #{ev['pull_request']['number']} - {ev['pull_request']['title']}", "green")
            files = []
            for commit in ev.get("commits", []):
                for f in commit.get("files_changed", []):
                    files.append({"path": f["path"], "diff": f["diff"], "commit": commit["sha"]})
            log("Retriever", f"Found {len(files)} changed files.", "green")
            return files
