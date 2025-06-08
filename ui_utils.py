import gradio as gr

# Theme configuration
theme = gr.themes.Soft(
    primary_hue="purple",
    secondary_hue="pink",
    neutral_hue="slate",
    text_size=gr.themes.sizes.text_lg,
).set(
    body_background_fill="linear-gradient(135deg, #0f0c29, #24243e, #302b63)",
    body_background_fill_dark="linear-gradient(135deg, #0f0c29, #24243e, #302b63)",
    button_primary_background_fill="linear-gradient(90deg, #8a2be2, #ff6b6b)",
    button_primary_background_fill_hover="linear-gradient(90deg, #9b4dff, #ff8c8c)",
    button_primary_text_color="white",
    block_title_text_color="#8a2be2",
    input_background_fill="rgba(255, 255, 255, 0.05)",
    input_border_color="rgba(255, 255, 255, 0.1)",
)

# Custom CSS
custom_css = """
/* YOUR ENTIRE CSS AS IT IS */
"""

# Header
def make_header():
    return """
    <div class="main-header">
        <span class="music-note note-1">♪</span>
        <span class="music-note note-2">♫</span>
        <span class="music-note note-3">♬</span>
        <span class="music-note note-4">🎵</span>
        <h1>Mood-Based Music Generator</h1>
        <p>Create custom music that matches exactly how you feel</p>
    </div>
    """

# Loading animation
def make_generating_message():
    return """
    <div style="display:flex;justify-content:center;align-items:center;flex-direction:column;margin:2rem 0;">
        <div style="display:flex;gap:10px;margin-bottom:1rem;">
            <div class="dot" style="width:15px;height:15px;border-radius:50%;background:#8a2be2;animation:loadingDot 1.5s ease-in-out infinite;"></div>
            <div class="dot" style="width:15px;height:15px;border-radius:50%;background:#8a2be2;animation:loadingDot 1.5s ease-in-out 0.2s infinite;"></div>
            <div class="dot" style="width:15px;height:15px;border-radius:50%;background:#8a2be2;animation:loadingDot 1.5s ease-in-out 0.4s infinite;"></div>
        </div>
        <p style="color:#b3b3b3;">Creating your music experience, please wait...</p>
        <style>
            @keyframes loadingDot {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-15px); }
            }
        </style>
    </div>
    """

# Footer
def make_footer():
    return """
    <footer>
        Built with Gradio • © 2025 Mood Music Generator
    </footer>
    """

# Card container for layout blocks
def card_container(label):
    return gr.Column(elem_classes=["card-panel"], variant="panel")