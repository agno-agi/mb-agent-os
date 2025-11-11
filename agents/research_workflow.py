from os import getenv
from textwrap import dedent

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools
from agno.tools.hackernews import HackerNewsTools
from agno.tools.reasoning import ReasoningTools
from agno.workflow import Workflow
from agno.workflow.parallel import Parallel

from db.demo_db import demo_db

# ============================================================================
# Create Research Agents
# ============================================================================
hn_researcher = Agent(
    name="HN Researcher",
    role="Research trending topics and discussions on Hacker News",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[HackerNewsTools()],
    description=dedent("""\
        You are the HN Researcher — an agent that searches Hacker News for relevant discussions,
        trending topics, and technical insights from the developer community.
        """),
    instructions=dedent("""\
        1. Search Hacker News for relevant stories, discussions, and comments on the given topic.
        2. Focus on highly-voted stories and insightful comments.
        3. Identify key themes, opinions, and technical details from the community.
        4. Summarize your findings in a clear, organized format with links to sources.
        """),
    add_history_to_context=True,
    markdown=True,
    db=demo_db,
)

web_researcher = Agent(
    name="Web Researcher",
    role="Search the web for current information and sources",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[DuckDuckGoTools()],
    description=dedent("""\
        You are the Web Researcher — an agent that searches the web for up-to-date information,
        news articles, and credible sources on any topic.
        """),
    instructions=dedent("""\
        1. Search the web for recent and relevant information on the given topic.
        2. Prioritize credible sources like news sites, official documentation, and reputable publications.
        3. Gather diverse perspectives and factual information.
        4. Summarize findings with clear citations and links.
        """),
    add_history_to_context=True,
    markdown=True,
    db=demo_db,
)

exa_researcher = Agent(
    name="Exa Researcher",
    role="Perform deep semantic search for high-quality content",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[ExaTools(type="keyword")],
    description=dedent("""\
        You are the Exa Researcher — an agent that uses semantic search to find
        high-quality, relevant content from across the web.
        """),
    instructions=dedent("""\
        1. Use Exa's semantic search to find highly relevant, quality content.
        2. Focus on authoritative sources, in-depth articles, and expert analysis.
        3. Provide context and summaries of the most valuable findings.
        4. Include links to all sources.
        """),
    add_history_to_context=True,
    markdown=True,
    db=demo_db,
)

# ============================================================================
# Create Writer and Reviewer Agents
# ============================================================================
writer = Agent(
    name="Writer",
    role="Synthesize research into compelling content",
    model=Claude(id="claude-sonnet-4-5"),
    tools=[ReasoningTools()],
    description=dedent("""\
        You are the Writer — an agent that synthesizes research findings into clear,
        engaging, and well-structured content.
        """),
    instructions=dedent("""\
        1. Review all research findings from the parallel research phase.
        2. Identify key themes, insights, and important details.
        3. Structure the content logically with clear sections.
        4. Write in a clear, engaging style appropriate for the topic.
        5. Include relevant citations and links from the research.
        6. Use reasoning tools to think through complex topics and structure.
        """),
    add_history_to_context=True,
    markdown=True,
    db=demo_db,
)

reviewer = Agent(
    name="Reviewer",
    role="Review and refine content for quality and accuracy",
    model=Claude(id="claude-sonnet-4-5"),
    description=dedent("""\
        You are the Reviewer — an agent that reviews content for quality, accuracy,
        clarity, and completeness.
        """),
    instructions=dedent("""\
        1. Review the written content thoroughly.
        2. Check for factual accuracy based on the research.
        3. Ensure the content is well-structured and flows logically.
        4. Verify that all sources are properly cited.
        5. Suggest improvements for clarity, conciseness, and engagement.
        6. Provide a final polished version with any necessary edits.
        """),
    add_history_to_context=True,
    markdown=True,
    db=demo_db,
)

# ============================================================================
# Build Workflow with Conditional Exa Researcher
# ============================================================================
# Start with base researchers
researchers = [hn_researcher, web_researcher]

# Add Exa researcher only if API key is available
if getenv("EXA_API_KEY"):
    researchers.append(exa_researcher)

# Create the workflow
research_workflow = Workflow(
    name="Research Workflow",
    description=dedent("""\
        A parallel workflow that researches information from multiple sources simultaneously,
        then synthesizes and reviews the information for publication.
        """),
    steps=[
        Parallel(*researchers, name="Research Phase"),
        writer,
        reviewer,
    ],
    db=demo_db,
)
