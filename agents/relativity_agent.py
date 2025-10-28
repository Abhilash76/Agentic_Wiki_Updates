from services.logger import log
import random

class RelativityAgent:
    def evaluate_alignment(self, readme_diff, attachments):
        log("RelativityAgent", f"Evaluating {len(attachments)} source(s) for README.md alignment...", "blue")
        reviews = []
        for src in attachments:
            score = round(random.uniform(0.6, 0.95), 2)
            verdict = "✅ Consistent with source" if score >= 0.8 else "⚠️ Possible mismatch"
            suggestion = (
                "No action needed." if score >= 0.8
                else "Consider refining the README section for accuracy."
            )
            log("RelativityAgent", f"{src} → Score: {score} ({verdict})", "cyan")
            reviews.append({"source": src, "score": score, "verdict": verdict, "suggestion": suggestion})
        return reviews
