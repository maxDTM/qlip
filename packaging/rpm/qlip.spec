Name:           qlip
Version:        1.0.0
Release:        1%{?dist}
Summary:        Lightweight screenshot utility for linux
License:        GPL-3.0-or-later
URL:            https://github.com/maxDTM/qlip
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python3 >= 3.8
Requires:       python3-tkinter

Recommends:     maim
Recommends:     slop
Recommends:     xdotool
Recommends:     xrandr
Recommends:     grim
Recommends:     slurp
Recommends:     wmctrl

%description
qlip captures screenshots with support for multi-monitor full-screen,
interactive region selection, and per-window capture. Includes a GUI
for settings and quick capture.

%prep
%autosetup

%install
%make_install PREFIX=/usr

%files
%license LICENSE
%{_bindir}/qlip
%{_mandir}/man1/qlip.1*
%{_datadir}/applications/qlip.desktop
%{_datadir}/icons/hicolor/scalable/apps/qlip.svg

%changelog
* Monday March 9 Max Alt - 1.0.0-1
- Initial release