import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from pytube import YouTube
from moviepy.editor import *
import os
import re
import threading

class MediaDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Downloader")
        self.root.geometry("500x300")
        self.root.config(bg="#f0f0f0")
        
        # Default download folder
        self.download_folder = os.path.expanduser("~")
        
        # Application title
        tk.Label(self.root, text="YouTube Media Downloader", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)
        
        # URL Entry
        tk.Label(self.root, text="Enter YouTube URL:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.url_entry = tk.Entry(self.root, width=60)
        self.url_entry.pack(pady=5)
        
        # Format Selection
        tk.Label(self.root, text="Select Format:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.format_var = tk.StringVar(value="mp4")
        tk.Radiobutton(self.root, text="MP4 (Video)", variable=self.format_var, value="mp4", bg="#f0f0f0").pack(anchor=tk.W, padx=180)
        tk.Radiobutton(self.root, text="MP3 (Audio)", variable=self.format_var, value="mp3", bg="#f0f0f0").pack(anchor=tk.W, padx=180)
        
        # Quality Selection
        tk.Label(self.root, text="Select Quality:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.quality_var = tk.StringVar(value="high")
        tk.Radiobutton(self.root, text="High Quality", variable=self.quality_var, value="high", bg="#f0f0f0").pack(anchor=tk.W, padx=180)
        tk.Radiobutton(self.root, text="Low Quality", variable=self.quality_var, value="low", bg="#f0f0f0").pack(anchor=tk.W, padx=180)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)
        
        # Download Button
        download_btn = tk.Button(self.root, text="Download", command=self.start_download_thread, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        download_btn.pack(pady=10)

        # Settings Menu
        menu_bar = tk.Menu(self.root)
        settings_menu = tk.Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Select Download Folder", command=self.set_download_folder)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)
        self.root.config(menu=menu_bar)
        
        # Status label
        self.status_label = tk.Label(self.root, text="", font=("Arial", 10), bg="#f0f0f0")
        self.status_label.pack(pady=5)
    
    def set_download_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.download_folder = folder_selected
            messagebox.showinfo("Download Folder", f"Download folder set to: {self.download_folder}")

    def start_download_thread(self):
        # Start download in a separate thread to avoid freezing the UI
        threading.Thread(target=self.download_media).start()

    def download_media(self):
        url = self.url_entry.get().strip()
        url = self.clean_youtube_url(url)
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return
        
        # Reset progress bar
        self.progress['value'] = 0
        self.status_label.config(text="Starting download...")

        try:
            yt = YouTube(url, on_progress_callback=self.update_progress)
            stream = None

            # Choose stream based on format and quality
            if self.format_var.get() == "mp4":
                stream = yt.streams.filter(file_extension="mp4").first() if self.quality_var.get() == "low" else yt.streams.get_highest_resolution()
            else:
                stream = yt.streams.filter(only_audio=True).first()

            # Downloading file
            self.status_label.config(text="Downloading...")
            out_file = stream.download(output_path=self.download_folder)
            
            # If MP3, convert the downloaded file
            if self.format_var.get() == "mp3":
                self.status_label.config(text="Converting to MP3...")
                self.convert_to_mp3(out_file)

            self.status_label.config(text="Download completed!")
            messagebox.showinfo("Success", f"Downloaded: {stream.title}")

        except Exception as e:
            self.status_label.config(text="Download failed!")
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def clean_youtube_url(self, url):
        match = re.search(r"(?:v=| \/)([0-9A-Za-z_-]{11}).*", url)
        if match:
            video_id = match.group(1)
            return f"httpts://www.youtube.com/watch?v={video_id}"
        return None

    def update_progress(self, stream, chunk, bytes_remaining):
        # Calculate and update progress bar
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress['value'] = percentage
        self.root.update_idletasks()
    
    def convert_to_mp3(self, file_path):
        base, ext = os.path.splitext(file_path)
        new_file = base + ".mp3"
        
        audio_clip = AudioFileClip(file_path)
        audio_clip.write_audiofile(new_file)
        audio_clip.close()
        os.remove(file_path)  # Delete the original mp4 file

# Run the application
root = tk.Tk()
app = MediaDownloaderApp(root)
root.mainloop()
