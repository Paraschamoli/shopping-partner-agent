# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""shopping-partner-agent - An Bindu Agent."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import traceback
from pathlib import Path
from textwrap import dedent
from typing import Any

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.openrouter import OpenRouter
from agno.tools.mem0 import Mem0Tools
from agno.tools.exa import ExaTools
from agno.tools.duckduckgo import DuckDuckGoTools
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Global agent instance
agent: Agent | None = None
_initialized = False
_init_lock = asyncio.Lock()


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Try multiple possible locations for agent_config.json
    possible_paths = [
        Path(__file__).parent.parent / "agent_config.json",  # Project root
        Path(__file__).parent / "agent_config.json",  # Same directory
        Path.cwd() / "agent_config.json",  # Current working directory
    ]

    for config_path in possible_paths:
        if config_path.exists():
            try:
                with open(config_path) as f:
                    return json.load(f)
            except (PermissionError, json.JSONDecodeError) as e:
                print(f"⚠️  Error reading {config_path}: {type(e).__name__}")
                continue
            except Exception as e:
                print(f"⚠️  Unexpected error reading {config_path}: {type(e).__name__}")
                continue

    # If no config found or readable, create a minimal default
    print("⚠️  No agent_config.json found, using default configuration")
    return {
        "name": "shopping-partner-agent",
        "description": "AI-powered product recommendation system that helps users find the perfect products based on their specific preferences and requirements",
        "version": "1.0.0",
        "deployment": {
            "url": "http://127.0.0.1:3773",
            "expose": True,
            "protocol_version": "1.0.0",
            "proxy_urls": ["127.0.0.1"],
            "cors_origins": ["*"],
        },
        "environment_variables": [
            {"key": "OPENAI_API_KEY", "description": "OpenAI API key for LLM calls", "required": False},
            {"key": "OPENROUTER_API_KEY", "description": "OpenRouter API key for LLM calls", "required": False},
            {"key": "EXA_API_KEY", "description": "Exa API key for search operations", "required": False},
            {"key": "MEM0_API_KEY", "description": "Mem0 API key for memory operations", "required": False},
        ],
    }


async def initialize_agent() -> None:
    """Initialize the shopping partner agent with proper model and tools."""
    global agent

    # Get API keys from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    exa_api_key = os.getenv("EXA_API_KEY")
    mem0_api_key = os.getenv("MEM0_API_KEY")
    model_name = os.getenv("MODEL_NAME", "openai/gpt-4o")

    # Model selection logic
    if openai_api_key:
        model = OpenAIChat(id="gpt-4o", api_key=openai_api_key)
        print("✅ Using OpenAI GPT-4o")
    elif openrouter_api_key:
        model = OpenRouter(
            id=model_name,
            api_key=openrouter_api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        )
        print(f"✅ Using OpenRouter model: {model_name}")
    else:
        error_msg = (
            "No API key provided. Set OPENAI_API_KEY or OPENROUTER_API_KEY environment variable.\n"
            "For OpenRouter: https://openrouter.ai/keys\n"
            "For OpenAI: https://platform.openai.com/api-keys"
        )
        raise ValueError(error_msg)

    # Initialize tools
    tools = []
    
    # Add search tools based on available APIs
    if exa_api_key:
        exa_tools = ExaTools(api_key=exa_api_key)
        tools.append(exa_tools)
        print("✅ Added Exa search tools")
    else:
        # Fallback to DuckDuckGo if Exa not available
        duckduckgo_tools = DuckDuckGoTools()
        tools.append(duckduckgo_tools)
        print("✅ Added DuckDuckGo search tools (EXA_API_KEY not set)")
    
    # Add Mem0 if available
    if mem0_api_key:
        mem0_tools = Mem0Tools(api_key=mem0_api_key)
        tools.append(mem0_tools)
        print("✅ Added Mem0 memory tools")
    else:
        print("⚠️  MEM0_API_KEY not set - memory features disabled")

    # Create the shopping partner agent
    agent = Agent(
        name="Shopping Partner",
        model=model,
        tools=tools,
        description=dedent("""\
            You are an AI-powered product recommendation system that helps users find 
            the perfect products based on their specific preferences and requirements.
            Your expertise encompasses: 🛍️

            - Smart product matching with minimum 50% match rate guarantee
            - Trusted source verification from authentic e-commerce platforms
            - Real-time availability and stock checking
            - Quality assurance to avoid counterfeit products
            - Detailed product information and comparison
            - User-friendly presentation and formatting
        """),
        instructions=dedent("""\
            **SHOPPING PARTNER PROTOCOL:**
            
            1. **Requirement Analysis**: Carefully analyze all user preferences and requirements
            2. **Trusted Source Search**: Search only authentic e-commerce platforms:
               - Amazon, Flipkart, Myntra, Meesho, Google Shopping, Nike
               - Other reputable and verified websites
               - NO counterfeit or unverified sources
            3. **Match Assessment**: Ensure products match at least 50% of user requirements
               - Prioritize higher match percentages when possible
               - Be transparent about match levels
            4. **Availability Verification**: Confirm products are in stock and available
               - Check current availability status
               - Note any delivery or shipping constraints
            5. **Information Presentation**: Provide comprehensive product details:
               - Price (with currency)
               - Brand and manufacturer
               - Key features and specifications
               - Product ratings and reviews when available
               - Purchase links from trusted sources
            
            **SEARCH PRIORITIES:**
            - Safety and authenticity first
            - Match percentage (minimum 50%)
            - Price within budget constraints
            - Availability and delivery options
            - User preference alignment
            
            **FORMATTING STANDARDS:**
            - Clear headings and product categories
            - Bullet points for easy scanning
            - Consistent price formatting
            - Source credibility indicators
            - Match percentage disclosure
            - Mobile-friendly presentation
            
            **TRUST & SAFETY:**
            - NEVER recommend from unverified sources
            - ALWAYS verify product authenticity
            - FLAG any suspicious listings
            - PROVIDE clear safety disclaimers when needed
            
            Remember: You help people make important purchasing decisions. 
            Be thorough, accurate, and safety-conscious.
        """),
        expected_output=dedent("""\
            # Shopping Recommendations 🛍️
            
            ## Search Summary
            - **User Requirements**: {summary of user preferences}
            - **Search Criteria**: {search parameters used}
            - **Trusted Sources**: {platforms searched}
            - **Match Threshold**: Minimum 50% match guarantee
            
            ## Top Recommendations
            
            ### Product 1: {Product Name}
            **Match Score**: XX% ✅
            **Price**: {Price with currency}
            **Brand**: {Brand Name}
            **Source**: {Trusted Platform}
            
            **Key Features:**
            - {Feature 1}
            - {Feature 2}
            - {Feature 3}
            
            **Why It Matches:**
            - {How it meets requirement 1}
            - {How it meets requirement 2}
            
            **Availability**: ✅ In Stock / ⚠️ Limited Stock / ❌ Out of Stock
            **Link**: {Purchase URL}
            
            ### Product 2: {Product Name}
            **Match Score**: XX% ✅
            **Price**: {Price with currency}
            **Brand**: {Brand Name}
            **Source**: {Trusted Platform}
            
            **Key Features:**
            - {Feature 1}
            - {Feature 2}
            - {Feature 3}
            
            **Why It Matches:**
            - {How it meets requirement 1}
            - {How it meets requirement 2}
            
            **Availability**: ✅ In Stock / ⚠️ Limited Stock / ❌ Out of Stock
            **Link**: {Purchase URL}
            
            ## Alternative Options
            {Brief mention of other options if top recommendations don't fully match}
            
            ## Safety & Trust Notes
            - All recommendations from verified, trusted sources
            - Prices and availability as of search time
            - Always verify product details before purchase
            - Use secure payment methods
            
            ## Next Steps
            - {Suggested actions for the user}
            - {Additional search options if needed}
            
            ---
            Search conducted by AI Shopping Partner
            Trusted Product Recommendation System
            Generated: {current_date}
            Last Updated: {current_time}
        """),
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Shopping Partner Agent initialized")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages."""
    global agent
    if not agent:
        error_msg = "Agent not initialized"
        raise RuntimeError(error_msg)

    # Run the agent and get response
    response = await agent.arun(messages)
    return response


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages with lazy initialization."""
    global _initialized

    # Lazy initialization on first call
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing Shopping Partner Agent...")
            await initialize_agent()
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result


async def cleanup() -> None:
    """Clean up any resources."""
    print("🧹 Cleaning up Shopping Partner Agent resources...")


def main():
    """Run the main entry point for the Shopping Partner Agent."""
    parser = argparse.ArgumentParser(description="Bindu Shopping Partner Agent")
    parser.add_argument(
        "--openai-api-key",
        type=str,
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key (env: OPENAI_API_KEY)",
    )
    parser.add_argument(
        "--openrouter-api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--exa-api-key",
        type=str,
        default=os.getenv("EXA_API_KEY"),
        help="Exa API key (env: EXA_API_KEY)",
    )
    parser.add_argument(
        "--mem0-api-key",
        type=str,
        default=os.getenv("MEM0_API_KEY"),
        help="Mem0 API key (env: MEM0_API_KEY)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o"),
        help="Model ID for OpenRouter (env: MODEL_NAME)",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to agent_config.json (optional)",
    )
    args = parser.parse_args()

    # Set environment variables if provided via CLI
    if args.openai_api_key:
        os.environ["OPENAI_API_KEY"] = args.openai_api_key
    if args.openrouter_api_key:
        os.environ["OPENROUTER_API_KEY"] = args.openrouter_api_key
    if args.exa_api_key:
        os.environ["EXA_API_KEY"] = args.exa_api_key
    if args.mem0_api_key:
        os.environ["MEM0_API_KEY"] = args.mem0_api_key
    if args.model:
        os.environ["MODEL_NAME"] = args.model

    print("🤖 Shopping Partner Agent - AI Product Recommendation System")
    print("🛍️ Capabilities: Smart product matching, trusted source verification, real-time availability checking")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        print("🚀 Starting Bindu Shopping Partner Agent server...")
        print(f"🌐 Server will run on: {config.get('deployment', {}).get('url', 'http://127.0.0.1:3773')}")
        bindufy(config, handler)
    except KeyboardInterrupt:
        print("\n🛑 Shopping Partner Agent stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Cleanup on exit
        asyncio.run(cleanup())


if __name__ == "__main__":
    main()