import streamlit as st
import numpy as np
import pickle

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Next Word Prediction",
    page_icon="🔮",
    layout="centered"
)


# =========================================================
# Load Model and Tokenizer
# =========================================================

@st.cache_resource
def load_resources():

    model = load_model("next_word_lstm.keras")

    with open("tokenizer.pkl", "rb") as file:
        tokenizer = pickle.load(file)

    return model, tokenizer


model, tokenizer = load_resources()

MAX_SEQUENCE_LENGTH = 10


# =========================================================
# Predict Top Words
# =========================================================

def predict_top_words(seed_text, top_n=5):

    token_list = tokenizer.texts_to_sequences(
        [seed_text.lower()]
    )[0]

    if not token_list:
        return []

    # Keep last 10 words
    token_list = token_list[-MAX_SEQUENCE_LENGTH:]

    # Padding
    token_list = pad_sequences(
        [token_list],
        maxlen=MAX_SEQUENCE_LENGTH,
        padding="pre"
    )

    # Prediction
    probabilities = model.predict(
        token_list,
        verbose=0
    )[0]

    # Top N predictions
    top_indices = np.argsort(
        probabilities
    )[-top_n:][::-1]

    results = []

    for word_id in top_indices:

        word = tokenizer.index_word.get(
            word_id,
            ""
        )
        probability = float(probabilities[word_id] * 100)

        if word:
            results.append(
                (word, probability)
            )

    return results


# =========================================================
# Generate Multiple Words
# =========================================================

def generate_text(seed_text, next_words=5):

    generated_text = seed_text

    for _ in range(next_words):

        predictions = predict_top_words(
            generated_text,
            top_n=1
        )

        if not predictions:
            break

        next_word = predictions[0][0]

        generated_text += " " + next_word

    return generated_text


# =========================================================
# Streamlit UI
# =========================================================

st.title("🔮 Next Word Prediction")

st.write(
    "Enter a sentence and let the LSTM model "
    "predict the most likely next words."
)

st.divider()


# =========================================================
# User Input
# =========================================================

user_input = st.text_input(
    "Enter your text:",
    placeholder="Example: machine learning is"
)


# =========================================================
# Prediction Button
# =========================================================

if st.button("🔍 Predict Next Word"):

    if not user_input.strip():

        st.warning(
            "Please enter some text first."
        )

    else:

        predictions = predict_top_words(
            user_input,
            top_n=5
        )

        if predictions:

            st.subheader("Top 5 Predictions")

            for i, (word, probability) in enumerate(
                predictions,
                start=1
            ):

                st.write(
                    f"**{i}. {word}** — "
                    f"{probability:.2f}%"
                )

                st.progress(
                    float(min(probability / 100, 1.0))
                    )
        else:

            st.error(
                "The entered words were not found "
                "in the model vocabulary."
            )


# =========================================================
# Generate Text
# =========================================================

st.divider()

st.subheader("✍️ Generate Text")

number_of_words = st.slider(
    "Number of words to generate:",
    min_value=1,
    max_value=10,
    value=5
)


if st.button("✨ Generate"):

    if not user_input.strip():

        st.warning(
            "Please enter some starting text."
        )

    else:

        generated = generate_text(
            user_input,
            number_of_words
        )

        st.success(generated)


# =========================================================
# Model Information
# =========================================================

st.divider()

st.caption(
    "Model: LSTM | Context Length: 10 words | "
    "Vocabulary: 8,153 words"
)