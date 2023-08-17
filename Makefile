#===============================
# Git commands
#===============================

COMMIT_MESSAGE ?= $(shell bash -c 'read -p "Commit Message: " COMMIT_MESSAGE; echo $$COMMIT_MESSAGE')

#@echo Commit Message › $(COMMIT_MESSAGE)
commit:
	git add .
	git commit -m "$(COMMIT_MESSAGE)"
	git push


pull:
	git fetch
	git pull

USERNAME ?= $(shell bash -c 'read -p "Username: " username; echo $$username')
PASSWORD ?= $(shell bash -c 'read -s -p "Password: " pwd; echo $$pwd')



talk:
	@clear
	@echo Username › $(USERNAME)
	@echo Password › $(PASSWORD)