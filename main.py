import gradio as gr
from engine.ai_model import suggest_code_improvement
from engine.utils import apply_changes, get_diff
from engine.syntax_check import assess_code
import time

history = []  # Session memory for recent prompts

def generate_suggestion(code, prompt, fast_mode):
    start_time = time.time()
    quality_msg = assess_code(code)

    context = history[-2:] if len(history) >= 2 else history
    suggestion, explanation = suggest_code_improvement(code, prompt, context, fast_mode)

    history.append((code, prompt))
    final_time = time.time() - start_time
    stats = f"✅ Suggestion generated in {final_time:.2f}s using {'Fast Mode' if fast_mode else 'Full Mode'}"

    return quality_msg, suggestion, explanation, stats

def integrate_final_code(original, suggestion):
    final_code = apply_changes(original, suggestion)
    diff = get_diff(original, final_code)
    return final_code, diff

with gr.Blocks() as demo:
    gr.Markdown("# 🎮 Aicade Code Assistant (v2)")

    with gr.Row():
        code_input = gr.Textbox(lines=18, label="Paste Game Code")
        prompt_input = gr.Textbox(lines=3, label="What do you want to improve or change?")
        fast_mode = gr.Checkbox(label="⚡ Fast Mode (Quicker, Less Accurate Suggestions)", value=True)

    check_btn = gr.Button("💡 Suggest Improvement")
    quality_output = gr.Textbox(lines=2, label="Code Quality Check")
    suggestion_output = gr.Textbox(lines=15, label="AI Suggested Code")
    explanation_output = gr.Textbox(lines=4, label="Pixie's Explanation 🧚‍♀️")
    stats_output = gr.Textbox(lines=1, label="Model Stats")

    check_btn.click(
        generate_suggestion,
        inputs=[code_input, prompt_input, fast_mode],
        outputs=[quality_output, suggestion_output, explanation_output, stats_output]
    )

    integrate_btn = gr.Button("✅ Integrate Suggestion")
    final_output = gr.Textbox(lines=15, label="Final Integrated Code")
    diff_output = gr.Textbox(lines=10, label="Code Diff Summary")

    integrate_btn.click(
        integrate_final_code,
        inputs=[code_input, suggestion_output],
        outputs=[final_output, diff_output]
    )

demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
