import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from utils.system_prompt import SYSTEM_PROMPT
from functions.call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot using Gemini API")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        types.Content(role="user",parts=[types.Part(text=args.user_prompt)])
    ]

    max_iters = 20
    for i in range(0, max_iters):
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0,
                tools=[available_functions]
            )
        )

        if response is None or response.usage_metadata is None:
            return 
        
        if(args.verbose):
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)
        
        if response.function_calls:
            for function_call_part in response.function_calls:
        
                try:
                    function_call_result = call_function(function_call_part, args.verbose)
                    # Validate non-empty parts
                    if not function_call_result.parts:
                        raise ValueError(
                            "Function returned a Content object with empty parts"
                        )
                    if function_call_result.parts[0].function_response is None:
                        raise ValueError("Error during function call: response is not a a FunctionResponse object")
                    if function_call_result.parts[0].function_response.response is None:
                        raise ValueError("Error during function call: empty response")
                        
                    messages.append(function_call_result)

                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                    
                    
                except Exception as e:
                    print(f"Error on call function: {e}")
        else:
            # final agent text response
            print(response.text)
            print(f'final response: {response.text}')
            return
   

main()
