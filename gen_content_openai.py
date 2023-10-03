import openai

# Replace 'YOUR_API_KEY' with your actual API key from OpenAI
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to generate content using GPT-3
def generate_content(prompt, max_tokens=100):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the appropriate engine (e.g., text-davinci-002)
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,  # Number of responses to generate
        stop=None,  # Optional stop sequence to end the content generation
        temperature=0.7,  # Controls the randomness of the output (adjust as needed)
    )
    return response.choices[0].text.strip()


def gen_content(prompt):
    content = generate_content(prompt)
    return content

