# Add an absolute path to your download folder
DOWNLOAD_FOLDER_PATH = "/Users/ilaumnov/Downloads"

# Define folders where do you want to move files
image_folder_path = DOWNLOAD_FOLDER_PATH + "/images"
sheet_folder_path = DOWNLOAD_FOLDER_PATH + "/spreadsheets"
text_folder_path = DOWNLOAD_FOLDER_PATH + "/texts"
app_folder_path = DOWNLOAD_FOLDER_PATH + "/apps"
code_folder_path = DOWNLOAD_FOLDER_PATH + "/codes"
structured_folder_path = DOWNLOAD_FOLDER_PATH + "/structured docs"
video_folder_path = DOWNLOAD_FOLDER_PATH + "/videos"
pdf_folder_path = DOWNLOAD_FOLDER_PATH + "/pdfs"
htmls_folder_path = DOWNLOAD_FOLDER_PATH + "/htmls"
styles_folder_path = DOWNLOAD_FOLDER_PATH + "/styles"
archive_folder_path = DOWNLOAD_FOLDER_PATH + "/archives"
presentation_folder_path = DOWNLOAD_FOLDER_PATH + "/presentations"

# Define folder for files their's extension not in the map
OTHER_FOLDER_PATH = DOWNLOAD_FOLDER_PATH + "/others"

# Define which file move to which folder
EXTENSIONS_MAP = {
    # IMAGE extensions:START
    ".png": image_folder_path,
    ".jpeg": image_folder_path,
    ".jpg": image_folder_path,
    ".heic": image_folder_path,
    ".svg": image_folder_path,
    ".webp": image_folder_path,
    # IMAGE extensions:END
    # SPREADSHEET extensions:START
    ".xls": sheet_folder_path,
    ".xlsx": sheet_folder_path,
    ".xlsm": sheet_folder_path,
    ".csv": sheet_folder_path,
    ".xlsb": sheet_folder_path,
    ".ods": sheet_folder_path,
    ".numbers": sheet_folder_path,
    # SPREADSHEET extensions:END
    # TEXT extensions:START
    ".txt": text_folder_path,
    ".doc": text_folder_path,
    ".docx": text_folder_path,
    ".pages": text_folder_path,
    # TEXT extensions:END
    # APP extensions:START
    ".exe": app_folder_path,
    ".apk": app_folder_path,
    ".dmg": app_folder_path,
    # APP extensions:END
    # CODE extensions:START
    ".py": code_folder_path,
    ".ts": code_folder_path,
    ".js": code_folder_path,
    ".c": code_folder_path,
    ".cpp": code_folder_path,
    # CODE extensions:END
    # STRUCTURED extensions:START
    ".json": structured_folder_path,
    ".yaml": structured_folder_path,
    ".yml": structured_folder_path,
    ".xml": structured_folder_path,
    # STRUCTURED extensions:END
    # VIDEO extensions:START
    ".mp4": video_folder_path,
    ".mov": video_folder_path,
    # VIDEO extensions:END
    # PDF extensions:START
    ".pdf": pdf_folder_path,
    # PDF extensions:END
    # HTML extensions:START
    ".html": htmls_folder_path,
    # HTML extensions:END
    # STYLES extensions:START
    ".css": styles_folder_path,
    # STYLES extensions:END
    # ARCHIVE extensions:START
    ".zip": archive_folder_path,
    ".tar": archive_folder_path,
    # ARCHIVE extensions:END
    # PRESENTATION extensions:START
    ".ppt": presentation_folder_path,
    ".pptx": presentation_folder_path
    # PRESENTATION extensions:END
}
