import os
import threading
import time
import subprocess
import requests
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from queue import Queue

MIN_ICON_SIZE = 2048


def find_steam_shortcuts():
    paths = []
    user = os.path.expanduser("~")

    desktop = os.path.join(user, "Desktop")
    onedrive_desktop = os.path.join(user, "OneDrive", "Desktop")

    locations = [desktop]

    if os.path.exists(onedrive_desktop):
        locations.append(onedrive_desktop)

    for base in locations:
        if not os.path.exists(base):
            continue

        for file in os.listdir(base):
            if file.lower().endswith(".url"):
                full = os.path.join(base, file)

                if is_steam_url(full):
                    paths.append(full)

    return paths


def is_steam_url(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if line.startswith("URL=steam://rungameid/"):
                    return True
    except:
        pass

    return False


def download_file(url, dest):
    try:
        r = requests.get(url, timeout=15)

        if r.status_code == 200:
            with open(dest, "wb") as f:
                f.write(r.content)
            return True
    except:
        pass

    return False


def process_file(file_path, log_callback):
    url = ""
    icon_file = ""

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith("URL="):
            url = line.strip().split("=", 1)[1]

        elif line.startswith("IconFile="):
            icon_file = line.strip().split("=", 1)[1]

    if not url.startswith("steam://rungameid/"):
        return False

    gameid = url.replace("steam://rungameid/", "")

    if not icon_file:
        return False

    icon_dir = os.path.dirname(icon_file)
    original_name = os.path.basename(icon_file)

    import re

    base_name = original_name

    match = re.match(r"^(.*?)(_new(\d+)?)?(\.[^.]+)$",base_name,re.IGNORECASE)

    if match:
        root_name = match.group(1)
        current_num = match.group(3)
        ext = match.group(4)

        if current_num:
            next_num = int(current_num) + 1
        elif "_new" in base_name.lower():
            next_num = 2
        else:
            next_num = 1

    else:
        root_name, ext = os.path.splitext(base_name)
        next_num = 1

    clean_name = f"{root_name}{ext}"
    new_name = f"{root_name}_new{next_num}{ext}"

    icon_file_original = os.path.join(icon_dir, clean_name)
    icon_file_new = os.path.join(icon_dir, new_name)

    os.makedirs(icon_dir, exist_ok=True)

    log_callback(f"Limpando ícones antigos de {root_name}...")

    for f in os.listdir(icon_dir):
        try:
            file_root = re.sub(r"_new\d*","",os.path.splitext(f)[0],flags=re.IGNORECASE)

            if (
                file_root.lower() == root_name.lower()
                and f.lower().endswith(".ico")
            ):
                os.remove(os.path.join(icon_dir, f))

        except Exception:
            pass

    icon_url = (
        "https://cdn.cloudflare.steamstatic.com/"
        f"steamcommunity/public/images/apps/{gameid}/{clean_name}"
    )

    log_callback(f"Baixando: {clean_name}")

    if not download_file(icon_url, icon_file_original):
        log_callback(f"[ERRO DOWNLOAD] {clean_name}")
        return False

    if os.path.getsize(icon_file_original) < MIN_ICON_SIZE:
        try:
            os.remove(icon_file_original)
        except:
            pass

        log_callback(f"[INVALIDO] {clean_name}")
        return False

    try:
        os.rename(icon_file_original, icon_file_new)
    except Exception as e:
        log_callback(f"[ERRO RENOMEAR] {e}")
        return False

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith("IconFile="):
                    f.write(f"IconFile={icon_file_new}\n")
                else:
                    f.write(line)

        os.utime(file_path, None)

    except Exception as e:
        log_callback(f"[ERRO URL] {e}")
        return False

    log_callback(f"[OK] {new_name}")
    return True


def clear_icon_cache(log_callback):
    log_callback("Finalizando Explorer...")

    subprocess.call("taskkill /IM explorer.exe /F", shell=True)

    time.sleep(2)

    subprocess.call("ie4uinit.exe -ClearIconCache", shell=True)

    local = os.getenv("LOCALAPPDATA")
    explorer_path = os.path.join(local, "Microsoft\\Windows\\Explorer")

    if os.path.isdir(explorer_path):
        for f in os.listdir(explorer_path):
            if "iconcache" in f.lower():
                try:
                    os.remove(os.path.join(explorer_path, f))
                except:
                    pass

    log_callback("Cache limpo. Agora clique em 'Iniciar Explorer'.")


def start_explorer(log_callback):
    log_callback("Iniciando Explorer...")

    subprocess.Popen("explorer.exe", shell=True)

    time.sleep(2)

    check = subprocess.run(
        'tasklist | findstr explorer.exe',
        shell=True,
        capture_output=True,
        text=True
    )

    if "explorer.exe" in check.stdout.lower():
        log_callback("Explorer iniciado com sucesso!")
    else:
        log_callback("[ERRO] Explorer não iniciou")


class App:
    def __init__(self, root):
        self.root = root

        self.root.title(
            "Steam Icon Fixer 1.1 - phobosfreeware.blogspot.com"
        )

        self.root.geometry("600x450")

        self.queue = Queue()

        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="both", expand=True)

        self.btn_scan = ttk.Button(
            frame,
            text="🔍 Escanear Desktop",
            command=self.scan
        )
        self.btn_scan.pack(fill="x", pady=5)

        self.btn_fix = ttk.Button(
            frame,
            text="🛠 Corrigir Tudo",
            command=self.fix,
            state="disabled"
        )
        self.btn_fix.pack(fill="x", pady=5)

        self.btn_clear = ttk.Button(
            frame,
            text="🧹 Limpar Cache",
            command=self.clear_cache_ui,
            state="disabled"
        )
        self.btn_clear.pack(fill="x", pady=5)

        self.btn_explorer = ttk.Button(
            frame,
            text="📂 Iniciar Explorer",
            command=self.start_explorer_ui,
            state="disabled"
        )
        self.btn_explorer.pack(fill="x", pady=5)

        self.progress = ttk.Progressbar(frame)
        self.progress.pack(fill="x", pady=5)

        self.log = scrolledtext.ScrolledText(frame, height=15)
        self.log.pack(fill="both", expand=True)

        self.files = []

        self.process_queue()

    def log_msg(self, msg):
        self.queue.put(msg)

    def process_queue(self):
        while not self.queue.empty():
            item = self.queue.get()

            if isinstance(item, tuple) and item[0] == "progress":
                self.progress["value"] = item[1]
            else:
                self.log.insert(tk.END, item + "\n")
                self.log.see(tk.END)

        self.root.after(100, self.process_queue)

    def scan(self):
        self.log_msg("Escaneando Desktop...")

        self.files = find_steam_shortcuts()

        self.log_msg(f"Encontrados: {len(self.files)} atalhos")

        if self.files:
            self.btn_fix.config(state="normal")

    def fix(self):
        if not self.files:
            messagebox.showwarning(
                "Aviso",
                "Faça o scan primeiro"
            )
            return

        self.btn_fix.config(state="disabled")

        threading.Thread(
            target=self.run_fix,
            daemon=True
        ).start()

    def clear_cache_ui(self):
        self.btn_clear.config(state="disabled")

        threading.Thread(
            target=self.clear_cache_worker,
            daemon=True
        ).start()

    def clear_cache_worker(self):
        clear_icon_cache(self.log_msg)

        self.root.after(
            0,
            lambda: self.btn_explorer.config(state="normal")
        )

    def start_explorer_ui(self):
        self.btn_explorer.config(state="disabled")

        threading.Thread(
            target=self.start_explorer_worker,
            daemon=True
        ).start()

    def start_explorer_worker(self):
        start_explorer(self.log_msg)

        self.root.after(
            0,
            lambda: self.btn_scan.config(state="normal")
        )

    def run_fix(self):
        total = len(self.files)

        self.queue.put(("progress", 0))

        self.root.after(
            0,
            lambda: self.progress.configure(maximum=total)
        )

        alterou = False

        for i, file in enumerate(self.files):
            result = process_file(
                file,
                self.log_msg
            )

            if result:
                alterou = True

            self.queue.put(("progress", i + 1))

        if alterou:
            self.log_msg(
                "Correção concluída. Clique em 'Limpar Cache'."
            )

            self.root.after(
                0,
                lambda: self.btn_clear.config(state="normal")
            )
        else:
            self.log_msg("Nada para corrigir")

        self.log_msg("Finalizado!")

        self.root.after(
            0,
            lambda: messagebox.showinfo(
                "Finalizado",
                "Processo concluído!"
            )
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
