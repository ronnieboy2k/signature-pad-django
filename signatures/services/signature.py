import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def save_signature_image(encoded_data):
    filename = (
        BASE_DIR / "signatures" / "static" / "signatures" / "images" / "signature.png"
    )

    if encoded_data:
        encoded_data = encoded_data.split(",", 1)[1]
        image_data = base64.b64decode(encoded_data)

        with filename.open("wb") as file:
            file.write(image_data)
    elif filename.exists():
        filename.unlink()
