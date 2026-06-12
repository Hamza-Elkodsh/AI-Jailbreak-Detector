from datasets import load_dataset

ds = load_dataset('OpenAssistant/oasst1', split='train[:500]') 

# Extract just the user messages
import pandas as pd
df = pd.DataFrame(ds)
df = df[df['role'] == 'prompter'][['text']].rename(columns={'text': 'prompt'})
df['label'] = 0  # 0 = normal
df.to_csv('data/raw/normal_prompts.csv', index=False)
print(f'Done! Saved {len(df)} normal prompts.')

