[app]
title = 
package.name = 
package.domain = org.
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
source.include_patterns = custom/*.py
version = 1.0
requirements = python3
orientation = portrait
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
icon.filename = %(source.dir)s/icon.png
log_level = 2

[buildozer]
log_level = 2
