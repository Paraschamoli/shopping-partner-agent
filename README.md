<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Shopping Partner Agent</h1>
<h3 align="center">AI-Powered Personal Shopping Assistant</h3>

<p align="center">
  <strong>Smart product recommendations from trusted e-commerce platforms with 50% match guarantee</strong><br/>
  Discover, compare, and choose products based on preferences, budget, and needs with AI-powered shopping intelligence
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/shopping-partner-agent/actions/workflows/build-and-push.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/shopping-partner-agent/build-and-push.yml?branch=main" alt="Build Status">
  </a>
  <a href="https://pypi.org/project/shopping-partner-agent/">
    <img src="https://img.shields.io/pypi/v/shopping-partner-agent" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python Version">
  <a href="https://github.com/Paraschamoli/shopping-partner-agent/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Paraschamoli/shopping-partner-agent" alt="License">
  </a>
</p>

---

## 🎯 What is Shopping Partner Agent?

An AI-powered personal shopping assistant that helps users discover, compare, and choose products based on preferences, budget, and needs. Think of it as having a personal shopper available 24/7 who only recommends from trusted sources.

### Key Features
*   **🔍 Smart Product Matching** - Minimum 50% match guarantee with user requirements
*   **🛡️ Trusted Source Verification** - Searches only authentic platforms: Amazon, Flipkart, Myntra, Google Shopping, etc.
*   **📦 Real-time Availability** - Verifies products are in stock and available for purchase
*   **✅ Quality Assurance** - Avoids counterfeit or unverified products
*   **💰 Budget Optimization** - Finds best products within specified budget constraints
*   **⚡ Lazy Initialization** - Fast boot times, initializes on first request
*   **🔐 Secure API Handling** - No API keys required at startup

---

## 🛠️ Tools & Capabilities

### Built-in Tools
*   **ExaTools** - Advanced search for product discovery (preferred)
*   **DuckDuckGoTools** - Web search fallback for basic product information
*   **Mem0Tools** - Memory and personalized recommendations (optional)

### Shopping Protocol
1.  **Requirement Analysis** - Carefully analyze all user preferences and requirements
2.  **Trusted Source Search** - Search only authentic e-commerce platforms
3.  **Match Assessment** - Ensure products match at least 50% of user requirements
4.  **Availability Verification** - Confirm products are in stock and available
5.  **Information Presentation** - Provide comprehensive product details with safety disclaimers

---

> **🌐 Join the Internet of Agents**
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. It takes 2 minutes and unlocks the full potential of your agent.

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/shopping-partner-agent.git
cd shopping-partner-agent

# Set up virtual environment with uv
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key (choose one):
# OPENAI_API_KEY=sk-...      # For OpenAI GPT-4o
# OPENROUTER_API_KEY=sk-...  # For OpenRouter (cheaper alternative)
# EXA_API_KEY=sk-...         # For enhanced product search (optional)
# MEM0_API_KEY=sk-...        # For memory features (optional)
```

### 3. Run Locally

```bash
# Start the shopping partner agent
python -m shopping_partner_agent

# Or using uv
uv run python -m shopping_partner_agent
```

### 4. Test with Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access at: http://localhost:3773
```

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file:

```env
# Choose ONE provider (both can be set, OpenAI takes priority)
OPENAI_API_KEY=sk-...      # OpenAI API key
OPENROUTER_API_KEY=sk-...  # OpenRouter API key (alternative)

# Optional - for enhanced features
EXA_API_KEY=sk-...         # Exa API key for enhanced product search
MEM0_API_KEY=sk-...        # Mem0 API key for memory operations

# Optional
DEBUG=true                # Enable debug logging
MODEL_NAME=openai/gpt-4o  # Model override
```

### Port Configuration
Default port: `3773` (can be changed in `agent_config.json`)

---

## 💡 Usage Examples

### Via HTTP API

```bash
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "I am looking for running shoes with the following preferences: Color: Black Purpose: Comfortable for long-distance running Budget: Under Rs. 10,000. Search only from trusted platforms like Amazon or Flipkart."
      }
    ]
  }'
```

### Sample Shopping Queries
*   "Find a laptop for programming: Budget: $1000-1500, RAM: 16GB minimum, SSD: 512GB, Brand preference: Dell or Lenovo, Only from verified sellers."
*   "Recommend a smartphone with good camera: Budget: $500-800, Battery life important, 5G required, Available in stock today."
*   "Looking for a coffee machine: Type: Espresso, Budget: $200-400, Countertop space limited, Must be available on Amazon with prime delivery."
*   "Find gifts for a 10-year-old: Interests: Robotics and coding, Budget: $50-100 per gift, Educational and safe products only."
*   "I need wireless headphones: Budget: $100-200, Noise cancellation important, Comfortable for long use, From trusted brands only."

### Expected Output Format

```markdown
# Shopping Recommendations 🛍️

## Search Summary
- **User Requirements**: Running shoes, Black, Long-distance, Under Rs. 10,000
- **Search Criteria**: Trusted platforms only, In stock verification
- **Match Threshold**: Minimum 50% match guarantee

## Top Recommendations

### Product 1: Nike Air Zoom Pegasus 39
**Match Score**: 92% ✅
**Price**: Rs. 8,999
**Brand**: Nike
**Source**: Amazon (Verified Seller)

**Key Features:**
- Black color with reflective details
- Zoom Air cushioning for long-distance comfort
- Breathable mesh upper
- Durable rubber outsole

**Why It Matches:**
- Perfect color match (Black)
- Specifically designed for long-distance running
- Within budget (Rs. 8,999 < Rs. 10,000)

**Availability**: ✅ In Stock (Prime Delivery)
**Link**: https://amazon.in/nike-air-zoom-pegasus-39

### Product 2: ASICS Gel-Cumulus 25
**Match Score**: 85% ✅
**Price**: Rs. 9,499
**Brand**: ASICS
**Source**: Flipkart (Assured Seller)

**Key Features:**
- Black with silver accents
- GEL technology cushioning
- Breathable mesh construction
- Rearfoot and forefoot GEL

**Why It Matches:**
- Color matches user preference
- Excellent cushioning for long runs
- Within specified budget range

**Availability**: ✅ In Stock (Free Delivery)
**Link**: https://flipkart.com/asics-gel-cumulus-25

## Safety & Trust Notes
- All recommendations from verified, trusted sources
- Prices and availability as of search time
- Always verify seller ratings before purchase
- Use secure payment methods on e-commerce platforms

## Next Steps
- Check size availability for your preferred option
- Read recent customer reviews
- Compare delivery options and timelines

---
Search conducted by AI Shopping Partner
Trusted Product Recommendation System
Generated: 2026-01-13
Last Updated: 15:30:00
```

---

## 🐳 Docker Deployment

### Quick Docker Setup

```bash
# Build the image
docker build -t shopping-partner-agent .

# Run container
docker run -d \
  -p 3773:3773 \
  -e OPENAI_API_KEY=your_key_here \
  --name shopping-partner-agent \
  shopping-partner-agent

# Check logs
docker logs -f shopping-partner-agent
```

### Docker Compose (Recommended)
`docker-compose.yml`

```yaml
version: '3.8'
services:
  shopping-partner-agent:
    build: .
    ports:
      - "3773:3773"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - EXA_API_KEY=${EXA_API_KEY}
      - MEM0_API_KEY=${MEM0_API_KEY}
    restart: unless-stopped
```

Run with Compose:

```bash
# Start with compose
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 📁 Project Structure

```text
shopping-partner-agent/
├── shopping_partner_agent/
│   ├── __init__.py          # Package initialization
│   ├── __version__.py       # Version information
│   └── main.py              # Main agent implementation
├── skills/
│   └── shopping-partner/
│       └── skill.yaml       # Skill configuration
├── agent_config.json        # Bindu agent configuration
├── pyproject.toml           # Python dependencies
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # Docker Compose setup
├── README.md                # This documentation
├── .env.example             # Environment template
└── uv.lock                  # Dependency lock file
```

---

## 🔌 API Reference

### Health Check
```bash
GET http://localhost:3773/health
```
Response:
```json
{"status": "healthy", "agent": "Shopping Partner Agent"}
```

### Chat Endpoint
```bash
POST http://localhost:3773/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Your shopping query here"}
  ]
}
```

### Agent Information
```bash
GET http://localhost:3773/agent/info
```

---

## 🧪 Testing

### Local Testing

```bash
# Install test dependencies
uv sync --group dev

# Run tests
pytest tests/

# Test with specific API key
OPENAI_API_KEY=test_key python -m pytest
```

### Integration Test

```bash
# Start agent
python -m shopping_partner_agent &

# Test API endpoint
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Find black running shoes under $100"}]}'
```

---

## 🚨 Troubleshooting

### Common Issues & Solutions

**"ModuleNotFoundError"**
```bash
uv sync --force
```

**"Port 3773 already in use"**
Change port in `agent_config.json` or kill the process:
```bash
lsof -ti:3773 | xargs kill -9
```

**"No API key provided"**
Check if `.env` exists and variable names match. Or set directly:
```bash
export OPENAI_API_KEY=your_key
```

**"Exa tools not available"**
Install optional dependency or agent will use DuckDuckGo fallback:
```bash
pip install exa-py
```

**Docker build fails**
```bash
docker system prune -a
docker-compose build --no-cache
```

---

## 📊 Dependencies

### Core Packages
*   **bindu** - Agent deployment framework
*   **agno** - AI agent framework
*   **openai** - OpenAI client
*   **exa-py** - Enhanced search for product discovery
*   **duckduckgo-search** - Web search fallback
*   **python-dotenv** - Environment management
*   **mem0ai** - Memory operations (optional)
*   **requests** - HTTP requests
*   **rich** - Console output

### Development Packages
*   **pytest** - Testing framework
*   **ruff** - Code formatting/linting
*   **pre-commit** - Git hooks

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/improvement`
3.  Make your changes following the code style
4.  Add tests for new functionality
5.  Commit with descriptive messages
6.  Push to your fork
7.  Open a Pull Request

**Code Style:**
*   Follow PEP 8 conventions
*   Use type hints where possible
*   Add docstrings for public functions
*   Keep functions focused and small

---

## 📄 License
MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Credits & Acknowledgments
*   **Developer:** Paras Chamoli
*   **Framework:** Bindu - Agent deployment platform
*   **Agent Framework:** Agno - AI agent toolkit
*   **Search Tools:** Exa Search API & DuckDuckGo Search API
*   **E-commerce Platforms:** Amazon, Flipkart, Myntra, Google Shopping integration

### 🔗 Useful Links
*   🌐 **Bindu Directory:** [bindus.directory](https://bindus.directory)
*   📚 **Bindu Docs:** [docs.getbindu.com](https://docs.getbindu.com)
*   🐙 **GitHub:** [github.com/Paraschamoli/shopping-partner-agent](https://github.com/Paraschamoli/shopping-partner-agent)
*   💬 **Discord:** Bindu Community

---

<p align="center">
  <strong>Built with ❤️ by Paras Chamoli</strong><br/>
  <em>Transforming shopping experiences with AI-powered personal assistance</em>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/shopping-partner-agent/stargazers">⭐ Star on GitHub</a> •
  <a href="https://bindus.directory">🌐 Register on Bindu</a> •
  <a href="https://github.com/Paraschamoli/shopping-partner-agent/issues">🐛 Report Issues</a>
</p>

> **Note:** This agent follows the Bindu pattern with lazy initialization and secure API key handling. It boots without API keys and only fails at runtime if keys are needed but not provided.
