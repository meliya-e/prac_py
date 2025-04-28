def task_docs():
    """Build documentation"""
    return {
            "actions": ["sphinx-build -M html source  _build"],
    }
