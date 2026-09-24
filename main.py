import sys
import os

def get_ffmpeg_path():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

os.environ["PATH"] += os.pathsep + get_ffmpeg_path()
import sys
import os
import secrets
import string
import psutil
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import yt_dlp
import subprocess

console = Console()

# --- 1. Swiss-Army Knife: Generatore Password ---
def password_generator():
    console.print("\n[bold cyan]--- GENERATORE PASSWORD SICURE ---[/bold cyan]")
    try:
        length = int(input("Lunghezza password (es. 16): ") or 16)
        alphabet = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        console.print(f"\nPassword Generata: [bold green]{pwd}[/bold green]\n")
    except ValueError:
        console.print("[red]Inserisci un numero valido.[/red]")

# --- 2. System Monitor: CPU & RAM ---
def system_monitor():
    console.print("\n[bold cyan]--- STATO SISTEMA ---[/bold cyan]")
    
    table = Table(title="Risorse Hardware")
    table.add_column("Risorsa", style="cyan", no_wrap=True)
    table.add_column("Valore", style="magenta")
    
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    
    table.add_row("Uso CPU", f"{cpu_usage}%")
    table.add_row("RAM Totale", f"{ram.total / (1024**3):.2f} GB")
    table.add_row("RAM Usata", f"{ram.used / (1024**3):.2f} GB ({ram.percent}%)")
    table.add_row("RAM Libera", f"{ram.available / (1024**3):.2f} GB")
    
    console.print(table)

# --- 3. Downloader Media Multi-Piattaforma ---
def media_downloader():
    console.print("\n[bold cyan]--- DOWNLOADER MEDIA MULTI-PIATTAFORMA ---[/bold cyan]")
    console.print("[white]Incolla un link da Spotify, YouTube, SoundCloud, Bandcamp, ecc.[/white]\n")
    
    url = input("Inserisci l'URL: ").strip()
    if not url:
        return

    if "spotify.com" in url:
        console.print("\n[yellow]Rilevato link Spotify. Download della traccia/playlist con metadati...[/yellow]")
        try:
            result = subprocess.run(["spotdl", url], capture_output=False, text=True)
            if result.returncode == 0:
                console.print("\n[bold green]Download e tagging Spotify completato con successo![/bold green]")
            else:
                console.print("\n[red]Si è verificato un errore durante il download da Spotify.[/red]")
        except FileNotFoundError:
            console.print("[red]Errore: 'spotdl' non trovato. Assicurati di aver fatto 'pip install spotdl'.[/red]")
        except Exception as e:
            console.print(f"[red]Errore: {e}[/red]")

    else:
        
        console.print("\n[yellow]Rilevato link generico (YouTube/SoundCloud/ecc.)...[/yellow]")
        console.print("1. Scarica Video")
        console.print("2. Scarica solo Audio (MP3)")
        scelta_fmt = input("Scegli formato (1/2): ").strip()

        if scelta_fmt == "2":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': False,
                'no_warnings': True,
            }
        else:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': False,
                'no_warnings': True,
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                console.print("[yellow]Scaricamento in corso...[/yellow]")
                ydl.download([url])
                console.print("[bold green]Download completato con successo![/bold green]")
        except Exception as e:
            console.print(f"[red]Errore durante il download: {e}[/red]")

## --- 4. Assistente AI (Gemini Cloud) ---
def ai_assistant():
    console.print("\n[bold cyan]--- ASSISTENTE AI (Powered by PhilipZ AI) ---[/bold cyan]")
    
    api_key = os.environ.get("GEMINI_API_KEY") or input("Inserisci la tua Gemini API Key: ").strip()
    
    if not api_key:
        console.print("[red]API Key non fornita.[/red]")
        return

    try:
        client = genai.Client(api_key=api_key)
        
        chat = client.chats.create(model='gemini-3.6-flash')
        
        console.print("[green]Chat avviata! Scrivi 'exit' o 'esci' per tornare al menu principale.[/green]\n")
        
        while True:
            prompt = input("Tu > ").strip()
            
            if prompt.lower() in ["exit", "esci"]:
                console.print("[yellow]Chiusura chat PhilipZ AI...[/yellow]")
                break
                
            if not prompt:
                continue

            console.print("[yellow]PhilipZ AI sta pensando...[/yellow]")
            response = chat.send_message(prompt)
            console.print(f"\n[bold green]PhilipZ AI:[/bold green] {response.text}\n")
            
    except Exception as e:
        console.print(f"[red]Errore: {e}[/red]")

# --- Menu Principale ---
def main():
    while True:
        console.clear()
        console.print(Panel.fit("[bold cyan]PhilipZ Tool v1.0[/bold cyan]\n[white]La tua suite personale da Terminale[/white]", title="PhilipZ CLI"))
        
        console.print("\n[bold yellow]Seleziona un modulo:[/bold yellow]")
        console.print("1. Generatore Password Sicure")
        console.print("2. Monitor CPU & Memoria RAM")
        console.print("3. Media Downloader (Video/Audio)")
        console.print("4. Assistente AI (Gemini)")
        console.print("5. Esci")
        
        scelta = input("\nPhilipZ> ").strip()
        
        if scelta == "1":
            password_generator()
        elif scelta == "2":
            system_monitor()
        elif scelta == "3":
            media_downloader()
        elif scelta == "4":
            ai_assistant()
        elif scelta == "5":
            console.print("[bold red]Arrivederci![/bold red]")
            sys.exit()
        else:
            console.print("[red]Opzione non valida.[/red]")
            
        input("\nPremi INVIO per tornare al menu...")

if __name__ == "__main__":
    main()