PREFIX ?= /usr/local
BINDIR = $(DESTDIR)$(PREFIX)/bin
MANDIR = $(DESTDIR)$(PREFIX)/share/man/man1
APPDIR = $(DESTDIR)$(PREFIX)/share/applications
ICONDIR = $(DESTDIR)$(PREFIX)/share/icons/hicolor/scalable/apps

.PHONY: install uninstall

install:
	install -Dm755 src/qlip $(BINDIR)/qlip
	install -Dm644 src/qlip.1 $(MANDIR)/qlip.1
	install -Dm644 src/qlip.desktop $(APPDIR)/qlip.desktop
	install -Dm644 src/qlip.svg $(ICONDIR)/qlip.svg

uninstall:
	rm -f $(BINDIR)/qlip
	rm -f $(MANDIR)/qlip.1
	rm -f $(APPDIR)/qlip.desktop
	rm -f $(ICONDIR)/qlip.svg
