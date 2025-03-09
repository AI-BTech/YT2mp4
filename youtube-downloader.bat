@echo off
echo YouTube Channel Downloader
echo ========================
echo.
set /p channel=Enter channel name (without @): 
set videos_folder=%USERPROFILE%\Videos\%channel%
echo.
echo Creating folder: %videos_folder%
mkdir "%videos_folder%" 2>nul
echo.
echo Downloading 3 most recent videos from @%channel%...
echo.
"%~dp0yt-dlp.exe" -f 18 --playlist-end 3 "https://www.youtube.com/@%channel%/videos" -o "%videos_folder%\%%(upload_date)s_%%(title)s.%%(ext)s" --restrict-filenames
echo.
echo Done! Videos saved to: %videos_folder%
echo.
pause
