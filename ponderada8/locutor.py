import argparse
import whisper
from googletrans import Translator
from gtts import gTTS
import pygame

def main():
    # Configuração do ArgumentParser para entrada do usuário
    parser = argparse.ArgumentParser(description="Ferramenta de transcrição, tradução e síntese de áudio.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Caminho para o arquivo de áudio")
    parser.add_argument('-l', '--language', type=str, required=True, help="Código do idioma para tradução (e.g. 'en', 'pt', 'ja')")
    args = parser.parse_args()

    # Transcrição de áudio para texto
    model = whisper.load_model("base")
    result = model.transcribe(args.file)
    print("\nTexto Transcrito:\n", result["text"]) 
    
    # Tradução do texto
    print(f"Traduzindo para {args.language}...")
    translated_text = translate_text(result["text"], args.language)
    print("Tradução concluída.")
    print("\nTexto Traduzido:\n", translated_text) 

    # Conversão de texto para áudio
    tts_audio = text_to_speech(translated_text, args.language)
    play_audio(tts_audio)
   
def translate_text(text, language):
    translator = Translator()
    translation = translator.translate(text, dest=language)
    return translation.text

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    temp_file = "translated_audio.mp3"
    tts.save(temp_file)
    return temp_file

def play_audio(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    main()
