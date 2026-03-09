# qlip

Lightweight screenshot utility for X11 and Wayland Linux desktops. Auto-detects display server at runtime.

## Dependencies

**X11:** python3, maim, slop, xdotool, xrandr, python3-tkinter. Optional: wmctrl  
**Wayland:** python3, grim, slurp, python3-tkinter. Plus one of: swaymsg (sway), hyprctl (Hyprland), or wlr-randr (generic wlroots)

## Install

```bash
sudo make install              # /usr/local
sudo make PREFIX=/usr install  # /usr
```

## Usage

```
qlip -a              # all monitors (separate file per display)
qlip -a -m           # active monitor only
qlip -a -m 13        # monitors 1 and 3 only
qlip -p              # select a region
qlip -w              # pick a window from a list
qlip -w -c           # capture active window
qlip -a -s           # capture all, prompt for save location
qlip gui             # open settings/capture GUI
```

## Configuration

Stored in `~/.config/qlip/config.json`:

| Key                 | Default                              | Description                      |
|---------------------|--------------------------------------|----------------------------------|
| `save_dir`          | `~/Pictures/Screenshots`             | Default save directory           |
| `ask_save_location` | `false`                              | Prompt on every capture          |
| `filetype`          | `png`                                | png, jpg, jpeg, or bmp           |
| `filename_template` | `screenshot-%Y-%m-%d_%H%M%S`        | strftime format codes            |

### Filename codes

| Code | Output        |
|------|---------------|
| `%Y` | 2025          |
| `%m` | 03            |
| `%B` | March         |
| `%d` | 09            |
| `%H` | 14            |
| `%M` | 30            |
| `%S` | 05            |

## Wayland support

qlip detects Wayland via `$WAYLAND_DISPLAY` and switches backends automatically. Compositor-specific features (active monitor, window listing, active window capture) work on Sway and Hyprland. Other wlroots compositors get monitor enumeration via `wlr-randr` but may lack window-level features.

## Packaging

Build files for AUR, Debian (.deb), and RPM are in `packaging/`.

## License

GPL-3.0-or-later

---

