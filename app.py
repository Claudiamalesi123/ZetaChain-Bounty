import streamlit as st
from faker import Faker
from datetime import datetime

# Initialize Faker for generating mock data
fake = Faker()

# Define categories and projects with the provided image URLs
categories = {
    "Technology": [
        {"id": 1, "name": "Project Alpha", "goal": 50.0, "raised": 20.0, "description": "An innovative project to revolutionize technology.", "image": "https://i.pinimg.com/564x/66/62/af/6662af5359c558c563fee6f8fdaf3c5f.jpg", "category": "Technology"},
        {"id": 2, "name": "Project Beta", "goal": 75.0, "raised": 50.0, "description": "A community-driven project for sustainable living.", "image": "https://i.pinimg.com/564x/a7/21/65/a721656a86cc4142772cfdfbdc119b64.jpg", "category": "Technology"},
        {"id": 3, "name": "Project Gamma", "goal": 30.0, "raised": 15.0, "description": "A creative project to support local artists.", "image": "https://i.pinimg.com/564x/7d/17/88/7d1788bdb070b9813fc5ab531a634618.jpg", "category": "Technology"}
    ],
    "Sustainability": [
        {"id": 4, "name": "Project Delta", "goal": 60.0, "raised": 10.0, "description": "A project aimed at improving public health.", "image": "https://i.pinimg.com/564x/02/55/ab/0255ab8d033408ebe61fa808084e4d36.jpg", "category": "Sustainability"},
        {"id": 5, "name": "Project Epsilon", "goal": 40.0, "raised": 5.0, "description": "An educational initiative to enhance learning.", "image": "https://i.pinimg.com/564x/ee/db/ff/eedbffe7da9bb9cf1e02094ebd794316.jpg", "category": "Sustainability"},
        {"id": 6, "name": "Project Zeta", "goal": 70.0, "raised": 25.0, "description": "A project for environmental conservation.", "image": "https://i.pinimg.com/564x/bf/85/1f/bf851f9d54bc1607003921590ae71501.jpg", "category": "Sustainability"}
    ],
    "Art": [
        {"id": 7, "name": "Project Eta", "goal": 55.0, "raised": 30.0, "description": "A project supporting local artists.", "image": "https://i.pinimg.com/564x/cf/d6/7c/cfd67cf1c0bb1c311b185c144dd211b6.jpg", "category": "Art"},
        {"id": 8, "name": "Project Theta", "goal": 90.0, "raised": 45.0, "description": "A project for promoting art education.", "image": "https://i.pinimg.com/564x/ff/e6/67/ffe66751ef98f026c42a9e71f5015027.jpg", "category": "Art"},
        {"id": 9, "name": "Project Iota", "goal": 80.0, "raised": 35.0, "description": "A creative project to support art installations.", "image": "https://i.pinimg.com/564x/ce/35/00/ce350044642d806741394546ad1bc3fc.jpg", "category": "Art"}
    ],
    "Health": [
        {"id": 10, "name": "Project Kappa", "goal": 60.0, "raised": 15.0, "description": "A project aimed at improving mental health.", "image": "https://i.pinimg.com/564x/ae/34/c5/ae34c5eb9e7abbe55e8ce4297204d526.jpg", "category": "Health"},
        {"id": 11, "name": "Project Lambda", "goal": 40.0, "raised": 10.0, "description": "A project for health awareness.", "image": "https://i.pinimg.com/736x/98/04/cc/9804cc584897f606c08a563d12ab8176.jpg", "category": "Health"},
        {"id": 12, "name": "Project Mu", "goal": 70.0, "raised": 25.0, "description": "A project focused on medical research.", "image": "https://i.pinimg.com/564x/d0/fd/68/d0fd686d9f97f4c8ee97e6f722f06ccc.jpg", "category": "Health"}
    ],
    "Education": [
        {"id": 13, "name": "Project Nu", "goal": 50.0, "raised": 20.0, "description": "An initiative to support educational programs.", "image": "https://i.pinimg.com/736x/23/5b/a3/235ba3e6371a964bc580cd6aeb1af39b.jpg", "category": "Education"},
        {"id": 14, "name": "Project Xi", "goal": 80.0, "raised": 30.0, "description": "A project for enhancing educational tools.", "image": "https://i.pinimg.com/564x/07/74/7f/07747f4ca6e85dabe44809ac2508e567.jpg", "category": "Education"},
        {"id": 15, "name": "Project Omicron", "goal": 70.0, "raised": 25.0, "description": "A project for educational scholarships.", "image": "https://i.pinimg.com/736x/40/d7/82/40d782832ff4773ddbf4e537d76f0c9d.jpg", "category": "Education"}
    ]
}

# Initialize session state if not already initialized
if 'projects' not in st.session_state:
    st.session_state.projects = categories["Technology"]
if 'transactions' not in st.session_state:
    st.session_state.transactions = []
if 'current_category_index' not in st.session_state:
    st.session_state.current_category_index = 0

def simulate_transaction(project_id, amount):
    projects = st.session_state.projects
    for project in projects:
        if project["id"] == project_id:
            project["raised"] += amount
            st.session_state.transactions.append({
                "project_id": project_id,
                "amount": amount,
                "backer": fake.name(),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            break
    st.session_state.projects = projects

def display_projects():
    st.title("Decentralized Crowdfunding Platform")
    st.markdown("### A platform to simulate decentralized crowdfunding.")
    
    # Display projects for the current category
    cols = st.columns(3)
    for idx, project in enumerate(st.session_state.projects):
        with cols[idx % 3]:
            st.image(project["image"], use_column_width=True)
            st.subheader(project["name"])
            st.write(f"Category: {project['category']}")
            st.write(f"Description: {project['description']}")
            st.write(f"Goal: {project['goal']} BTC")
            st.write(f"Raised: {project['raised']} BTC")
            progress = project['raised'] / project['goal']
            st.markdown(f"""
            <style>
            .progress-bar {{
                height: 20px;
                width: 100%;
                background-color: #e0e0e0;
                border-radius: 5px;
                overflow: hidden;
            }}
            .progress {{
                height: 100%;
                background-color: #ff4d4d;
                width: {progress * 100}%;
                transition: width 0.5s ease-in-out;
            }}
            </style>
            <div class='progress-bar'><div class='progress'></div></div>
            """, unsafe_allow_html=True)

            if progress < 1:
                with st.form(f"back_project_{project['id']}"):
                    amount = st.number_input(
                        "Enter amount to back this project (BTC)",
                        min_value=0.01,
                        max_value=float(project['goal'] - project['raised']),
                        value=0.01,
                        step=0.01,
                        key=f"amount_{project['id']}"
                    )
                    submitted = st.form_submit_button("Back this project")
                    if submitted:
                        simulate_transaction(project["id"], amount)
                        st.success("Transaction successful!")

def display_transactions():
    st.markdown("### Transaction History")
    for txn in st.session_state.transactions:
        project = next((p for p in st.session_state.projects if p["id"] == txn["project_id"]), None)
        if project:
            st.write(f"Project: {project['name']}, Amount: {txn['amount']} BTC, Backer: {txn['backer']}, Date: {txn['date']}")

def change_category(category_index):
    st.session_state.current_category_index = category_index
    categories_list = list(categories.keys())
    category_name = categories_list[category_index]
    st.session_state.projects = categories[category_name]

st.sidebar.title("Categories")
categories_list = list(categories.keys())
selected_category = st.sidebar.radio("Select a category", categories_list, index=st.session_state.current_category_index)
change_category(categories_list.index(selected_category))

# Display projects and transactions
display_projects()
display_transactions()

