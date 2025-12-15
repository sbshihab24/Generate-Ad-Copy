import os
from openai import OpenAI
import json

def get_openai_client():
    """Initializes and returns the OpenAI client securely."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API Key not found. Please set it in the .env file.")
    return OpenAI(api_key=api_key)

def generate_ad_copy(product_service, target_audience, key_benefits, tone):
    """
    Generates high-quality ad copy with strict tone adherence and richer descriptions.
    """
    client = get_openai_client()

    # --- ADVANCED PROMPT ENGINEERING ---
    # We give the AI specific instructions on how to handle different tones.
    
    tone_instructions = {
        "Professional": "Use formal, authoritative, and trust-building language. Focus on value, efficiency, and quality. No slang. Minimal emojis.",
        "Friendly": "Be conversational, warm, and relatable. Use 'You' and 'We'. It's okay to use 1-2 relevant emojis.",
        "Urgent": "Use short, punchy sentences. Focus on FOMO (Fear Of Missing Out), limited time, and immediate action.",
        "Luxury": "Use sophisticated, elegant vocabulary. Focus on exclusivity, premium quality, and status.",
        "Witty": "Be clever, playful, and humorous. Use puns or wordplay if appropriate for the product."
    }
    
    # Get the specific instruction for the selected tone, or default to professional
    selected_tone_instruction = tone_instructions.get(tone, tone_instructions["Professional"])

    system_prompt = f"""
    You are an elite Senior Marketing Copywriter with 10 years of experience.
    Your goal is to write high-converting Facebook and Instagram ad copy.
    
    STRICT TONE GUIDELINES:
    The user has selected the tone: '{tone}'.
    Instruction: {selected_tone_instruction}
    
    OUTPUT REQUIREMENTS:
    You must return a valid JSON object with these exact keys:
    
    1. "headline": A powerful hook. (Max 50 characters).
       - If Professional: Focus on the main result.
       - If Friendly: Focus on the feeling.
       
    2. "primary_text": The main body of the ad. (2-4 sentences, Max 300 characters).
       - Elaborate on the 'Key Benefits' provided.
       
    3. "description": A detailed and persuasive link description. (Max 150 characters).
       - Do NOT be short. Write 1-2 complete sentences.
       - Explain specifically *why* this offer is valuable or add social proof.
       - Example: "Join 10,000+ happy customers who have upgraded their style. Includes a 30-day money-back guarantee."
       
    4. "call_to_action": The best button choice (e.g., Learn More, Shop Now, Sign Up).
    """

    user_prompt = f"""
    Here are the product details. Write the ad copy now.
    
    Product/Service: {product_service}
    Target Audience: {target_audience}
    Key Benefits: {key_benefits}
    Tone: {tone}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Use gpt-4o or gpt-4-turbo for high quality. gpt-3.5 is too simple.
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.75 # Slightly higher creativity
        )
        
        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        return {"error": str(e)}