from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

print("Enter context. Type END to finish:")
context_lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    context_lines.append(line)

context = " ".join(context_lines)

question = input("\nEnter your question: ").strip()

prompt = f"""
You are an intelligent assistant.
Read the context carefully and answer the question with reasoning.

Context:
{context}

Question:
{question}

Answer in full sentences and explain the reasoning clearly.
"""

result = generator(
    prompt,
    max_length=128,
    do_sample=False
)

print("\nAnswer:")
print(result[0]["generated_text"].strip())
