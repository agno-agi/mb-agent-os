# AgentOS

Welcome to your AgentOS: a robust, production-ready application for serving agents, multi-agent teams and agentic workflows. It includes:

- An **AgentOS server** for serving agents, multi-agent teams and agentic workflows.
- A **PostgreSQL database** for storing agent sessions, knowledge, and memories.
- A set of **pre-built agents, teams and workflows** to use as a starting point.

For more information, checkout [Agno](https://agno.link/gh) and give it a ⭐️

## Quickstart

Follow these steps to get your AgentOS up and running:

> Prerequisites: [docker desktop](https://www.docker.com/products/docker-desktop) should be installed and running.

### Clone the repo

```sh
git clone https://github.com/agno-agi/mb-agent-os.git
cd mb-agent-os
```

### Configure API keys

We'll use sonnet 4.5 as the default model, please export the `ANTHROPIC_API_KEY` environment variable to get started.

```sh
export ANTHROPIC_API_KEY="YOUR_API_KEY_HERE"
```

We also use `OPENAI_API_KEY` to generate embeddings for knowledge bases. So, please export the `OPENAI_API_KEY` environment variable to use agents with knowledge bases.

```sh
export OPENAI_API_KEY="YOUR_API_KEY_HERE"
```

Finally, we use Exa for the Research Agent. So, please export the `EXA_API_KEY` environment variable to use the Research Agent.

```sh
export EXA_API_KEY="YOUR_API_KEY_HERE"
```

> [!TIP]
> You can use the `example.env` file as a template to create your own `.env` file.

### Start the application

Run the application using docker compose:

```sh
docker compose up -d
```

This command starts:

- The **AgentOS server**, running on [http://localhost:8000](http://localhost:8000).
- The **PostgreSQL database** for storing agent sessions, knowledge, and memories, accessible on `localhost:5432`.

Once started, you can:

- View the AgentOS server documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

### Connect the AgnoUI to the AgentOS server

- Open the [Agno UI](https://os.agno.com)
- Login and add `http://localhost:8000` as a new AgentOS. You can call it `Local AgentOS` (or any name you prefer).

### Stop the application

When you're done, stop the application using:

```sh
docker compose down
```

## Prebuilt Agents

The `/agents` folder contains pre-built agents that you can use as a starting point.

* **Agno MCP Agent**: An Agent that can help answer questions about Agno using Agno's MCP server. This is a great starting point for building Agents that need to MCP.

* **Agno Knowledge Agent**: An Agent that loads the Agno documentation in a knowledge base and answers questions about Agno. Please run `docker exec -it mb-agent-os-agent-os-1 python -m agents.agno_knowledge_agent` to load the Agno documentation into the knowledge base.

* **Finance Agent**: An agent that uses the YFinance API to get stock prices and financial data.

* **Research Agent**: An agent that can search the web/Exa for information.

* **Memory Manager**: An agent that can manage user memories.

* **YouTube Agent**: An agent that can search YouTube for videos and answer questions about them.

## Prebuilt Teams

The `/teams` folder contains pre-built teams that you can use as a starting point.

* **Finance Team**: A team of agents that can work together to analyze financial data.

## Prebuilt Workflows

The `/workflows` folder contains pre-built workflows that you can use as a starting point.

* **Research Workflow**: A workflow that can research information from multiple sources simultaneously.

## Development Setup

To setup your local virtual environment:

### Install `uv`

We use `uv` for python environment and package management. Install it by following the the [`uv` documentation](https://docs.astral.sh/uv/#getting-started) or use the command below for unix-like systems:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Create Virtual Environment & Install Dependencies

Run the `dev_setup.sh` script. This will create a virtual environment and install project dependencies:

```sh
./scripts/dev_setup.sh
```

### Activate Virtual Environment

Activate the created virtual environment:

```sh
source .venv/bin/activate
```

(On Windows, the command might differ, e.g., `.venv\Scripts\activate`)

## Managing Python Dependencies

If you need to add or update python dependencies:

### Modify pyproject.toml

Add or update your desired Python package dependencies in the `[dependencies]` section of the `pyproject.toml` file.

### Generate requirements.txt

The `requirements.txt` file is used to build the application image. After modifying `pyproject.toml`, regenerate `requirements.txt` using:

```sh
./scripts/generate_requirements.sh
```

To upgrade all existing dependencies to their latest compatible versions, run:

```sh
./scripts/generate_requirements.sh upgrade
```

### Rebuild Docker Images

Rebuild your Docker images to include the updated dependencies:

```sh
docker compose up -d --build
```

## Community & Support

Need help, have a question, or want to connect with the community?

- 📚 **[Read the Agno Docs](https://docs.agno.com)** for more in-depth information.
- 💬 **Chat with us on [Discord](https://agno.link/discord)** for live discussions.
- ❓ **Ask a question on [Discourse](https://agno.link/community)** for community support.
- 🐛 **[Report an Issue](https://github.com/agno-agi/agent-api/issues)** on GitHub if you find a bug or have a feature request.

## Running in Production

This repository includes a `Dockerfile` for building a production-ready container image of the application.

The general process to run in production is:

1. Update the `scripts/build_image.sh` file and set your IMAGE_NAME and IMAGE_TAG variables.
2. Build and push the image to your container registry:

```sh
./scripts/build_image.sh
```

3. Run in your cloud provider of choice.
