from flask import Flask, request, render_template, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():

    url = request.form['url']
    quality = request.form['quality']

    ydl_opts = {
        'format': f'bestvideo[height<={quality}]+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': 'video.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)