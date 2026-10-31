[app]
title = Vinayak App
package.name = vinayakapp
package.domain = com.vinayak.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# Android
[app:android]
android.permissions = FOREGROUND_SERVICE, POST_NOTIFICATIONS
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.foreground_service = True
p4a.bootstrap = sdl2
