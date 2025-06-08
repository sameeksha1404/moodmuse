import gradio as gr
from backend import generate_music
from ui_utils import (
    theme,
    custom_css,
    make_header,
    make_footer,
    make_generating_message,
    card_container
)

moods = ["😊 Happy", "😢 Sad", "🌙 Calm", "⚡ Energetic"]

with gr.Blocks(theme=theme, css=custom_css) as demo:
    # Header
    gr.HTML(make_header())
    
    # Main Card
    with card_container("Design Your Music"):
        gr.HTML('<div class="card-header">Design Your Music Experience</div>')
        with gr.Group(elem_classes=["card-body"]):
            mood_input = gr.Radio(choices=moods, value="😊 Happy", label="", elem_classes=["radio-group"])
            music_type_input = gr.Radio(choices=["🎤 Riff", "🎹 Tune"], value="🎤 Riff", label="", elem_classes=["radio-group"])
            generate_btn = gr.Button("🎶 Generate My Music", elem_classes=["generate-btn"])
            status_message = gr.HTML(visible=False)
            with gr.Group(elem_classes=["output-panel"]):
                gr.Markdown("### Your Music")
                output_audio = gr.Audio(label="", type="filepath")
                download_btn = gr.Button("⬇ Download Your Track", visible=False)

    # Footer
    gr.HTML(make_footer())

    # Logic
    def on_generate_click(mood, music_type):
        yield gr.HTML.update(value=make_generating_message(), visible=True), gr.Audio.update(), gr.Button.update(visible=False)
        output_path = generate_music(mood, music_type)
        yield gr.HTML.update(visible=False), gr.Audio.update(value=output_path), gr.Button.update(visible=True)

    generate_btn.click(
        fn=on_generate_click,
        inputs=[mood_input, music_type_input],
        outputs=[status_message, output_audio, download_btn],
    )

demo.launch(debug=True)
if _name_ == "_main_":
    interface.launch(server_name="0.0.0.0", server_port=8080)