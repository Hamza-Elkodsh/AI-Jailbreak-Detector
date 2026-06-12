# 🛡️ AI Jailbreak Detector

A machine learning classifier that detects jailbreak attempts in LLM prompts.  
Built as a portfolio project showcasing NLP, text classification, and AI safety concepts.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)

---

## 🔍 What is a Jailbreak?

A **jailbreak** is a prompt crafted to bypass an AI's safety guidelines — for example, by using roleplay framing, instruction overrides, or hypothetical scenarios to trick the model into producing harmful content.

This project builds a binary classifier that labels prompts as:
- `0` — **Normal**: a legitimate user query
- `1` — **Jailbreak**: an attempt to override model safety

---

## 🗂️ Project Structure

```
ai-jailbreak-detector/
├── data/
│   ├── raw/              # Original downloaded datasets
│   └── processed/        # Cleaned, combined dataset (dataset.csv)
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation.ipynb
├── src/
│   ├── data_loader.py    # Download & combine datasets
│   ├── preprocessor.py   # Text cleaning & feature engineering
│   ├── classifier.py     # Model training
│   └── evaluate.py       # Metrics & visualizations
├── app/
│   ├── app.py            # Streamlit demo
│   └── utils.py          # Prediction helpers
├── models/               # Saved model artifacts
├── reports/figures/      # Generated charts
├── requirements.txt
└── README.md
```

---

## 🚀 Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-jailbreak-detector
cd ai-jailbreak-detector

# 2. Install dependencies
pip install -r requirements.txt

# 3. Build the dataset
python -m src.data_loader

# 4. Train the classifier
python -m src.classifier

# 5. Launch the demo app
streamlit run app/app.py
```

---

## 🧠 How It Works

### Data
- **Jailbreak prompts** from [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench)
- **Normal prompts** sampled from the [LMSYS ChatBot Arena](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) dataset

### Features
| Feature | Description |
|---|---|
| TF-IDF (1-2 grams) | Bag-of-words representation, 5000 features |
| `has_roleplay` | Detects "pretend", "act as", "DAN", etc. |
| `has_instruction_override` | Detects "ignore", "bypass", "override", etc. |
| `has_hypothetical` | Detects "hypothetically", "for a story", etc. |
| `char_count`, `word_count` | Prompt length features |

### Model
Logistic Regression with balanced class weights.  
Simple, interpretable, and effective for text classification.

---

## 📊 Results

| Metric | Score |
|---|---|
| Accuracy | ~XX% |
| F1 (Jailbreak) | ~XX% |
| ROC-AUC | ~XX |

*(Run the evaluation notebook to fill in your results)*

---

## 🔮 Future Work
- [ ] Fine-tune a BERT-based model for higher accuracy
- [ ] Add adversarial robustness testing
- [ ] Expand dataset with more jailbreak categories
- [ ] Add SHAP explainability to show why a prompt was flagged

---

## 📚 References
- [JailbreakBench](https://arxiv.org/abs/2404.01318) — Chao et al., 2024
- [LMSYS ChatBot Arena](https://huggingface.co/datasets/lmsys/lmsys-chat-1m)
- [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483)

---

## 👤 Author
**Hamza Mohamed Elkodsh** · [LinkedIn](https://www.linkedin.com/in/hamza-mohamed-01b124334/) · [GitHub](https://github.com/Hamza-Elkodsh?tab=repositories)
