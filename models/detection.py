import cv2
import pytesseract

# Funktion für die Nummernschild-Erkennung und Texterkennung (OCR)
def recognize_license_plate(frame):
    # Implementieren Sie die Objekterkennung und Texterkennung für Nummernschilder hier
    # ...

    return license_plate_text

# Hauptfunktion für das Lizenzschild-Erkennungssystem in Live-Videos
def main():
    video = cv2.VideoCapture(0)  # Zugriff auf die Kamera für Live-Video

    while True:
        ret, frame = video.read()  # Frame von der Kamera lesen

        # Lizenzschild erkennen und Text extrahieren
        license_plate_text = recognize_license_plate(frame)

        # Text auf dem Bild anzeigen
        cv2.putText(frame, f"License Plate: {license_plate_text}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Live-Video mit erkanntem Text anzeigen
        cv2.imshow('License Plate Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()