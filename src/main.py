from audio_steganography import hide_data as hide_audio, reveal_data as reveal_audio
from image_steganography import hide_data as hide_image, reveal_data as reveal_image

def main():
    print("1. Ukryj dane w pliku audio")
    print("2. Odkryj ukryte dane z pliku audio")
    print("3. Ukryj dane w pliku obrazowym")
    print("4. Odkryj ukryte dane z pliku obrazowego")

    choice = int(input("Wybierz opcję: "))

    if choice == 1:
        audio_file = input("Podaj ścieżkę do pliku audio: ")
        data_to_hide = input("Podaj dane do ukrycia (ogranicz do jednego znaku lub kilku znaków): ")
        output_file = input("Podaj ścieżkę do pliku wyjściowego: ")
        hide_audio(audio_file, data_to_hide, output_file)
        print("Dane zostały pomyślnie ukryte!")

    elif choice == 2:
        audio_file = input("Podaj ścieżkę do pliku audio: ")
        print("Ukryte dane:", reveal_audio(audio_file))

    elif choice == 3:
        image_file = input("Podaj ścieżkę do pliku obrazowego: ")
        data_to_hide = input("Podaj dane do ukrycia: ")
        output_file = input("Podaj ścieżkę do pliku wyjściowego: ")
        hide_image(image_file, data_to_hide, output_file)
        print("Dane zostały pomyślnie ukryte!")

    elif choice == 4:
        image_file = input("Podaj ścieżkę do pliku obrazowego: ")
        print("Ukryte dane:", reveal_image(image_file))

    else:
        print("Nieprawidłowy wybór!")

if __name__ == "__main__":
    main()
