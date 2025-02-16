#!usr/bin/env python3
# Downloader Instagram Reels
# Copyright by © WahyuDin Ambia
# Created 16 February 2025

# <--- import library --->
import requests
import os, random, sys
import time, datetime
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from rich import print as dawg
from rich.panel import Panel as cuy
from rich.columns import Columns as bro
from rich.tree import Tree as dalan
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
console = Console()
sys.stdout.write('\x1b]2; InstaLoader | WahyuXD Downloader Reels/Post Instagram \x07')

# <--- Waktu --->
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

# <---  Warna  --->
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

# <!--  Warna 2  -->
Z2 = "[#FF0505]" # HITAM
mera  = "[#F00000]"
M2 = "[#AAAAAA]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00E2F5]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
M2, H2, K2, P2, B2, U2, O2 = ["[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#FFFFFF]", "[#00C8FF]", "[#AF00FF]", "[#00FFFF]"]
acak = [M2, H2, K2, B2, U2, O2, P2]
warna = random.choice(acak)
til =f"{mera}● {K2}● {H2}●"
ken = f'{mera}›{K2}›{H2}› '
tod = f' {H2}‹{K2}‹{mera}‹'

# <--- API KEY --->
API_KEY = "23a4534fd6msh5c0ad3449f0d1c5p131c5ejsn475c38969b4f"

# <--- Logo --->
def logo_menu():
  banner = f''' {til}                                                     {H2}Version 1.0
        {warna}____           __        __                    __         
       /  _/___  _____/ /_____ _/ /   ____  ____ _____/ /__  _____
       / // __ \/ ___/ __/ __ `/ /   / __ \/ __ `/ __  / _ \/ ___/
     _/ // / / (__  ) /_/ /_/ / /___/ /_/ / /_/ / /_/ /  __/ /    
    /___/_/ /_/____/\__/\__,_/_____/\____/\__,_/\__,_/\___/_/ 
    
        {P2}[italic]Free Tools Instagram Downloader Post / Video Reels [/italic]
  '''
  dawg(cuy(banner,title=f'{ken}{A2}{hari}, {tanggal}{tod}',subtitle_align='left',width=75,padding=(0),style='#AAAAAA'))


# <--- Ambil Video --->
def jikot_pidio(link_dawg):
    url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/get-info-rapidapi"
    format_link = {"url": link_dawg}
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=format_link)
    if response.status_code != 200:
        dawg("[bold red]❌ Gagal mengambil data dari API![/bold red]")
        return None
    data = response.json()
    dess = cuy.fit(f'{P2}📩 Response JSON',style="#AAAAAA")
    ress = cuy.fit(f"[bold cyan]{data}[/bold cyan]",style="#AAAAAA")
    apalahh = dalan(dess, guide_style="bold #AAAAAA")
    apalahh.add(ress)
    console.print(apalahh)

    if "download_url" in data:
        return data["download_url"]
    else:
        dawg(cuy.fit(f"{P2}❌ Video tidak ditemukan dalam response JSON!",style="#AAAAAA"))
        return None

# <--- Donlot Dawg --->
def donlot(link_pidio, simpen, filename="insta_video_wahyuxd.mp4"):
    if not os.path.exists(simpen):
        os.makedirs(simpen)
    full_path = os.path.join(simpen, filename)
    with requests.get(link_pidio, stream=True) as response:
        if response.status_code == 200:
            total_size = int(response.headers.get("content-length", 0))
            chunk_size = 1024
            
            with open(full_path, "wb") as f, Progress(
                SpinnerColumn(),
                TextColumn("[bold cyan]⬇ Downloading...[/bold cyan]"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            ) as progress:
                task = progress.add_task("Download", total=total_size)
                
                for chunk in response.iter_content(chunk_size):
                    if chunk:
                        f.write(chunk)
                        progress.update(task, advance=len(chunk))
                        time.sleep(0.01)
            
            dawg(cuy.fit(f"{P2}✅ Download sukses! Video disimpan di: {B2}{full_path}",style="#AAAAAA"))
        else:
            dawg("[bold red]❌ Gagal download video![/bold red]")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    logo_menu()
    dawg(cuy.fit(f'{P2}Masukkan link Instagram publik{A2}',subtitle=f'{A2}╭─{ken}{P2}(Reels/Post){tod}',subtitle_align='left',style='#AAAAAA'))
    link_dawg = input(f"{A}   ╰─> {H}")
    dawg(cuy.fit(f'{P2}Masukkan folder penyimpan video{A2}',subtitle=f'{A2}╭─{ken}{P2}Penyimpanan{tod}',subtitle_align='left',style='#AAAAAA'))
    simpen = input(f"{A}   ╰─> {H}")
    dawg(cuy.fit(f'{P2}Masukkan nama file video (Bebas){A2}',subtitle=f'{A2}╭─{ken}{P2}Tanpa .mp4{tod}',subtitle_align='left',style='#AAAAAA'))
    aran_file = input(f"{A}   ╰─> {H}").strip()
    if not aran_file.lower().endswith(".mp4"):
        aran_file += ".mp4"
    link_pidio = jikot_pidio(link_dawg)
    if link_pidio:
        des = cuy.fit(f'{P2}🔗 Link video',style="#AAAAAA")
        res = cuy.fit(f"[bold yellow]{link_pidio}[/bold yellow]",style="#AAAAAA")
        apalah = dalan(des, guide_style="bold #AAAAAA")
        apalah.add(res)
        console.print(apalah)
        print("")
        
        donlot(link_pidio, simpen, aran_file)