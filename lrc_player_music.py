import time
import re
import pygame

def parse_lrc(file_path):
    pattern = re.compile(r"\[(\d+):(\d+\.\d+)\](.*)")
    lyrics = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = pattern.match(line)
            if match:
                minutes = int(match.group(1))
                seconds = float(match.group(2))
                text = match.group(3).strip()
                total_time = minutes * 60 + seconds
                lyrics.append((total_time, text))

    return lyrics


def play_lyrics(lyrics):
    start_time = time.time()

    for t, line in lyrics:
        while time.time() - start_time < t:
            time.sleep(0.01)
        print(line)


# 🎵 Inicializar audio
pygame.mixer.init()
pygame.mixer.music.load("es_por_ti.mp3")
pygame.mixer.music.play()

lyrics = parse_lrc("juanesEsPorTi.lrc")
play_lyrics(lyrics)