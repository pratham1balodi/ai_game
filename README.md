# ai_game

An intelligent, local-first AI Code Assistant built specifically for **game developers**.  
It helps you iterate, debug, and improve code with speed and context awareness — powered by an open-source LLM and a clean, developer-first UI.

> Built for Aicade's AI Engineer Challenge  
> Designed and developed by **Pratham Balodi**

---

## 🚀 What It Does

✅ Accepts raw game code (e.g., player movement, object updates)  
✅ Accepts a natural-language prompt for the improvement you want  
✅ Returns an optimized or modified version of the code  
✅ Explains changes clearly in human-readable language  
✅ Shows a side-by-side diff before integrating suggestions  
✅ Optional "Fast Mode" to trade depth for speed  
✅ Runs entirely offline (no paid APIs, no OpenAI calls)  
✅ Supports Google Colab + GPU acceleration

---

## 💡 Why It’s Different

- **Smart AI + UX**: It doesn’t just complete code — it *thinks about your goal*  
- **Friendly Explanation**: Meet "Pixie" — your code reviewer with attitude  
- **Real-world Integration**: Applies suggestions directly into existing code  
- **Performance Optimized**: Handles both CPU and GPU, with Fast Mode for demos  
- **Developer Experience**: Diff tools, syntax validation, memory-aware context

---

## 🧪 Demo It Yourself

Paste this code into the UI:

```python
def move_player(x, y, dx, dy):
    return x + dx, y + dy
