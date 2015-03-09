# Installs web2py and makes symlinks.

ROOT_DIR = $(abspath ./)
export ROOT_DIR
TARGET_WEB2PY_DIR = $(abspath web2py)
export TARGET_WEB2PY_DIR

.PHONY: all install uninstall run migrate deploy stop \
		aws sync
all:
	$(error Please specify target. Valid targets are: install, uninstall, deploy, migrate, aws, run or stop)

# Run a dev server without GUI, where the admin password is '123'.
run:
	$(eval include deploy/db/env_vars.sh)
	python $(WEB2PY)/web2py.py --nogui -p 8000 -a 123

stop:
	killall python

uninstall:
	rm -fr $(TARGET_WEB2PY_DIR)

install:
	$(MAKE) install -C site-packages
	@echo 'Make app symlinks...'
	ln -s $(abspath applications/myfreedomm) \
		$(abspath $(TARGET_WEB2PY_DIR)/applications/myfreecomm)
	ln -s $(abspath requirements.txt) \
		$(abspath $(TARGET_WEB2PY_DIR)/requirements.txt)
	ln -s $(abspath deploy/routes.py) \
		$(abspath $(TARGET_WEB2PY_DIR)/routes.py)
	cp $(TARGET_WEB2PY_DIR)/handlers/wsgihandler.py $(TARGET_WEB2PY_DIR)/application.py
