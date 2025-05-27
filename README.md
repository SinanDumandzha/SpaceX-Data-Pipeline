# 🚀 SpaceX Missions Data Pipeline

An end-to-end data pipeline project designed to extract, transform, and load SpaceX launch data using Singer Taps and Targets, with data modeling handled by dbt and storage/processing in Snowflake. This project provides an efficient and modular pipeline for analyzing real-world data using modern data stack tools.

## 📦 Technologies Used

- **Python**  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
- **Pandas**  ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white)
- **NumPy**  ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white)
- **Singer.io**  ![Singer](https://img.shields.io/badge/-Singer.io-000000?style=flat&logo=data&logoColor=white)
- **dbt**  ![dbt](https://img.shields.io/badge/-dbt-FF694B?style=flat&logo=dbt&logoColor=white)
- **Snowflake**  ![Snowflake](https://img.shields.io/badge/-Snowflake-29B5E8?style=flat&logo=snowflake&logoColor=white)

## 🛠️ Installation Instructions

**1. Clone the Repository**
   ```bash
   git clone https://github.com/SinanDumandzha/SpaceX-Data-Pipeline.git
   cd SpaceX-Data-Pipeline
   ```

**2. Set Up Virtual Environment (Recommended)**
 ```bash
 python -m venv venv
 source venv/bin/activate  # On Windows: venv\Scripts\activate
 Install Python Dependencies
 ```

**3. Install Python Dependencies**
 ```bash
 pip install -r requirements.txt
 ```

**4. Install Singer Tap and Target**
Example (adjust according to the tap/target you use):
```bash
pip install singer-python
pip install tap-rest-api
pip install target-snowflake
```

**5. Configure Singer Tap & Target**
- Create config.json, catalog.json, and state.json files for the tap.
- Create a target_config.json for the Snowflake connection.

**6. Run the Singer ETL Pipeline**
```bash
 tap-spacex | target-snowflake
```

**7. Configure and Run dbt**
- Edit profiles.yml to include your Snowflake credentials.
- Initialize dbt and run transformations:
```bash
dbt deps
dbt run
dbt test
```

## 🚀 Usage Example
1. Extract SpaceX data using a Singer Tap from the SpaceX API.
2. Load the data into Snowflake using a Singer Target.
3. Transform and model the data using dbt.
4. Run analytics on clean, well-structured datasets.

## 📷 Screenshots

- **10 launches:**

![Launches (10)](https://github.com/SinanDumandzha/SpaceX-Data-Pipeline/blob/main/screenshots/10-launches.PNG)

- **Launches by rocket:**

![Launches by rocket](https://github.com/SinanDumandzha/SpaceX-Data-Pipeline/blob/main/screenshots/launches-by-rocket.PNG)

- **Success rate:**

![Success rate](https://github.com/SinanDumandzha/SpaceX-Data-Pipeline/blob/main/screenshots/success-rate.PNG)

- **Launches per year:**

![Launches per year](https://github.com/SinanDumandzha/SpaceX-Data-Pipeline/blob/main/screenshots/launches-per-year.PNG)

- **Create View - Successful Launches**
  
![Create View - Successful Launches](https://github.com/SinanDumandzha/SpaceX-Data-Pipeline/blob/main/screenshots/create-view-successful-launches.PNG)