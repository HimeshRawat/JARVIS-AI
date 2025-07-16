from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="openai/gpt-4o-mini-search-preview",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)



#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