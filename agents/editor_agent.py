from services.logger import log

class EditorAgent:
    def _mock_llm_generate(self, file_path):
        if "model_inference" in file_path:
            return f"Update for `{file_path}`\n\n- Added retry logic for model loading.\n- Document this change and include new config options.\n"
        elif "data_pipeline" in file_path:
            return f"Update for `{file_path}`\n\n- Added null safety in transformations.\n- Add schema validation examples.\n"
        return f"Update for `{file_path}`\n\n- General improvements and documentation fixes.\n"

    def generate_updates(self, changed_files, repo_context):
        log("Editor", f"Generating drafts for {len(changed_files)} files...", "magenta")
        drafts = []
        for f in changed_files:
            draft = self._mock_llm_generate(f["path"])
            drafts.append({"path": f["path"], "draft": draft})
            log("Editor", f"Draft created for {f['path']}", "magenta")
        return drafts
