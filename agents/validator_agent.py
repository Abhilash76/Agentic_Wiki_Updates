from services.logger import log

class ValidatorAgent:
    def _passes_checks(self, draft):
        return len(draft) > 100 and all(word not in draft.lower() for word in ["maybe", "might", "possibly"])

    def check_drafts(self, drafts):
        valid, rejected = [], []
        for d in drafts:
            if self._passes_checks(d["draft"]):
                valid.append(d)
                log("Validator", f"{d['path']} ✅ Passed validation", "yellow")
            else:
                rejected.append(d)
                log("Validator", f"{d['path']} ❌ Rejected - too short or uncertain", "red")
        return valid, rejected
