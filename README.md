This project implements a context-aware generative Question Answering (QA) system using a pre-trained FLAN-T5 transformer model from Hugging Face.
Unlike extractive QA systems that rely on span matching, this system generates answers in natural language, making it more robust to informal text, multi-sentence reasoning, and “why” questions.

The model reads a user-provided context and produces answers with explanation, closely resembling the behavior of modern conversational AI systems.

⚙️ Key Features

Uses FLAN-T5 (instruction-tuned transformer) for generative reasoning

Accepts multi-line contextual input

Handles why / who / comparative questions

Produces full-sentence answers with reasoning

Runs locally using Hugging Face Transformers (no API keys required)

🧠 How It Works

User provides a text context (multiple lines supported)

User asks a question based on that context

The system constructs an instruction-based prompt

FLAN-T5 generates a reasoned natural language answer

🚀 Example

Context

Ravi worked hard and got a good job. Neha later started her own business and became successful.
However, Ravi lost his job and is currently unemployed.


Question

Who is more successful now and why?


Answer

Neha is more successful now because she started her own business and became successful, while Ravi is currently unemployed.

🧩 Why Generative QA?

Traditional extractive QA systems often fail on:

informal text

multi-sentence reasoning

“why” questions

subject–predicate ambiguity

This project demonstrates how generative transformers overcome these limitations by reasoning over the full context instead of selecting text spans.

🛠️ Tech Stack

Python

Hugging Face Transformers

FLAN-T5 (google/flan-t5-base)

📚 Learning Outcomes

Understanding the difference between extractive vs generative QA

Prompt engineering for reasoning-based answers

Practical use of instruction-tuned transformer models

Building explainable NLP systems
