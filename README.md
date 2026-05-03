# 🚀 Tech Ideas Hub

An automated blog that posts latest tech ideas daily.

## 🛠️ How it Works
1. **Generation:** A Python script (`main.py`) uses NVIDIA NIM (Llama 3.1) to generate a visionary tech idea.
2. **Formatting:** The idea is formatted into an HTML card and injected into `index.html`.
3. **Automation:** A GitHub Action (`.github/workflows/generate_idea.yml`) runs the script every day at midnight.

## 🌐 Live Blog
The blog is hosted on GitHub Pages: [https://iamgpreetsinghtablet.github.io/tech_ideas/](https://iamgpreetsinghtablet.github.io/tech_ideas/)

## ⚙️ Setup
To run this locally:
1. Clone the repo.
2. Set environment variables:
   ```bash
   export NVIDIA_API_KEY=your_key
   export GITHUB_TOKEN=your_token
   ```
3. Run the generator:
   ```bash
   python main.py
   ```
