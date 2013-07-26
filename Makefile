all:
	cd src; \
	zip -r ../thunderbird-redis-sender.xpi ./*
	@echo "Done. Install the thunderbird-redis-sender.xpi file in TB."