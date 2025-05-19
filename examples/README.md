# Gradio Example

This folder contains a simple Gradio interface for `yt-dlp`.

The script `gradio_app.py` exposes a minimal web UI where you can
provide a video URL and optional `yt-dlp` options in JSON format.
The downloaded video will be returned as a file once processing
is complete.

Run the application with:

```bash
python examples/gradio_app.py
```

The same script can be used on services like Hugging Face Spaces
to provide an online downloader interface.
