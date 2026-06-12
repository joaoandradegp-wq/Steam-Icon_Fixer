<h1 align="center">🎮 Steam Icon Fixer</h1>

<p align="center">
Simple and automated tool for fixing broken, missing, or blank Steam game desktop icons.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success">
  <img src="https://img.shields.io/badge/Language-Python-blue">
  <img src="https://img.shields.io/badge/Type-Utility-lightgrey">
  <img src="https://img.shields.io/badge/Language-Português%20(BR)-009C3B">
  <img src="https://img.shields.io/badge/Language-English-3C3B6E">
</p>

---

## 📌 About

**Steam Icon Fixer** was developed to solve a common Windows issue:
Steam game desktop icons that disappear, become generic, broken, or completely blank.

The application automatically scans `.url` shortcuts, identifies Steam games, and re-downloads the original icons directly from Steam's official CDN.

The entire process is automated, including shortcut updates and immediate Windows notification to refresh icons without requiring an Explorer restart.

---

## ⚙️ Features

<br>
<table style="border: none; border-collapse: collapse;">

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔍 AUTOMATIC SCANNING

Automatically locates Steam shortcuts on the Desktop (including OneDrive), identifying `.url` files containing `steam://rungameid`.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🎯 GAME IDENTIFICATION

Extracts the GameID directly from the shortcut and uses it to retrieve the correct icon from Steam.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### ⬇️ AUTOMATIC ICON DOWNLOAD

Downloads icons directly from Steam's official CDN, ensuring valid and up-to-date files.

Includes size validation to prevent corrupted icons.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🔄 SHORTCUT UPDATES

Automatically updates the icon path inside the `.url` file, ensuring Windows uses the new icon file.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🆕 PROGRESSIVE ICON VERSIONING

Each time an icon is repaired, the program generates a new version:

`_new1`, `_new2`, `_new3`, `_new4`...

This forces Windows to use a new file and dramatically reduces issues caused by persistent icon cache.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### ⚡ INSTANT WINDOWS REFRESH

After fixing a shortcut, the program automatically notifies Windows Shell to refresh icons without restarting Explorer.

<br>
</td>
</tr>

<tr>
<td width="50%" valign="top" style="border: none; padding: 15px;">

### 🧠 SMART FILE MANAGEMENT

Removes older versions related to the same icon, prevents duplication, and keeps consistency between shortcuts and downloaded files.

<br><br>
</td>

<td width="50%" valign="top" style="border: none; padding: 15px;">

### 📊 REAL-TIME LOGGING & PROGRESS

Simple interface with a progress bar and real-time log showing every step of the process.

<br>
</td>
</tr>

</table>

---

## 🚀 How to Use

1. Click **Scan Desktop**
2. Click **Fix All**
3. Wait for the automatic processing
4. Your shortcuts will be updated automatically

There is no longer any need to manually clear the icon cache or restart Explorer.

---

## 🎯 Problems Solved

- Generic Steam icons
- Broken or missing icons
- Completely blank icons
- Persistent Windows icon cache issues
- Shortcuts with invalid icon paths
- Incorrect reuse of old icons by Windows

---

## 📸 Preview

<p align="center">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/4f209275-ce40-401c-924f-ad2906ee4ccd" />
</p>

---

<p align="center">
Built to automate something nobody should have to fix manually. 😄
</p>
