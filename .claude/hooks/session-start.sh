#!/bin/bash
# Bulut oturumu açılırken animasyon araçlarını kurar:
# Manim (animasyon), LaTeX (formüller), matplotlib/numpy (grafikler)
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

export DEBIAN_FRONTEND=noninteractive
APT_PAKETLER="libpango1.0-dev pkg-config ffmpeg texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-lang-european dvisvgm"

eksik=""
for p in $APT_PAKETLER; do
  dpkg -s "$p" >/dev/null 2>&1 || eksik="$eksik $p"
done
if [ -n "$eksik" ]; then
  apt-get install -y -q --no-install-recommends $eksik >/dev/null 2>&1 \
    || { apt-get update -q >/dev/null 2>&1 && apt-get install -y -q --no-install-recommends $eksik >/dev/null; }
fi

# Manim, sistem Python'unun setuptools'u ile kurulamadığı için ayrı bir ortama kurulur
MANIM_ENV=/opt/manimenv
if ! "$MANIM_ENV/bin/python" -c "import manim, matplotlib" >/dev/null 2>&1; then
  python3 -m venv "$MANIM_ENV"
  "$MANIM_ENV/bin/pip" install -q --upgrade pip setuptools wheel
  "$MANIM_ENV/bin/pip" install -q manim matplotlib numpy
fi

# manim komutu doğrudan çalışsın
echo "export PATH=\"$MANIM_ENV/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
