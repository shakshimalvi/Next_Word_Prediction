# 🔮 Next Word Prediction using LSTM

A deep learning-based **Next Word Prediction** application that predicts the most likely words following a given text sequence. The project uses **Natural Language Processing (NLP)** and **LSTM (Long Short-Term Memory)** networks and is deployed as an interactive **Streamlit web application**.

## 🚀 Live Demo

👉 **[Try the Live App] https://nextwordprediction-zv6nmmyeoyz9wqq5jdkfcj.streamlit.a**

## 📌 Project Overview

Next Word Prediction is an NLP task where a model learns patterns from previously seen text and predicts the next word based on the given context.

In this project, a text corpus was processed and converted into fixed-length sequences. Two recurrent neural network approaches were explored:

* SimpleRNN — baseline model
* LSTM — final model

The trained LSTM model is integrated into a Streamlit application where users can enter text and receive:

* Top 5 predicted next words
* Prediction probabilities
* Automatically generated continuation text

---

## 🎯 Objectives

* Understand text preprocessing for NLP
* Convert text into numerical sequences
* Build a next-word prediction dataset
* Implement a SimpleRNN baseline
* Implement an LSTM model
* Compare model performance
* Generate next-word predictions
* Build an interactive Streamlit application
* Deploy the model as a web application

---

## 🏗️ Project Architecture

```text
                    Text Dataset
                         │
                         ▼
                Text Preprocessing
                         │
                         ▼
                     Tokenization
                         │
                         ▼
              Fixed-Length Sequences
                         │
                         ▼
                  Train / Test Split
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
          SimpleRNN                LSTM
          Baseline              Final Model
              │                     │
              └──────────┬──────────┘
                         ▼
                  Model Evaluation
                         │
                         ▼
              next_word_lstm.keras
                         │
                         ▼
                  Streamlit App
                         │
                         ▼
                 User Input Text
                         │
                         ▼
             Top-5 Word Predictions
                         │
                         ▼
                  Text Generation
```

---

## 📂 Project Structure

```text
Next_Word_Prediction/
│
├── app.py
├── next_word_lstm.keras
├── tokenizer.pkl
├── requirements.txt
├── dataset.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── prediction.png
    ├── generation.png
    └── app.png
```

---

## 📊 Dataset & Preprocessing

The project uses a text (`.txt`) corpus as the training data.

### Preprocessing steps

1. Convert text to lowercase
2. Remove unwanted characters
3. Normalize whitespace
4. Tokenize the text
5. Convert words into integer IDs
6. Create fixed-length sequences
7. Separate input sequences and target words
8. Split the data into training and testing sets

### Dataset statistics

| Parameter             |    Value |
| --------------------- | -------: |
| Total sequences       |  109,137 |
| Input sequence length | 10 words |
| Vocabulary size       |    8,153 |
| Training samples      |   87,309 |
| Testing samples       |   21,828 |

Each training example contains:

```text
10 input words → 1 target word
```

For example:

```text
Input:
machine learning is very

Target:
useful
```

---

## 🧠 Models Used

### 1. SimpleRNN

A SimpleRNN model was first implemented as a baseline.

```text
Input
  ↓
Embedding
  ↓
SimpleRNN
  ↓
Dense + Softmax
  ↓
Next Word
```

### 2. LSTM

The final model uses an LSTM network because LSTM networks are designed to retain information across sequences and can model longer-term dependencies better than a basic recurrent layer.

```text
Input
  ↓
Embedding
  ↓
LSTM
  ↓
Dropout
  ↓
Dense + Softmax
  ↓
Next Word
```

### LSTM Configuration

| Parameter             |                           Value |
| --------------------- | ------------------------------: |
| Input sequence length |                              10 |
| Embedding dimension   |                             100 |
| LSTM units            |                             128 |
| Dropout               |                             0.2 |
| Output layer          |                           Dense |
| Activation            |                         Softmax |
| Optimizer             |                            Adam |
| Loss                  | Sparse Categorical Crossentropy |
| Batch size            |                              64 |
| Maximum epochs        |                              10 |

Early stopping was used during training to prevent unnecessary training after validation performance stopped improving.

---

## 📈 Model Results

The SimpleRNN model was used as the baseline and compared with the LSTM model.

| Model     | Validation Accuracy |
| --------- | ------------------: |
| SimpleRNN |              13.52% |
| LSTM      |             ~13.81% |

The LSTM provided a modest improvement over the SimpleRNN baseline on this dataset.

> **Note:** Next-word prediction is a difficult multi-class NLP problem because the model must choose among thousands of vocabulary words. The validation accuracy should therefore be interpreted in the context of the vocabulary size and dataset.

---

## 🔮 Prediction

The application accepts a user-provided text sequence and returns the most probable next words.

### Example

**Input:**

```text
machine learning is
```

**Prediction:**

```text
1. a
2. ...
3. ...
4. ...
5. ...
```

The application also displays the prediction probability for each suggested word.

---

## ✍️ Text Generation

The application can generate multiple words sequentially.

For example:

```text
Input:
machine learning

Generated text:
machine learning and the door had been
```

The model predicts one word at a time and feeds the predicted word back into the input sequence to generate the next word.

---

## 🖥️ Streamlit Application

The project is deployed using **Streamlit**.

The application provides:

* Text input
* Top-5 predictions
* Prediction probabilities
* Text generation
* Adjustable number of generated words
* Interactive user interface

### Application Screenshot

Add your screenshot here:

```text
screenshots/app.png
```

<img width="1150" height="837" alt="Screenshot 2026-09-27 200417" src="https://github.com/user-attachments/assets/876e65c1-9782-47a3-ab49-bc089ed519b0" />

### Prediction Screenshot

```text
screenshots/prediction.png
```

<img width="515" height="752" alt="Screenshot 2026-09-27 190604" src="https://github.com/user-attachments/assets/5b15e7e7-31f6-4335-b42f-46ee853d87b0" />

### Text Generation Screenshot

```text
screenshots/generation.png
```

<img width="1001" height="380" alt="Screenshot 2026-09-27 200511" src="https://github.com/user-attachments/assets/b65f83ae-977f-4c47-9deb-7595397396ea" />

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Scikit-learn
* Streamlit
* NLP
* LSTM
* SimpleRNN
* Git & GitHub

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/shakshimalvi/Next_Word_Prediction.git
```

Navigate to the project:

```bash
cd Next_Word_Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📋 Requirements

```text
streamlit
tensorflow==2.18.0
numpy<2
pandas
```

---

## 🔄 How the Application Works

```text
User enters text
       ↓
Tokenizer converts words to IDs
       ↓
Last 10 tokens are selected
       ↓
Sequence is padded
       ↓
LSTM model predicts vocabulary probabilities
       ↓
Top 5 words are selected
       ↓
Predictions displayed to user
```

For text generation, the predicted word is added to the input and the process is repeated.

---

## 📚 Key Learning Outcomes

Through this project, I practiced:

* NLP text preprocessing
* Tokenization
* Sequence generation
* Padding
* Vocabulary creation
* Word-to-index mapping
* Embedding layers
* Recurrent Neural Networks
* LSTM networks
* Model evaluation
* Early stopping
* Probability-based prediction
* Sequential text generation
* Model serialization
* Streamlit deployment
* Git and GitHub workflow

---

## 🔮 Future Improvements

Possible improvements include:

* Train on a larger and more diverse corpus
* Increase context length
* Experiment with Bidirectional LSTM
* Implement GRU
* Use pretrained language models
* Add temperature-based sampling
* Add top-k and top-p sampling
* Improve text-generation quality
* Evaluate using Top-K Accuracy and Perplexity
* Experiment with Transformer-based architectures

---

## 🌐 Links

**GitHub Repository:**
https://github.com/shakshimalvi/Next_Word_Prediction

**Live Demo:**
https://nextwordprediction-zv6nmmyeoyz9wqq5jdkfcj.streamlit.a
---

## 👩‍💻 Author

### Shakshi Malvi

B.Tech Computer Science & Engineering Student
Aspiring ML Engineer | Data Science & NLP Enthusiast

**GitHub:**
https://github.com/shakshimalvi

**LinkedIn:**
https://www.linkedin.com/in/shakshi-malvi/

---

