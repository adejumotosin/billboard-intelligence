import streamlit as st

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Billboard Optimization: Design Thinking Proposal",
    page_icon="📍",
    layout="wide"
)

# ---------------------------
# Title Section
# ---------------------------
st.title("📍 Billboard Advertising Location Intelligence System")
st.subheader("A Data-Driven Optimization Framework for Nigeria’s Outdoor Media Market")
st.markdown("**Presented Using the Design Thinking Framework**")
st.markdown("---")

# ---------------------------
# Sidebar Navigation
# ---------------------------
section = st.sidebar.radio("📌 Navigate Slides", [
    "Overview",
    "Empathize",
    "Define",
    "Ideate",
    "Prototype",
    "Test",
    "Outcomes",
    "Timeline & Resources",
    "Conclusion & Q&A"
])

# ---------------------------
# Slide Content Sections
# ---------------------------

if section == "Overview":
    st.header("🎯 Design Thinking Framework Overview")
    st.markdown("""
    The project follows the **Design Thinking** methodology to solve a major inefficiency in Nigeria’s ₦50B outdoor advertising market:
    
    **Design Thinking Phases:**
    1. **Empathize** – Understand stakeholder pain points
    2. **Define** – Frame the core problem clearly
    3. **Ideate** – Generate creative, human-centered solutions
    4. **Prototype** – Build a working system and models
    5. **Test** – Validate with users and iterate
    
    This approach ensures a human-centered, scalable, and context-aware solution.
    """)

elif section == "Empathize":
    st.header("🔎 EMPATHIZE: Understanding Stakeholders")
    st.subheader("👥 Key Stakeholders")
    st.markdown("""
    - **Advertisers**: Need to target the right audience with measurable ROI
    - **Agencies**: Require data to justify pricing and effectiveness
    - **Urban Planners**: Want efficient infrastructure use
    - **Regulators**: Need transparency in outdoor ad placements
    - **Commuters/Public**: Are the real audience, yet often ignored in planning
    """)
    st.subheader("❗ Pain Points Identified")
    st.markdown("""
    - Placement decisions are based on **intuition**, not evidence
    - **Low ROI** and wasted budget on ineffective locations
    - No tools to **correlate traffic/demographics to effectiveness**
    - **Event traffic** and **daypart visibility** are ignored
    """)

elif section == "Define":
    st.header("📌 DEFINE: Framing the Problem")
    st.subheader("🎯 Problem Statement")
    st.markdown("> Outdoor advertising decisions in Nigeria lack integrated data analysis, leading to inefficient placements and poor audience targeting.")
    
    st.subheader("💬 Design Challenge")
    st.markdown("> *How might we empower advertisers and media planners with a geospatial decision-support tool that optimizes billboard placements using traffic, demographic, and temporal insights?*")
    
    st.subheader("🔍 Research Questions")
    st.markdown("""
    - Which variables most influence billboard effectiveness?
    - Can we integrate multiple datasets (traffic, demographics, land use)?
    - How do patterns change by **time of day**, **weather**, and **events**?
    - Can this be made **replicable** across other African cities?
    """)

elif section == "Ideate":
    st.header("💡 IDEATE: Solution Generation")
    st.subheader("💻 Proposed System")
    st.markdown("""
    **Billboard Location Intelligence System**
    - Combines **spatial, demographic, and temporal** data
    - Produces **location scores** to guide billboard selection
    - Offers **interactive dashboards** for strategic planning
    """)
    
    st.subheader("🔧 Core Components")
    st.markdown("""
    - **Geospatial Mapping** (GIS, OpenStreetMap)
    - **Multi-Criteria Scoring** (MCDA, AHP)
    - **Dashboard Interface** (Streamlit)
    - **Data Sources**: Traffic APIs, Census Data, Field Survey
    """)
    
    st.subheader("🚀 Innovation Highlights")
    st.markdown("""
    - Optimized for **data-scarce environments**
    - **Open-source architecture** for replicability
    - Can be scaled to support **real-time forecasting**
    """)

elif section == "Prototype":
    st.header("🧪 PROTOTYPE: System Blueprint")
    
    st.subheader("🛠️ Technology Stack")
    st.markdown("""
    - **Backend**: Python, PostgreSQL + PostGIS, Apache Airflow
    - **Frontend**: Streamlit, Folium, Plotly
    - **APIs**: Google Maps Traffic Layer, OSM, Census data
    """)
    
    st.subheader("📊 Scoring Model (MCDA)")
    st.markdown("""
    **Weighted Criteria for Billboard Scoring:**
    - 🚦 Traffic Accessibility: 35%
    - 👥 Demographic Alignment: 25%
    - 🏗️ Infrastructure Quality: 20%
    - 📍 Competitive Saturation: 15%
    - ⏰ Temporal Optimization: 5%
    
    **Formula:**  
    `Score = (T^0.35 × D^0.25 × I^0.20 × C^0.15 × Temp^0.05)`
    """)
    
    st.subheader("🖥️ Dashboard Features")
    st.markdown("""
    - Map-based location viewer with clustering
    - Side-by-side location comparisons
    - Exportable reports (PDF, CSV)
    - "What-if" campaign scenario planner
    """)

elif section == "Test":
    st.header("🧪 TEST: Validation & Feedback")
    
    st.subheader("✅ Validation Methods")
    st.markdown("""
    - **Internal Testing**: Model cross-validation, sensitivity analysis
    - **External Validation**: Expert interviews (12+), retrospective case analysis
    - **User Testing**: Dashboard usability with planners & agencies
    """)
    
    st.subheader("📈 Success Metrics")
    st.markdown("""
    - 🔍 ≥ 0.70 correlation with actual market pricing
    - 🔁 < 15% score variation across time periods
    - 🌍 ≥ 90% coverage of target billboard locations
    """)

elif section == "Outcomes":
    st.header("📊 Expected Outcomes & Deliverables")
    
    st.subheader("📚 Academic Contributions")
    st.markdown("""
    - New MCDA framework for billboard scoring
    - Methodology for **data-light** environments
    - Open-source tools for urban location intelligence
    """)
    
    st.subheader("🏢 Industry Impact")
    st.markdown("""
    - **25–40% increase** in placement effectiveness
    - Improved **ROI prediction** models
    - More **transparent billboard pricing**
    """)
    
    st.subheader("📦 Deliverables")
    st.markdown("""
    - 📍 Geospatial database (500+ billboards)
    - 📊 Streamlit dashboard with API endpoints
    - 📘 Documentation & user manuals
    - 🌐 GitHub repository for public access
    """)

elif section == "Timeline & Resources":
    st.header("📆 Timeline & Resources")
    
    st.subheader("🗓️ 4-Week Timeline")
    st.markdown("""
    | Week | Focus | Milestone |
    |------|-------|-----------|
    | 1 | Data & Setup | Pipeline and 100+ locations |
    | 2 | Modeling | Functional MCDA Model |
    | 3 | Dashboard | Interactive UI built |
    | 4 | Validation | Testing, Documentation, Final Pitch |
    """)
    
    st.subheader("💰 Budget Estimate (₦30k – ₦65k)")
    st.markdown("""
    - API Access: ₦15,000 – ₦25,000  
    - Field Surveys: ₦8,000 – ₦15,000  
    - Hosting/Storage: ₦2,000 – ₦8,000  
    - Contingency: ₦5,000 – ₦12,000  
    """)

    st.subheader("👨‍💻 Team & Tools")
    st.markdown("""
    - Researcher (you), Faculty Advisor  
    - Volunteer Experts (marketing agencies)  
    - Python, PostGIS, Streamlit, OpenStreetMap  
    """)

elif section == "Conclusion & Q&A":
    st.header("✅ Conclusion & Next Steps")
    
    st.markdown("""
    This project represents a powerful opportunity to bring **data-driven transparency** to Nigeria’s ₦50B billboard market.

    With its **scalable framework**, this tool can:
    - Improve campaign ROI
    - Inform better urban policy
    - Set a precedent for ad-tech innovation in Africa
    """)

    st.subheader("📣 Call to Action")
    st.markdown("""
    - **Pilot test** with advertising agencies  
    - **Collaborate** with data providers & regulators  
    - **Release** as open-source for broader adoption  
    """)

    st.success("Thank you! Let’s revolutionize outdoor advertising—together.")
    st.markdown("---")
    st.write("**Q&A Time — What would you like to discuss or suggest?**")
