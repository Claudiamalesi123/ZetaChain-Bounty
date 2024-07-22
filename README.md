
---

# Decentralized Crowdfunding Platform

Welcome to the **Decentralized Crowdfunding Platform**! This app allows users to simulate crowdfunding campaigns where projects can raise funds in BTC. The platform features different categories of projects, allowing backers to support initiatives across various domains.

**App URL deployed on Streamlit:** [Decentralized Crowdfunding Platform](https://zetachain-bounty-claudiamalesi.streamlit.app/)

## Overview

This application is built using Streamlit and includes functionality to:
- Display projects within various categories.
- Allow users to back projects with BTC.
- Maintain a transaction history.
- Switch between categories using a sidebar menu.

## Code Explanation

### `app.py`

The main script of the application is `app.py`. Below is a breakdown of its components and functionality:

1. **Imports and Initialization**

   ```python
   import streamlit as st
   from faker import Faker
   from datetime import datetime
   ```

   - `streamlit` is used for creating the web application.
   - `Faker` is used to generate mock names for backers.
   - `datetime` is used to timestamp transactions.

2. **Categories and Projects Definition**

   ```python
   categories = {
       "Technology": [ ... ],
       "Sustainability": [ ... ],
       "Art": [ ... ],
       "Health": [ ... ],
       "Education": [ ... ]
   }
   ```

   This dictionary contains project categories and their respective projects, including details like `id`, `name`, `goal`, `raised`, `description`, `image`, and `category`.

3. **Session State Initialization**

   ```python
   if 'projects' not in st.session_state:
       st.session_state.projects = categories["Technology"]
   if 'transactions' not in st.session_state:
       st.session_state.transactions = []
   if 'current_category_index' not in st.session_state:
       st.session_state.current_category_index = 0
   ```

   Initializes session state variables for `projects`, `transactions`, and `current_category_index`.

4. **Functions**

   - **`simulate_transaction(project_id, amount)`**

     Simulates a transaction by updating the `raised` amount of the selected project and appending the transaction details to `transactions`.

   - **`display_projects()`**

     Displays projects for the current category, showing project details and progress bars. Allows users to back projects with BTC using a form.

   - **`display_transactions()`**

     Shows a history of transactions including project names, amounts, backers, and timestamps.

   - **`change_category(category_index)`**

     Changes the current category based on the index provided and updates the displayed projects.

5. **Sidebar and Category Selection**

   ```python
   st.sidebar.title("Categories")
   categories_list = list(categories.keys())
   selected_category = st.sidebar.radio("Select a category", categories_list, index=st.session_state.current_category_index)
   change_category(categories_list.index(selected_category))
   ```

   Provides a sidebar for selecting project categories. Changes the displayed projects based on the selected category.

6. **Displaying Projects and Transactions**

   ```python
   display_projects()
   display_transactions()
   ```

   Calls functions to display projects and transaction history.

### `requirements.txt`

The `requirements.txt` file lists the dependencies required to run the application:

```
streamlit
Faker
```

These libraries are necessary for running the Streamlit app and generating mock data.

---

