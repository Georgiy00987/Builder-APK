[app]
title = GhostRun Studio
package.name = ghostrunstudio
package.domain = org.ghostrun
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
source.include_patterns = custom/*.py
version = 1.0
requirements = python3,kivy==2.3.0,aiohttp,multidict,yarl
orientation = portrait
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.arch = arm64-v8a
icon.filename = %(source.dir)s/icon.png
log_level = 2

[buildozer]
log_level = 2
