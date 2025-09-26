@echo off
:: One-Click Environment Setup for Siemens Energy Digitalization Live Web App
:: Built by Heider Jeffer

:: Display welcome message
echo ==============================================
echo One-Click Environment Setup
echo Built by Heider Jeffer
echo ==============================================

:: -------------------------------
:: Variables
SET ENV_NAME=project11
SET PYTHON_VERSION=3.11

:: -------------------------------
:: 1️⃣ Create Conda environment
echo Creating Conda environment %ENV_NAME% with Python %PYTHON_VERSION%...
conda create -n %ENV_NAME python=%PYTHON_VERSION% ipykernel -y

:: -------------------------------
:: 2️⃣ Activate environment
echo Activating environment...
call conda activate %ENV_NAME%

:: -------------------------------
:: 3️⃣ Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: -------------------------------
:: 4️⃣ Install all required packages
echo Installing Python packages...
pip install streamlit matplotlib seaborn
pip install pomegranate
pip install hmmlearn
pip install wordcloud
pip install alpha_vantage
pip install yfinance
pip install pulp
pip install onnx
pip install gekko
pip install beautifulsoup4
pip install lxml
pip install keras
pip install numpy
pip install opencv-python
pip install pandas
pip install plotly
pip install torch torchvision
pip install scikit-learn
pip install scipy
pip install statsmodels
pip install tclab
pip install tensorflow
pip install xgboost
pip install jupyterlab notebook
pip install nltk
pip install PyDrive
pip install pandas-profiling[notebook]
pip install jupyter_contrib_nbextensions

:: -------------------------------
:: 5️⃣ Enable Jupyter extensions
echo Enabling Jupyter extensions...
jupyter nbextension enable --py widgetsnbextension
jupyter contrib nbextension install --user
jupyter nbextension list

:: -------------------------------
:: 6️⃣ Launch Jupyter Lab
echo Launching Jupyter Lab...
jupyter-lab
