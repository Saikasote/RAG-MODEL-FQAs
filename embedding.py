import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load your FAQ dataset
df = pd.read_csv("FQAs_cleaned.csv")
questions = df["Question"].tolist()
answers = df["Answer"].tolist()

# Load a faster model
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

# Generate embeddings
embeddings = model.encode(questions, show_progress_bar=True)

# Save questions, answers, and embeddings to compressed .npz
np.savez_compressed("faq_data.npz", 
                    questions=questions, 
                    answers=answers, 
                    embeddings=embeddings)
print("✅ Embeddings saved to 'faq_data.npz'")
