<img width="1024" alt="Steam Icon Fixer" src="https://github.com/user-attachments/assets/c274ea2c-d702-4d51-91a2-8d2e648b3e7e" />

<p align="center"><br>
  <img src="https://img.shields.io/badge/Status-Active-success">
  <img src="https://img.shields.io/badge/Language-Python-blue">
  <img src="https://img.shields.io/badge/Type-Utility-lightgrey">
  <img src="https://img.shields.io/badge/Languages-PT--BR%20%7C%20EN-purple">
  <img src="https://img.shields.io/badge/Platform-Windows-blue">
</p>

## 📌 About

**Steam Icon Fixer** is a lightweight Windows utility designed to solve a common Steam issue:

Steam game desktop icons that disappear, become generic, broken, or completely blank.

The application automatically scans `.url` shortcuts, identifies Steam games through their Steam GameID, and re-downloads the corresponding icons directly from Steam's official CDN.

The entire process is automated, including icon validation, progressive file versioning, shortcut updates, and Windows Shell notification to refresh the icons without requiring an Explorer restart.

The application is available in **Brazilian Portuguese (PT-BR) and English**, with the interface language automatically detected from the Windows UI language.

---

## ⚙️ Features

<br>
<table style="border: none; border-collapse: collapse;">

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔍 AUTOMATIC SCANNING

Automatically locates Steam shortcuts on the Windows Desktop, including the user's OneDrive Desktop folder when available.

The application identifies `.url` files containing:

`steam://rungameid/`

<br><br>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🎯 GAME IDENTIFICATION

Extracts the Steam GameID directly from each shortcut and uses it to retrieve the corresponding icon from Steam's official CDN.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### ⬇️ AUTOMATIC ICON DOWNLOAD

Downloads icons directly from Steam's official CDN.

Downloaded files are validated against a minimum file size to prevent invalid or incomplete icons from being used.

<br><br>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔄 SHORTCUT UPDATES

Automatically updates the `IconFile` entry inside each `.url` shortcut.

The shortcut timestamp is also updated to help Windows detect the modification.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🆕 PROGRESSIVE ICON VERSIONING

Each repair generates a new icon version using progressive numbering:

`_new1`, `_new2`, `_new3`, `_new4`...

This prevents Windows from continuously reusing a cached version of the previous icon.

<br><br>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🧹 SMART ICON CLEANUP

Before downloading a new version, previous `.ico` files belonging to the same icon are automatically removed.

This prevents old `_newX` files from accumulating and keeps the icon directory clean.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### ⚡ INSTANT WINDOWS REFRESH

After modifying a shortcut, the application automatically sends a `SHChangeNotify` notification to Windows Shell.

This helps Windows immediately recognize the shortcut change without restarting Explorer.

<br><br>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🌎 MULTI-LANGUAGE SUPPORT

The interface automatically detects the Windows UI language and supports:

🇧🇷 **Portuguese (PT-BR)**
🇺🇸 **English**

Other Windows languages automatically fall back to English.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 📊 REAL-TIME LOGGING & PROGRESS

Displays a real-time processing log and progress bar while repairing multiple shortcuts.

Each download, validation, error, and successful repair is reported directly in the interface.

<br><br>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### ⚙️ BACKGROUND PROCESSING

Icon repairs are performed in a background thread, keeping the application interface responsive while multiple shortcuts are being processed.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🛡️ ERROR HANDLING

The application safely handles download, invalid icon, URL, file rename, and shortcut update errors.

A failure affecting one shortcut does not unnecessarily interrupt the entire process.

<br><br>

</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🎛️ CONTROLLED USER FLOW

The **Fix All** button remains disabled until a Desktop scan has been completed and Steam shortcuts have been found.

This prevents incorrect usage and makes the workflow straightforward.

<br>
</td>
</tr>

</table>

---

## 🚀 How to Use

1. Launch **Steam Icon Fixer**
2. Click **Scan Desktop**
3. The application identifies all Steam shortcuts found on the Desktop
4. Click **Fix All**
5. Wait for the automatic processing
6. The shortcuts and icons will be updated automatically

The application detects the Windows interface language automatically and displays the appropriate interface in **PT-BR or English**.

There is normally **no need to manually clear the Windows icon cache or restart Explorer**.

---

## 🔄 How Icon Versioning Works

Windows can sometimes continue displaying a cached icon even after the shortcut has been updated.

To work around this behavior, Steam Icon Fixer uses progressive icon filenames.

For example:

```text
game.ico
game_new1.ico
game_new2.ico
game_new3.ico
```

When repairing an icon:

1. Previous versions of the same icon are identified and removed.
2. The next progressive version is determined.
3. A fresh icon is downloaded from Steam.
4. The downloaded file is validated.
5. The icon is renamed to the new `_newX` version.
6. The shortcut is updated to point to the new file.
7. Windows Shell is notified about the shortcut change.

This approach significantly reduces problems caused by persistent Windows icon caching.

---

## 🎯 Problems Solved

* Generic Steam icons
* Broken or missing Steam icons
* Completely blank icons
* Persistent Windows icon cache issues
* Shortcuts with invalid icon paths
* Windows continuing to display an old cached icon
* Multiple obsolete `_new` icon files
* Invalid or incomplete icon downloads
* Manual Explorer restarts after icon repairs

---

## 🪟 Compatibility

Designed for:

* Windows 10
* Windows 11

The application uses Windows Shell functionality to notify the operating system when shortcuts are modified.

---

## 📦 Requirements

* Windows 10 or Windows 11
* Internet connection
* Steam desktop shortcuts using `.url` files

No manual icon cache clearing or Explorer restart is normally required.

---

## 📸 Preview

<p align="center">
  <img width="500" alt="Steam Icon Fixer" src="https://github.com/user-attachments/assets/4f209275-ce40-401c-924f-ad2906ee4ccd" />
</p>

---

<p align="center">
Built to automate something nobody should have to fix manually. 😄
</p>
