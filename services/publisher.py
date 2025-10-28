from services.logger import log
from datetime import datetime
import os
import textwrap

class Publisher:
    def __init__(self, output_md="Wiki_Update.md"):
        self.output_md = output_md

    def publish(self, valid_drafts, pr_event):
        log("Publisher", f"Publishing {len(valid_drafts)} drafts to {self.output_md}", "blue")
        header = f"# Wiki Update - PR #{pr_event['pull_request']['number']}\n\n"
        with open(self.output_md, "w", encoding="utf-8") as fh:
            fh.write(header)
            for d in valid_drafts:
                fh.write(f"## {d['path']}\n\n{textwrap.dedent(d['draft'])}\n\n---\n\n")
        return os.path.abspath(self.output_md)
