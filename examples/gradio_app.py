#!/usr/bin/env python3
from __future__ import annotations
'''Simple Gradio interface for yt-dlp.

This script provides a basic web UI using Gradio to download
videos using yt-dlp. Provide a video URL and optional yt-dlp
options in JSON format. The downloaded file will be returned
for download.
'''

import json
import os
import tempfile

import gradio as gr
from yt_dlp import YoutubeDL


def download_video(url: str, options_json: str | None = None) -> str:
    """Download video using yt-dlp and return the file path."""
    ydl_opts = {'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s')}

    if options_json:
        try:
            ydl_opts.update(json.loads(options_json))
        except json.JSONDecodeError as err:
            raise gr.Error(f'Invalid options JSON: {err}')

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        if 'requested_downloads' in info:
            file_path = info['requested_downloads'][0]['filepath']
        else:
            file_path = ydl.prepare_filename(info)
    return file_path


def main() -> None:
    gr.Interface(
        fn=download_video,
        inputs=[
            gr.Textbox(label='Video URL'),
            gr.Textbox(label='yt-dlp options (JSON)', value='{}'),
        ],
        outputs=gr.File(label='Downloaded file'),
        title='yt-dlp Gradio Downloader',
        description=(
            'Minimal web interface to run yt-dlp. '
            'Enter a video URL and optional options in JSON format.'
        ),
    ).launch()


if __name__ == '__main__':
    main()
