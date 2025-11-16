.PHONY: help list-inboxes create-inbox delete-first-inbox create-list-delete-inbox check-env

.DEFAULT_GOAL := help

PYTHON := python3
PYTHON_PATH := PYTHONPATH=.

help: ## Show this help message
	@echo "Available commands:"
	@echo "  make list-inboxes          List all inboxes"
	@echo "  make create-inbox          Create a new inbox"
	@echo "  make delete-first-inbox    Delete the first inbox found"
	@echo "  make create-list-delete-inbox    Full pipeline: create, list, delete"

check-env: ## Check if .env file exists
	@if [ ! -f .env ]; then \
		echo "Error: .env file not found"; \
		echo "Create a .env file with: AGENTMAIL_API_KEY=your_key_here"; \
		exit 1; \
	fi

list-inboxes: check-env ## List all inboxes
	@$(PYTHON_PATH) $(PYTHON) examples/inboxes/list_inboxes.py

create-inbox: check-env ## Create a new inbox
	@$(PYTHON_PATH) $(PYTHON) examples/inboxes/create_inbox.py

delete-first-inbox: check-env ## Delete the first inbox found
	@$(PYTHON_PATH) $(PYTHON) examples/inboxes/delete_first_inbox.py

cld-inbox: check-env ## Full pipeline: create, list, delete
	@$(PYTHON_PATH) $(PYTHON) examples/inboxes/create_list_delete_inbox.py
